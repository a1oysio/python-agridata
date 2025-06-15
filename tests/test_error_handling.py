import os
import sys
import json
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agridata.service import AgriDataService
from agridata.exceptions import AgriDataHTTPError

class ErrorResponse:
    def __init__(self, status_code=404, data=None):
        self.status_code = status_code
        self._data = data or {"message": "not found"}
    def raise_for_status(self):
        import requests
        raise requests.HTTPError(f"{self.status_code} Error")
    def json(self):
        return self._data
    @property
    def text(self):
        return json.dumps(self._data)

def test_error_message_exposed(monkeypatch):
    service = AgriDataService()
    def mock_get(url, params=None, timeout=None):
        return ErrorResponse()
    monkeypatch.setattr(service.cereals.client.session, "get", mock_get)
    with pytest.raises(AgriDataHTTPError) as exc:
        service.cereals.get_prices()
    assert "not found" in str(exc.value)
    assert exc.value.status_code == 404
