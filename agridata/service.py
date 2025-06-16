# service.py
from .client import AgriDataClient
from . import api
from .api import _to_class_name
from .enums import CATEGORY_SERVICES


class AgriDataService:
    def __init__(self):
        client = AgriDataClient()

        def _to_attr(category: str) -> str:
            import re

            return re.sub(r"(?<!^)(?=[A-Z])", "_", category).lower()

        for _category in CATEGORY_SERVICES.keys():
            _cls_name = _to_class_name(_category)
            _cls = getattr(api, _cls_name)
            setattr(self, _to_attr(_category), _cls(client))


