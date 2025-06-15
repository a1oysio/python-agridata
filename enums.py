from datetime import datetime

HOST_URL = "https://ec.europa.eu/agrifood/api/{CATEGORY}/{SERVICE}"

CATEGORIES = [
    "beef",
    "liveAnimal",
    "pigmeat",
    "poultry",
    "sheepAndGoat",
    "rawMilk",
    "dairy",
    "rice",
    "oilseed",
    "sugar",
    "oliveOil",
    "wine",
    "taxud",
    "cmefIndicators",
    "fertiliser",
    "organic"
    ]

BEEF_SERVICES = [
    "prices",
    "categories",
    "productCodes",
    "production"
    "production/categories"
    ]

LIVE_ANIMAL_SERVICES = [
    "prices",
    "categories",
    ]

PIGMEAT_SERVICES = [
    "prices",
    "cuts/prices",
    "cuts/categories",
    "cuts/priceTypes",
    "cuts/prices/month",
    "cuts/prices/month/categories",
    "cuts/prices/month/priceTypes",
    "production"
    ]

EGGS_POULTRY_SERVICES = [
    "prices",
    "priceTypes",
    "prices/month",
    "prices/month/priceTypes",
    "egg/prices"
    "egg/farmingMethods",
    "production",
    "production/animals",
    ]

SHEEP_GOAT_SERVICES = [
    "prices",
    "categories",
    "markets",
    "production",
    "production/meats",
    "production/items"
    ]

MILK_SERVICES = [
    "prices",
    "products",
        ]

DAIRY_SERVICES = [
    "prices",
    "products",
    "production",
    "production/categories"
    ]


CEREAL_SERVICES = [
    "prices",
    "products",
    "stages",
    "markets",
    "production",
    "production/crops",
    ]

RICE_SERVICES = [
    "prices",
    "stages",
    "types",
    "varieties",
    "memberStates",
    "production",
    "production/types",
    "production/products"
    ]

OILSEED_SERVICES = [
    "prices",
    "products"
    "productTypes",
    "markets",
    "marketStages"
    "production"
    "production/crops",
    "crops/prices"
    "crops/products"
    "crops/productTypes",
    "crops/marketStages"
    ]

SUGAR_SERVICES = [
    "prices",
    "regions",
    "production"
    "production/regions"
    ]

OLIVE_OIL_SERVICES = [
    "prices",
    "products"
    "markets",
    "memberStates",
    "production",
    ]

WINE_SERVICES = [
    "prices",
    "descriptions",
    ]

TAXUD_SERVICES = [
    "weeklyData/import",
    "weeklyData/sectors",
    "weeklyData/importCategories",
    "weeklyData/import/cn8ProductCodes",
    "weeklyData/import/taric10ProductCodes",
    "weeklyData/import/products",
    "weeklyData/export",
    "weeklyData/export/cn8ProductCodes",
    "weeklyData/export/taric10ProductCodes",
    "weeklyData/export/products"

    ]

CMEF_INDICATORS_SERVICES = [
    "values",
    "types",
    "categories",
    "indicators",
    "subIndicators",
    "parameters",
    "units",
    "codes",
    "sources",
    ]

FERTILISER_SERVICES = [
    "prices",
    "prices/products",
    ]

ORGANIC_SERVICES = [
    "prices",
    "sectors",
    "organicProducts",
    "overallProducts",
    ]


