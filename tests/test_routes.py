from agridata.service import AgriDataService
from agridata.config import API_BASE_URL


class DummyResponse:
    def __init__(self, data=None):
        self._data = data or []

    def raise_for_status(self):
        pass

    def json(self):
        return self._data


def test_cereal_prices_route(monkeypatch):
    service = AgriDataService()
    captured = {}

    def mock_get(url, params=None, timeout=None):
        captured["url"] = url
        captured["params"] = params
        return DummyResponse([])
    monkeypatch.setattr(service.cereal.client.session, "get", mock_get)
    service.cereal.get_prices(memberStateCodes="IT")
    assert captured["url"] == f"{API_BASE_URL}/cereal/prices"
    assert captured["params"] == {"memberStateCodes": "IT"}


def test_dairy_prices_route(monkeypatch):
    service = AgriDataService()
    captured = {}

    def mock_get(url, params=None, timeout=None):
        captured["url"] = url
        captured["params"] = params
        return DummyResponse([])
    monkeypatch.setattr(service.dairy.client.session, "get", mock_get)
    service.dairy.get_prices()
    assert captured["url"] == f"{API_BASE_URL}/dairy/prices"
    assert captured["params"] == {}


def test_oilseeds_prices_route(monkeypatch):
    service = AgriDataService()
    captured = {}

    def mock_get(url, params=None, timeout=None):
        captured["url"] = url
        captured["params"] = params
        return DummyResponse([])

    monkeypatch.setattr(service.oilseeds.client.session, "get", mock_get)
    service.oilseeds.get_prices(products="rapeseed")
    assert captured["url"] == f"{API_BASE_URL}/oilseeds/prices"
    assert captured["params"] == {"products": "rapeseed"}
