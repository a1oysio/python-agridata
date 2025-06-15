from dataclasses import dataclass, fields
from datetime import datetime
from typing import Optional

from . import BaseQuery


@dataclass
class MeatPricesParams:
    """Allowed parameters for the meat prices endpoint."""

    memberStateCodes: Optional[str] = None
    categories: Optional[str] = None
    productCodes: Optional[str] = None
    marketingYears: Optional[str] = None
    weeks: Optional[str] = None
    months: Optional[str] = None
    beginDate: Optional[datetime] = None
    endDate: Optional[datetime] = None


class MeatPricesQuery(BaseQuery):
    VALID_PARAMS = {f.name for f in fields(MeatPricesParams)}

    def __init__(self, **params):
        super().__init__(**params)
        self.params_obj = MeatPricesParams(**params)
