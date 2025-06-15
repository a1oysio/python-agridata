from ..client import AgriDataClient
from ..enums import BEEF_SERVICES
from ..queries.beef import (
    BeefPricesQuery,
    BeefCategoriesQuery,
    BeefProductCodesQuery,
    BeefProductionQuery,
    BeefProductionCategoriesQuery,
)
from ..models.beef import (
    BeefPricesResponse,
    BeefCategoryResponse,
    BeefProductCodesResponse,
    BeefProductionResponse,
    BeefProductionCategoriesResponse,
)
from .base import BaseAPI


class BeefAPI(BaseAPI):
    SERVICES = BEEF_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)

    def get_prices(self, **kwargs) -> BeefPricesResponse:
        self._validate_service("prices")
        query = BeefPricesQuery(**kwargs)
        data = self.client._get("beef", "prices", query.dict())
        return BeefPricesResponse.from_api(data)

    async def get_prices_async(self, **kwargs) -> BeefPricesResponse:
        self._validate_service("prices")
        query = BeefPricesQuery(**kwargs)
        data = await self.client._get("beef", "prices", query.dict())
        return BeefPricesResponse.from_api(data)

    def get_categories(self) -> BeefCategoryResponse:
        self._validate_service("categories")
        query = BeefCategoriesQuery()
        data = self.client._get("beef", "categories", query.dict())
        return BeefCategoryResponse.from_api(data)

    async def get_categories_async(self) -> BeefCategoryResponse:
        self._validate_service("categories")
        query = BeefCategoriesQuery()
        data = await self.client._get("beef", "categories", query.dict())
        return BeefCategoryResponse.from_api(data)

    def get_productCodes(self) -> BeefProductCodesResponse:
        self._validate_service("productCodes")
        query = BeefProductCodesQuery()
        data = self.client._get("beef", "productCodes", query.dict())
        return BeefProductCodesResponse.from_api(data)

    async def get_productCodes_async(self) -> BeefProductCodesResponse:
        self._validate_service("productCodes")
        query = BeefProductCodesQuery()
        data = await self.client._get("beef", "productCodes", query.dict())
        return BeefProductCodesResponse.from_api(data)

    def get_production(self, **kwargs) -> BeefProductionResponse:
        self._validate_service("production")
        query = BeefProductionQuery(**kwargs)
        data = self.client._get("beef", "production", query.dict())
        return BeefProductionResponse.from_api(data)

    async def get_production_async(self, **kwargs) -> BeefProductionResponse:
        self._validate_service("production")
        query = BeefProductionQuery(**kwargs)
        data = await self.client._get("beef", "production", query.dict())
        return BeefProductionResponse.from_api(data)

    def get_production_categories(self) -> BeefProductionCategoriesResponse:
        self._validate_service("production/categories")
        query = BeefProductionCategoriesQuery()
        data = self.client._get("beef", "production/categories", query.dict())
        return BeefProductionCategoriesResponse.from_api(data)

    async def get_production_categories_async(self) -> BeefProductionCategoriesResponse:
        self._validate_service("production/categories")
        query = BeefProductionCategoriesQuery()
        data = await self.client._get("beef", "production/categories", query.dict())
        return BeefProductionCategoriesResponse.from_api(data)
