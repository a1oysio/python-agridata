import pytest
import requests

from agridata.client import AgriDataClient, AgriDataHTTPError


class MockResponse:
    def __init__(self, status_code=404, json_data=None, text=""):
        self.status_code = status_code
        self._json = json_data or {}
        self.text = text

    def json(self):
        return self._json

    def raise_for_status(self):
        raise requests.HTTPError()


class MockSession:
    def get(self, *args, **kwargs):
        return MockResponse(status_code=404, json_data={"message": "Not Found"}, text="Not Found")


def test_http_error_raised():
    client = AgriDataClient()
    client.session = MockSession()
    with pytest.raises(AgriDataHTTPError) as exc:
        client._get("foo", "bar", {})
    assert exc.value.status_code == 404
