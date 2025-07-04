# client.py
import requests
from .config import API_BASE_URL, DEFAULT_TIMEOUT
from .exceptions import AgriDataHTTPError


def _extract_error_message(resp) -> str:
    """Return the error message extracted from a response."""
    try:
        data = resp.json()
        if isinstance(data, dict):
            return data.get("message") or data.get("error") or resp.text
    except Exception:
        pass
    return resp.text


class AgriDataClient:
    def __init__(self, timeout: int = DEFAULT_TIMEOUT):
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})
        self.timeout = timeout

    def _get(self, category: str, service: str, params: dict):
        url = f"{API_BASE_URL}/{category}/{service}"
        resp = self.session.get(url, params=params, timeout=self.timeout)
        try:
            resp.raise_for_status()
        except requests.HTTPError as exc:
            message = _extract_error_message(resp)
            raise AgriDataHTTPError(resp.status_code, message) from exc
        return resp.json()
