from statistics import mean
from agridata.service import AgriDataService


def _parse_price(value: str) -> float | None:
    if not value:
        return None
    cleaned = value.strip()
    if cleaned.startswith("€"):
        cleaned = cleaned[1:]
    cleaned = cleaned.replace(",", "").replace(" ", "")
    try:
        return float(cleaned)
    except ValueError:
        return None


def main() -> None:
    service = AgriDataService()
    entries = service.oilseeds.get_prices(memberStateCodes="IT")
    prices = []
    for entry in entries:
        price = _parse_price(entry.get("price"))
        if price is not None:
            prices.append(price)
    if not prices:
        print("No price data returned.")
        return
    avg = mean(prices)
    print(f"Average price based on {len(prices)} records: {avg:.2f}")
    print("First 5 prices:", prices[:5])


if __name__ == "__main__":
    main()
