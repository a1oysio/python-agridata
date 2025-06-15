# endpoints/meat.py
from ..client import AgriDataClient
from ..enums import MEAT_SERVICES
from ..queries.meat import MeatPricesQuery
from ..models.meat import MeatPricesResponse
from .base import BaseAPI


class MeatAPI(BaseAPI):
    SERVICES = MEAT_SERVICES

    def __init__(self, client: AgriDataClient):
        super().__init__(client)

    def get_prices(self, **kwargs) -> MeatPricesResponse:
        self._validate_service("prices")
        query = MeatPricesQuery(**kwargs)
        data = self.client._get("meat", "prices", query.dict())
        return MeatPricesResponse.from_api(data)

    async def get_prices_async(self, **kwargs) -> MeatPricesResponse:
        self._validate_service("prices")
        query = MeatPricesQuery(**kwargs)
        data = await self.client._get("meat", "prices", query.dict())
        return MeatPricesResponse.from_api(data)
