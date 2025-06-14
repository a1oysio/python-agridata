
# service.py
from .client import AgriDataClient
from .endpoints.cereals import CerealsAPI
from .endpoints.meat    import MeatAPI
# ...

class AgriDataService:
    def __init__(self, api_key: str):
        client = AgriDataClient(api_key)
        self.cereals = CerealsAPI(client)
        self.meat    = MeatAPI(client)
        # dairy, fruitveg, etc.
