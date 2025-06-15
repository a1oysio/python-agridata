from . import BaseQuery
from ..enums import COMMON_PARAMS

class MeatPricesQuery(BaseQuery):
    VALID_PARAMS = COMMON_PARAMS.keys()
