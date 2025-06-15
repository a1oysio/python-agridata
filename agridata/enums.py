from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple

HOST_URL = "https://ec.europa.eu/agrifood/api/{CATEGORY}/{SERVICE}"

@dataclass(frozen=True)
class CategoryInfo:
    """Information about an API category and its available services."""

    name: str
    services: Tuple[str, ...]

class ApiCategory(Enum):
    BEEF = CategoryInfo(
        "beef",
        (
            "prices",
            "categories",
            "productCodes",
            "production",
            "production/categories",
        ),
    )
    LIVE_ANIMAL = CategoryInfo(
        "liveAnimal",
        (
            "prices",
            "categories",
        ),
    )
    PIGMEAT = CategoryInfo(
        "pigmeat",
        (
            "prices",
            "cuts/prices",
            "cuts/categories",
            "cuts/priceTypes",
            "cuts/prices/month",
            "cuts/prices/month/categories",
            "cuts/prices/month/priceTypes",
            "production",
        ),
    )
    POULTRY = CategoryInfo(
        "poultry",
        (
            "prices",
            "priceTypes",
            "prices/month",
            "prices/month/priceTypes",
            "egg/prices",
            "egg/farmingMethods",
            "production",
            "production/animals",
        ),
    )
    SHEEP_AND_GOAT = CategoryInfo(
        "sheepAndGoat",
        (
            "prices",
            "categories",
            "markets",
            "production",
            "production/meats",
            "production/items",
        ),
    )
    RAW_MILK = CategoryInfo(
        "rawMilk",
        (
            "prices",
            "products",
        ),
    )
    DAIRY = CategoryInfo(
        "dairy",
        (
            "prices",
            "products",
            "production",
            "production/categories",
        ),
    )
    CEREAL = CategoryInfo(
        "cereal",
        (
            "prices",
            "products",
            "stages",
            "markets",
            "production",
            "production/crops",
        ),
    )
    RICE = CategoryInfo(
        "rice",
        (
            "prices",
            "stages",
            "types",
            "varieties",
            "memberStates",
            "production",
            "production/types",
            "production/products",
        ),
    )
    OILSEED = CategoryInfo(
        "oilseed",
        (
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
        ),
    )
    SUGAR = CategoryInfo(
        "sugar",
        (
            "prices",
            "regions",
            "production",
            "production/regions",
        ),
    )
    OLIVE_OIL = CategoryInfo(
        "oliveOil",
        (
            "prices",
            "products",
            "markets",
            "memberStates",
            "production",
        ),
    )
    WINE = CategoryInfo(
        "wine",
        (
            "prices",
            "descriptions",
        ),
    )
    TAXUD = CategoryInfo(
        "taxud",
        (
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
        ),
    )
    CMEF_INDICATORS = CategoryInfo(
        "cmefIndicators",
        (
            "values",
            "types",
            "categories",
            "indicators",
            "subIndicators",
            "parameters",
            "units",
            "codes",
            "sources",
        ),
    )
    FERTILISER = CategoryInfo(
        "fertiliser",
        (
            "prices",
            "prices/products",
        ),
    )
    ORGANIC = CategoryInfo(
        "organic",
        (
            "prices",
            "sectors",
            "organicProducts",
            "overallProducts",
        ),
    )


def get_categories() -> List[str]:
    """Return all category names used by the API."""

    return [c.value.name for c in ApiCategory]


# Backwards compatible constants
CATEGORIES = get_categories()

BEEF_SERVICES = ApiCategory.BEEF.value.services
LIVE_ANIMAL_SERVICES = ApiCategory.LIVE_ANIMAL.value.services
PIGMEAT_SERVICES = ApiCategory.PIGMEAT.value.services
EGGS_POULTRY_SERVICES = ApiCategory.POULTRY.value.services
SHEEP_GOAT_SERVICES = ApiCategory.SHEEP_AND_GOAT.value.services
MILK_SERVICES = ApiCategory.RAW_MILK.value.services
DAIRY_SERVICES = ApiCategory.DAIRY.value.services
CEREAL_SERVICES = ApiCategory.CEREAL.value.services
RICE_SERVICES = ApiCategory.RICE.value.services
OILSEED_SERVICES = ApiCategory.OILSEED.value.services
SUGAR_SERVICES = ApiCategory.SUGAR.value.services
OLIVE_OIL_SERVICES = ApiCategory.OLIVE_OIL.value.services
WINE_SERVICES = ApiCategory.WINE.value.services
TAXUD_SERVICES = ApiCategory.TAXUD.value.services
CMEF_INDICATORS_SERVICES = ApiCategory.CMEF_INDICATORS.value.services
FERTILISER_SERVICES = ApiCategory.FERTILISER.value.services
ORGANIC_SERVICES = ApiCategory.ORGANIC.value.services
