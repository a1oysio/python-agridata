
# service.py
from .client import AgriDataClient, AsyncAgriDataClient
from .endpoints.cereals import CerealsAPI
from .endpoints.meat    import MeatAPI
# ...

class AgriDataService:
    def __init__(self, api_key: str):
        client = AgriDataClient(api_key)
        self.cereals = CerealsAPI(client)
        self.meat    = MeatAPI(client)
        # dairy, fruitveg, etc.


class AgriDataAsyncService:
    """Asynchronous service exposing API endpoints."""

    def __init__(self, api_key: str):
        client = AsyncAgriDataClient(api_key)
        self.client = client
        self.cereals = CerealsAPI(client)
        self.meat = MeatAPI(client)
        # dairy, fruitveg, etc.

    async def aclose(self):
        await self.client.aclose()
