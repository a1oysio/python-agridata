from typing import List

HOST_URL = "https://ec.europa.eu/agrifood/api/{CATEGORY}/{SERVICE}"

CATEGORY_SERVICES = {
    "beef": [
        "prices",
        "categories",
        "productCodes",
        "production",
        "production/categories",
    ],
    "liveAnimal": [
        "prices",
        "categories",
    ],
    "pigmeat": [
        "prices",
        "cuts/prices",
        "cuts/categories",
        "cuts/priceTypes",
        "cuts/prices/month",
        "cuts/prices/month/categories",
        "cuts/prices/month/priceTypes",
        "production",
    ],
    "poultry": [
        "prices",
        "priceTypes",
        "prices/month",
        "prices/month/priceTypes",
        "egg/prices",
        "egg/farmingMethods",
        "production",
        "production/animals",
    ],
    "sheepAndGoat": [
        "prices",
        "categories",
        "markets",
        "production",
        "production/meats",
        "production/items",
    ],
    "rawMilk": [
        "prices",
        "products",
    ],
    "dairy": [
        "prices",
        "products",
        "production",
        "production/categories",
    ],
    "cereal": [
        "prices",
        "products",
        "stages",
        "markets",
        "production",
        "production/crops",
    ],
    "rice": [
        "prices",
        "stages",
        "types",
        "varieties",
        "memberStates",
        "production",
        "production/types",
        "production/products",
    ],
    "oilseeds": [
        "prices",
        "products",
        "productTypes",
        "markets",
        "marketStages",
        "production",
        "production/crops",
        "crops/prices",
        "crops/products",
        "crops/productTypes",
        "crops/marketStages",
    ],
    "sugar": [
        "prices",
        "regions",
        "production",
        "production/regions",
    ],
    "oliveOil": [
        "prices",
        "products",
        "markets",
        "memberStates",
        "production",
    ],
    "wine": [
        "prices",
        "descriptions",
    ],
    "taxud": [
        "weeklyData/import",
        "weeklyData/sectors",
        "weeklyData/importCategories",
        "weeklyData/import/cn8ProductCodes",
        "weeklyData/import/taric10ProductCodes",
        "weeklyData/import/products",
        "weeklyData/export",
        "weeklyData/export/cn8ProductCodes",
        "weeklyData/export/taric10ProductCodes",
        "weeklyData/export/products",
    ],
    "cmefIndicators": [
        "values",
        "types",
        "categories",
        "indicators",
        "subIndicators",
        "parameters",
        "units",
        "codes",
        "sources",
    ],
    "fertiliser": [
        "prices",
        "prices/products",
    ],
    "organic": [
        "prices",
        "sectors",
        "organicProducts",
        "overallProducts",
    ],
}


def get_categories() -> List[str]:
    """Return all category names used by the API."""

    return list(CATEGORY_SERVICES.keys())


# Backwards compatible constants
CATEGORIES = get_categories()

BEEF_SERVICES = CATEGORY_SERVICES["beef"]
LIVE_ANIMAL_SERVICES = CATEGORY_SERVICES["liveAnimal"]
PIGMEAT_SERVICES = CATEGORY_SERVICES["pigmeat"]
EGGS_POULTRY_SERVICES = CATEGORY_SERVICES["poultry"]
SHEEP_GOAT_SERVICES = CATEGORY_SERVICES["sheepAndGoat"]
MILK_SERVICES = CATEGORY_SERVICES["rawMilk"]
DAIRY_SERVICES = CATEGORY_SERVICES["dairy"]
CEREAL_SERVICES = CATEGORY_SERVICES["cereal"]
RICE_SERVICES = CATEGORY_SERVICES["rice"]
OILSEEDS_SERVICES = CATEGORY_SERVICES["oilseeds"]
SUGAR_SERVICES = CATEGORY_SERVICES["sugar"]
OLIVE_OIL_SERVICES = CATEGORY_SERVICES["oliveOil"]
WINE_SERVICES = CATEGORY_SERVICES["wine"]
TAXUD_SERVICES = CATEGORY_SERVICES["taxud"]
CMEF_INDICATORS_SERVICES = CATEGORY_SERVICES["cmefIndicators"]
FERTILISER_SERVICES = CATEGORY_SERVICES["fertiliser"]
ORGANIC_SERVICES = CATEGORY_SERVICES["organic"]
