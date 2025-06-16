from ..client import AsyncAgriDataClient
from ..enums import BEEF_SERVICES
from .base import BaseAPI


class BeefAPI(BaseAPI):
    SERVICES = BEEF_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

    async def get_prices(self, **kwargs):
        self._validate_service("prices")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get("beef", "prices", params)

    async def get_categories(self):
        self._validate_service("categories")
        return await self.client._get("beef", "categories", {})

    async def get_productCodes(self):
        self._validate_service("productCodes")
        return await self.client._get("beef", "productCodes", {})

    async def get_production(self, **kwargs):
        self._validate_service("production")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get("beef", "production", params)

    async def get_production_categories(self):
        self._validate_service("production/categories")
        return await self.client._get("beef", "production/categories", {})
