from dataclasses import dataclass
from typing import List


@dataclass
class CerealPrice:
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
class CerealPricesResponse:
    prices: List[CerealPrice]

    @classmethod
    def from_api(cls, data: List[dict]) -> "CerealPricesResponse":
        prices = [CerealPrice(**item) for item in data]
        return cls(prices=prices)


@dataclass
class CerealProductionResponse:
    data: List[dict]

    @classmethod
    def from_api(cls, data: List[dict]) -> "CerealProductionResponse":
        return cls(data=data)
