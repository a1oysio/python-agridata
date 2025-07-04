from agridata.service import AgriDataService
from agridata.enums import CATEGORY_SERVICES


def main():
    # Display available services for the 'cereal' category
    cereal_services = CATEGORY_SERVICES.get("cereal")
    print("Cereal services:", cereal_services)

    # Create the service instance
    service = AgriDataService()

    # Retrieve all cereal products
    products = service.cereal.get_products()
    print("Cereal products:", products)

    # Example of filtering by parameters when retrieving prices
    prices = service.cereal.get_prices(memberStateCodes="IT")
    print("Italian cereal prices for 2024:", prices)

    # Another request with different parameters
    production = service.cereal.get_production(
        memberStateCodes="FR", marketingYears="2023"
    )
    print("French cereal production in 2023:", production)

    l1 = service.cereal.get_production_crops()
    l2 = service.cereal.get_products()
    print(l1, l2)


if __name__ == "__main__":
    main()
