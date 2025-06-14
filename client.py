
# client.py
import requests
from .config import API_BASE_URL, DEFAULT_TIMEOUT

class AgriDataClient:
    def __init__(self, api_key: str, timeout: int = DEFAULT_TIMEOUT):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json"
        })
        self.timeout = timeout

    def _get(self, category: str, service: str, params: dict):
        url = f"{API_BASE_URL}/{category}/{service}"
        resp = self.session.get(url, params=params, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()
