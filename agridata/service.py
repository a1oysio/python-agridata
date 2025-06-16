# service.py
from .client import AgriDataClient
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


class AgriDataService:
    def __init__(self):
        client = AgriDataClient()
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


