from ..client import AsyncAgriDataClient
from ..enums import CEREAL_SERVICES
from ..queries.cereals import CerealPricesQuery, CerealProductionQuery
from ..models.cereals import CerealPricesResponse, CerealProductionResponse
from .base import BaseAPI


class CerealsAPI(BaseAPI):
    SERVICES = CEREAL_SERVICES

    def __init__(self, client: AsyncAgriDataClient):
        super().__init__(client)

    async def get_prices(self, **kwargs) -> CerealPricesResponse:
        self._validate_service("prices")
        query = CerealPricesQuery(**kwargs)
        data = await self.client._get("cereal", "prices", query.dict())
        return CerealPricesResponse.from_api(data)

    async def get_production(self, **kwargs) -> CerealProductionResponse:
        self._validate_service("production")
        query = CerealProductionQuery(**kwargs)
        data = await self.client._get("cereal", "production", query.dict())
        return CerealProductionResponse.from_api(data)
