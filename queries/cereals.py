from dataclasses import dataclass, fields
from datetime import datetime
from typing import Optional

from . import BaseQuery
from ..enums import COMMON_PARAMS


@dataclass
class CerealPricesParams:
    """Allowed parameters for the cereal prices endpoint."""

    memberStateCodes: Optional[str] = None
    categories: Optional[str] = None
    productCodes: Optional[str] = None
    marketingYears: Optional[str] = None
    weeks: Optional[str] = None
    months: Optional[str] = None
    beginDate: Optional[datetime] = None
    endDate: Optional[datetime] = None

class CerealPricesQuery(BaseQuery):
    VALID_PARAMS = {f.name for f in fields(CerealPricesParams)}

    def __init__(self, **params):
        super().__init__(**params)
        # instantiate to leverage dataclass type checking
        self.params_obj = CerealPricesParams(**params)

class CerealProductionQuery(BaseQuery):
    VALID_PARAMS = COMMON_PARAMS.keys()
