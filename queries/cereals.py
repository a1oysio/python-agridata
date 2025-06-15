from . import BaseQuery
from ..enums import COMMON_PARAMS

class CerealPricesQuery(BaseQuery):
    VALID_PARAMS = COMMON_PARAMS.keys()

class CerealProductionQuery(BaseQuery):
    VALID_PARAMS = COMMON_PARAMS.keys()
