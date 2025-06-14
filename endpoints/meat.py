
# endpoints/meat.py
from ..client import AgriDataClient
from ..queries.meat import MeatPricesQuery
from ..models.meat import MeatPricesResponse

class MeatAPI:
    def __init__(self, client: AgriDataClient):
        self.client = client

    def get_prices(self, **kwargs) -> MeatPricesResponse:
        query = MeatPricesQuery(**kwargs)
        data = self.client._get("meat", "prices", query.dict())
        return MeatPricesResponse(**data)
