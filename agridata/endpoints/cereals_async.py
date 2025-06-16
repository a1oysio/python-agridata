from ..client import AsyncAgriDataClient
from ..enums import CEREAL_SERVICES
from .base import BaseAPI


class CerealsAPI(BaseAPI):
    SERVICES = CEREAL_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

    async def get_prices(self, **kwargs):
        self._validate_service("prices")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get("cereal", "prices", params)

    async def get_production(self, **kwargs):
        self._validate_service("production")
        params = {k: v for k, v in kwargs.items() if v is not None}
        return await self.client._get("cereal", "production", params)
