from ..client import AgriDataClient
from ..enums import BEEF_SERVICES

from .base import BaseAPI


class BeefAPI(BaseAPI):
    SERVICES = BEEF_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)

    def get_prices(self, **kwargs):
        self._validate_service("prices")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return self.client._get("beef", "prices", params)

    async def get_prices_async(self, **kwargs):
        self._validate_service("prices")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get("beef", "prices", params)

    def get_categories(self):
        self._validate_service("categories")
        return self.client._get("beef", "categories", {})

    async def get_categories_async(self):
        self._validate_service("categories")
        return await self.client._get("beef", "categories", {})

    def get_productCodes(self):
        self._validate_service("productCodes")
        return self.client._get("beef", "productCodes", {})

    async def get_productCodes_async(self):
        self._validate_service("productCodes")
        return await self.client._get("beef", "productCodes", {})

    def get_production(self, **kwargs):
        self._validate_service("production")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return self.client._get("beef", "production", params)

    async def get_production_async(self, **kwargs):
        self._validate_service("production")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get("beef", "production", params)

    def get_production_categories(self):
        self._validate_service("production/categories")
        return self.client._get("beef", "production/categories", {})

    async def get_production_categories_async(self):
        self._validate_service("production/categories")
        return await self.client._get("beef", "production/categories", {})
