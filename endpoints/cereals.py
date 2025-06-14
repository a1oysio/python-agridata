
# endpoints/cereals.py
from ..client import AgriDataClient
from ..queries.cereals import CerealPricesQuery, CerealProductionQuery
from ..models.cereals import CerealPricesResponse, CerealProductionResponse

class CerealsAPI:
    def __init__(self, client: AgriDataClient):
        self.client = client

    def get_prices(self, **kwargs) -> CerealPricesResponse:
        query = CerealPricesQuery(**kwargs)
        data = self.client._get("cereal", "prices", query.dict())
        return CerealPricesResponse(**data)

    def get_production(self, **kwargs) -> CerealProductionResponse:
        query = CerealProductionQuery(**kwargs)
        data = self.client._get("cereal", "production", query.dict())
        return CerealProductionResponse(**data)
