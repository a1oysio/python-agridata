from ..enums import CATEGORY_SERVICES
from .base import BaseAPI, create_api_class

__all__ = ["BaseAPI"]

# Dynamically generate API classes based on the declared categories
for _category, _services in CATEGORY_SERVICES.items():
    _cls = create_api_class(_category, _services)
    globals()[_cls.__name__] = _cls
    __all__.append(_cls.__name__)
