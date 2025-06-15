from dataclasses import dataclass
from typing import List


@dataclass
class MeatPrice:
    memberStateCode: str
    memberStateName: str
    beginDate: str
    endDate: str
    price: str
    unit: str
    weekNumber: int
    productName: str
    marketName: str
    stageName: str
    referencePeriod: str


@dataclass
class MeatPricesResponse:
    prices: List[MeatPrice]

    @classmethod
    def from_api(cls, data: List[dict]) -> "MeatPricesResponse":
        prices = [MeatPrice(**item) for item in data]
        return cls(prices=prices)
