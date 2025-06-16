# service.py
from .client import AgriDataClient
from .endpoints import (
    BeefAPI as SyncBeefAPI,
    CerealsAPI as SyncCerealsAPI,
    LiveAnimalAPI as SyncLiveAnimalAPI,
    PigmeatAPI as SyncPigmeatAPI,
    PoultryAPI as SyncPoultryAPI,
    SheepAndGoatAPI as SyncSheepAndGoatAPI,
    RawMilkAPI as SyncRawMilkAPI,
    DairyAPI as SyncDairyAPI,
    RiceAPI as SyncRiceAPI,
    OilseedAPI as SyncOilseedAPI,
    SugarAPI as SyncSugarAPI,
    OliveOilAPI as SyncOliveOilAPI,
    WineAPI as SyncWineAPI,
    TaxudAPI as SyncTaxudAPI,
    CmefIndicatorsAPI as SyncCmefIndicatorsAPI,
    FertiliserAPI as SyncFertiliserAPI,
    OrganicAPI as SyncOrganicAPI,
)


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


