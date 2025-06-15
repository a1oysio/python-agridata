# service.py
from .client import AgriDataClient, AsyncAgriDataClient
from .endpoints.cereals import CerealsAPI
from .endpoints.beef import BeefAPI
from .endpoints.live_animal import LiveAnimalAPI
from .endpoints.pigmeat import PigmeatAPI
from .endpoints.poultry import PoultryAPI
from .endpoints.sheep_and_goat import SheepAndGoatAPI
from .endpoints.raw_milk import RawMilkAPI
from .endpoints.dairy import DairyAPI
from .endpoints.rice import RiceAPI
from .endpoints.oilseed import OilseedAPI
from .endpoints.sugar import SugarAPI
from .endpoints.olive_oil import OliveOilAPI
from .endpoints.wine import WineAPI
from .endpoints.taxud import TaxudAPI
from .endpoints.cmef_indicators import CmefIndicatorsAPI
from .endpoints.fertiliser import FertiliserAPI
from .endpoints.organic import OrganicAPI


class AgriDataService:
    def __init__(self, api_key: str):
        client = AgriDataClient(api_key)
        self.cereals = CerealsAPI(client)
        self.beef = BeefAPI(client)
        self.live_animal = LiveAnimalAPI(client)
        self.pigmeat = PigmeatAPI(client)
        self.poultry = PoultryAPI(client)
        self.sheep_and_goat = SheepAndGoatAPI(client)
        self.raw_milk = RawMilkAPI(client)
        self.dairy = DairyAPI(client)
        self.rice = RiceAPI(client)
        self.oilseed = OilseedAPI(client)
        self.sugar = SugarAPI(client)
        self.olive_oil = OliveOilAPI(client)
        self.wine = WineAPI(client)
        self.taxud = TaxudAPI(client)
        self.cmef_indicators = CmefIndicatorsAPI(client)
        self.fertiliser = FertiliserAPI(client)
        self.organic = OrganicAPI(client)


class AgriDataAsyncService:
    """Asynchronous service exposing API endpoints."""

    def __init__(self, api_key: str):
        client = AsyncAgriDataClient(api_key)
        self.client = client
        self.cereals = CerealsAPI(client)
        self.beef = BeefAPI(client)
        self.live_animal = LiveAnimalAPI(client)
        self.pigmeat = PigmeatAPI(client)
        self.poultry = PoultryAPI(client)
        self.sheep_and_goat = SheepAndGoatAPI(client)
        self.raw_milk = RawMilkAPI(client)
        self.dairy = DairyAPI(client)
        self.rice = RiceAPI(client)
        self.oilseed = OilseedAPI(client)
        self.sugar = SugarAPI(client)
        self.olive_oil = OliveOilAPI(client)
        self.wine = WineAPI(client)
        self.taxud = TaxudAPI(client)
        self.cmef_indicators = CmefIndicatorsAPI(client)
        self.fertiliser = FertiliserAPI(client)
        self.organic = OrganicAPI(client)

    async def aclose(self):
        await self.client.aclose()
