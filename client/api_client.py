import requests
from config.config import BASE_URL, TIMEOUT


class APIClient:
    def get(self, endpoint, params=None):
        return requests.get(
            url=f"{BASE_URL}{endpoint}",
            params=params,
            timeout=TIMEOUT
        )