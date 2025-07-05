from .enums import CATEGORY_SERVICES


class BaseAPI:
    SERVICES = None

    def __init__(self, client):
        self.client = client

    def _validate_service(self, service: str):
        if self.SERVICES is not None and service not in self.SERVICES:
            raise ValueError(f"Service '{service}' not supported")


def _to_class_name(category: str) -> str:
    """Return a CamelCase class name for a category."""
    import re

    # Insert spaces before capitals, then split on
    # spaces, hyphens or underscores
    tmp = re.sub("([A-Z])", r" \1", category)
    parts = re.split(r"[\s_-]+", tmp)
    return "".join(p.capitalize() for p in parts if p) + "API"


def create_api_class(category: str, services: list):
    """Return a ``BaseAPI`` subclass for *category* and *services*."""

    class_name = _to_class_name(category)
    attrs = {"SERVICES": services}

    for _service in services:
        _name = _service.replace("/", "_")

        def _sync(self, _svc=_service, **kwargs):
            self._validate_service(_svc)
            params = {k: v for k, v in kwargs.items() if v is not None}
            return self.client._get(category, _svc, params)

        attrs[f"get_{_name}"] = _sync

    return type(class_name, (BaseAPI,), attrs)


__all__ = ["BaseAPI"]

for _category, _services in CATEGORY_SERVICES.items():
    _cls = create_api_class(_category, _services)
    globals()[_cls.__name__] = _cls
    __all__.append(_cls.__name__)
