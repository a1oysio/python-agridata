from datetime import datetime

HOST_URL = "https://ec.europa.eu/agrifood/api/{CATEGORY}/{SERVICE}"



CEREAL_SERVICES = [
    "prices",
    "products",
    "stages",
    "markets",
    "production",
    "production/crops",
]

MEAT_SERVICES = ["prices"]


COMMON_PARAMS = {
    "memberStateCodes": str,
    "categories": str,
    "productCodes": str,
    "years": str,
    "weeks": str,
    "months": str,
    "beginDate": datetime,
    "endDate": datetime,
}
