# service.py
from .client import AgriDataClient, AsyncAgriDataClient
from .endpoints.cereals import CerealsAPI as SyncCerealsAPI
from .endpoints.beef import BeefAPI as SyncBeefAPI
from .endpoints.live_animal import LiveAnimalAPI as SyncLiveAnimalAPI
from .endpoints.pigmeat import PigmeatAPI as SyncPigmeatAPI
from .endpoints.poultry import PoultryAPI as SyncPoultryAPI
from .endpoints.sheep_and_goat import SheepAndGoatAPI as SyncSheepAndGoatAPI
from .endpoints.raw_milk import RawMilkAPI as SyncRawMilkAPI
from .endpoints.dairy import DairyAPI as SyncDairyAPI
from .endpoints.rice import RiceAPI as SyncRiceAPI
from .endpoints.oilseed import OilseedAPI as SyncOilseedAPI
from .endpoints.sugar import SugarAPI as SyncSugarAPI
from .endpoints.olive_oil import OliveOilAPI as SyncOliveOilAPI
from .endpoints.wine import WineAPI as SyncWineAPI
from .endpoints.taxud import TaxudAPI as SyncTaxudAPI
from .endpoints.cmef_indicators import CmefIndicatorsAPI as SyncCmefIndicatorsAPI
from .endpoints.fertiliser import FertiliserAPI as SyncFertiliserAPI
from .endpoints.organic import OrganicAPI as SyncOrganicAPI
from .endpoints.cereals_async import CerealsAPI as AsyncCerealsAPI
from .endpoints.beef_async import BeefAPI as AsyncBeefAPI
from .endpoints.live_animal_async import LiveAnimalAPI as AsyncLiveAnimalAPI
from .endpoints.pigmeat_async import PigmeatAPI as AsyncPigmeatAPI
from .endpoints.poultry_async import PoultryAPI as AsyncPoultryAPI
from .endpoints.sheep_and_goat_async import SheepAndGoatAPI as AsyncSheepAndGoatAPI
from .endpoints.raw_milk_async import RawMilkAPI as AsyncRawMilkAPI
from .endpoints.dairy_async import DairyAPI as AsyncDairyAPI
from .endpoints.rice_async import RiceAPI as AsyncRiceAPI
from .endpoints.oilseed_async import OilseedAPI as AsyncOilseedAPI
from .endpoints.sugar_async import SugarAPI as AsyncSugarAPI
from .endpoints.olive_oil_async import OliveOilAPI as AsyncOliveOilAPI
from .endpoints.wine_async import WineAPI as AsyncWineAPI
from .endpoints.taxud_async import TaxudAPI as AsyncTaxudAPI
from .endpoints.cmef_indicators_async import CmefIndicatorsAPI as AsyncCmefIndicatorsAPI
from .endpoints.fertiliser_async import FertiliserAPI as AsyncFertiliserAPI
from .endpoints.organic_async import OrganicAPI as AsyncOrganicAPI


class AgriDataService:
    def __init__(self, api_key: str):
        client = AgriDataClient(api_key)
        self.cereals = SyncCerealsAPI(client)
        self.beef = SyncBeefAPI(client)
        self.live_animal = SyncLiveAnimalAPI(client)
        self.pigmeat = SyncPigmeatAPI(client)
        self.poultry = SyncPoultryAPI(client)
        self.sheep_and_goat = SyncSheepAndGoatAPI(client)
        self.raw_milk = SyncRawMilkAPI(client)
        self.dairy = SyncDairyAPI(client)
        self.rice = SyncRiceAPI(client)
        self.oilseed = SyncOilseedAPI(client)
        self.sugar = SyncSugarAPI(client)
        self.olive_oil = SyncOliveOilAPI(client)
        self.wine = SyncWineAPI(client)
        self.taxud = SyncTaxudAPI(client)
        self.cmef_indicators = SyncCmefIndicatorsAPI(client)
        self.fertiliser = SyncFertiliserAPI(client)
        self.organic = SyncOrganicAPI(client)


class AgriDataAsyncService:
    """Asynchronous service exposing API endpoints."""

    def __init__(self, api_key: str):
        client = AsyncAgriDataClient(api_key)
        self.client = client
        self.cereals = AsyncCerealsAPI(client)
        self.beef = AsyncBeefAPI(client)
        self.live_animal = AsyncLiveAnimalAPI(client)
        self.pigmeat = AsyncPigmeatAPI(client)
        self.poultry = AsyncPoultryAPI(client)
        self.sheep_and_goat = AsyncSheepAndGoatAPI(client)
        self.raw_milk = AsyncRawMilkAPI(client)
        self.dairy = AsyncDairyAPI(client)
        self.rice = AsyncRiceAPI(client)
        self.oilseed = AsyncOilseedAPI(client)
        self.sugar = AsyncSugarAPI(client)
        self.olive_oil = AsyncOliveOilAPI(client)
        self.wine = AsyncWineAPI(client)
        self.taxud = AsyncTaxudAPI(client)
        self.cmef_indicators = AsyncCmefIndicatorsAPI(client)
        self.fertiliser = AsyncFertiliserAPI(client)
        self.organic = AsyncOrganicAPI(client)

    async def aclose(self):
        await self.client.aclose()
