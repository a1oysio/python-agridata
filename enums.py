from datetime import datetime
import requests

HOST_URL = "https://ec.europa.eu/agrifood/api/{CATEGORY}/{SERVICE}"



CEREAL_SERVCES = ["prices", "products", "stages", "markets", "production", "production/crops"]


params = {
    "memberStateCodes": str,
    "categories": str,
    "productCodes": str,
    "years": str, 
    "weeks": str,
    "months": str, 
    "beginDate": datetime,
    "endDate": datetime,
}
