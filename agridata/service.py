# service.py
from .client import AgriDataClient
from . import endpoints
from .endpoints.base import _to_class_name
from .enums import CATEGORY_SERVICES


class AgriDataService:
    def __init__(self):
        client = AgriDataClient()

        def _to_attr(category: str) -> str:
            import re

            return re.sub(r"(?<!^)(?=[A-Z])", "_", category).lower()

        for _category in CATEGORY_SERVICES.keys():
            _cls_name = _to_class_name(_category)
            _cls = getattr(endpoints, _cls_name)
            setattr(self, _to_attr(_category), _cls(client))


