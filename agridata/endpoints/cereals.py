# endpoints/cereals.py
from ..client import AgriDataClient
from ..enums import CEREAL_SERVICES
from .base import BaseAPI


class CerealsAPI(BaseAPI):
    SERVICES = CEREAL_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)

    def get_prices(self, **kwargs):
        self._validate_service("prices")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return self.client._get("cereal", "prices", params)

    async def get_prices_async(self, **kwargs):
        self._validate_service("prices")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get("cereal", "prices", params)

    def get_production(self, **kwargs):
        self._validate_service("production")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return self.client._get("cereal", "production", params)

    async def get_production_async(self, **kwargs):
        self._validate_service("production")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get("cereal", "production", params)
