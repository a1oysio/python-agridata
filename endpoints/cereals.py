
# endpoints/cereals.py
from ..client import AgriDataClient
from ..enums import CEREAL_SERVICES
from ..queries.cereals import CerealPricesQuery, CerealProductionQuery
from ..models.cereals import CerealPricesResponse, CerealProductionResponse
from .base import BaseAPI

class CerealsAPI(BaseAPI):
    SERVICES = CEREAL_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)

    def get_prices(self, **kwargs) -> CerealPricesResponse:
        self._validate_service("prices")
        query = CerealPricesQuery(**kwargs)
        data = self.client._get("cereal", "prices", query.dict())
        return CerealPricesResponse(**data)

    async def get_prices_async(self, **kwargs) -> CerealPricesResponse:
        self._validate_service("prices")
        query = CerealPricesQuery(**kwargs)
        data = await self.client._get("cereal", "prices", query.dict())
        return CerealPricesResponse(**data)

    def get_production(self, **kwargs) -> CerealProductionResponse:
        self._validate_service("production")
        query = CerealProductionQuery(**kwargs)
        data = self.client._get("cereal", "production", query.dict())
        return CerealProductionResponse(**data)

    async def get_production_async(self, **kwargs) -> CerealProductionResponse:
        self._validate_service("production")
        query = CerealProductionQuery(**kwargs)
        data = await self.client._get("cereal", "production", query.dict())
        return CerealProductionResponse(**data)
