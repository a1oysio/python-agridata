
from dataclasses import dataclass, fields
from datetime import datetime
from typing import Optional

from . import BaseQuery

@dataclass
class BeefPricesParams:
    """Allowed parameters for the beef prices endpoint."""
    memberStateCodes: Optional[str] = None
    categories: Optional[str] = None
    productCodes: Optional[str] = None
    years: Optional[str] = None
    weeks: Optional[str] = None
    months: Optional[str] = None
    beginDate: Optional[datetime] = None
    endDate: Optional[datetime] = None

class BeefPricesQuery(BaseQuery):
    """Query builder for the beef prices endpoint."""
    VALID_PARAMS = {f.name for f in fields(BeefPricesParams)}

    def __init__(self, **params):
        super().__init__(**params)
        # Instantiate to leverage dataclass type checking
        self.params_obj = BeefPricesParams(**params)

class BeefCategoriesQuery(BaseQuery):
    """Query builder for the beef categories endpoint (no parameters)."""
    VALID_PARAMS = set()

    def __init__(self):
        super().__init__()
        # No parameters to validate

class BeefProductCodesQuery(BaseQuery):
    """Query builder for the beef product codes endpoint (no parameters)."""
    VALID_PARAMS = set()

    def __init__(self):
        super().__init__()
        # No parameters to validate

@dataclass
class BeefProductionParams:
    """Allowed parameters for the beef production endpoint."""
    memberStateCodes: Optional[str] = None
    categories: Optional[str] = None
    years: Optional[str] = None
    months: Optional[str] = None

class BeefProductionQuery(BaseQuery):
    """Query builder for the beef production endpoint."""
    VALID_PARAMS = {f.name for f in fields(BeefProductionParams)}

    def __init__(self, **params):
        super().__init__(**params)
        # Instantiate to leverage dataclass type checking
        self.params_obj = BeefProductionParams(**params)

class BeefProductionCategoriesQuery(BaseQuery):
    """Query builder for the beef production categories endpoint (no parameters)."""
    VALID_PARAMS = set()

    def __init__(self):
        super().__init__()
        # No parameters to validate
