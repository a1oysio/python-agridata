from dataclasses import dataclass
from typing import List, Optional

@dataclass
class BeefPrice:
    memberStateCode: str
    memberStateName: str
    beginDate: str
    endDate: str
    weekNumber: int
    unit: str
    price: str
    category: str
    productCode: str

@dataclass
class BeefPricesResponse:
    prices: List[BeefPrice]

    @classmethod
    def from_api(cls, data: List[dict]) -> "BeefPricesResponse":
        prices = [BeefPrice(**item) for item in data]
        return cls(prices=prices)

@dataclass
class BeefCategoryResponse:
    categories: List[str]

    @classmethod
    def from_api(cls, data: List[str]) -> "BeefCategoryResponse":
        return cls(categories=data)

@dataclass
class BeefProductCodesResponse:
    productCodes: List[str]

    @classmethod
    def from_api(cls, data: List[str]) -> "BeefProductCodesResponse":
        return cls(productCodes=data)

@dataclass
class BeefProduction:
    memberStateCode: str
    memberStateName: str
    year: int
    month: str
    category: str
    tonnes: float
    heads: float
    kgPerHead: float

@dataclass
class BeefProductionResponse:
    productions: List[BeefProduction]

    @classmethod
    def from_api(cls, data: List[dict]) -> "BeefProductionResponse":
        prods = [BeefProduction(**item) for item in data]
        return cls(productions=prods)

@dataclass
class BeefProductionCategoriesResponse:
    categories: List[str]

    @classmethod
    def from_api(cls, data: List[str]) -> "BeefProductionCategoriesResponse":
        return cls(categories=data)
