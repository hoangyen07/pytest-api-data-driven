import requests
from config.config import BASE_URL, TIMEOUT
import logging
logger = logging.getLogger(__name__)


class APIClient:
    def get(self, endpoint, params=None):
        return requests.get(
            url=f"{BASE_URL}{endpoint}",
            params=params,
            timeout=TIMEOUT
        )
    
    def get_posts(self):
        logger.info("GET /posts")
        logger.debug("Sending request to jsonplaceholder")