import agridata.api as api
from agridata.enums import CATEGORY_SERVICES


def test_api_methods_exist():
    for category, services in CATEGORY_SERVICES.items():
        class_name = api._to_class_name(category)
        cls = getattr(api, class_name)
        obj = cls(client=None)
        for service in services:
            method = f"get_{service.replace('/', '_')}"
            assert hasattr(obj, method)
