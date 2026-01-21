import logging
from client.api_client import APIClient
from utils.assertions import assert_status_code, assert_user_id


client = APIClient()


# @pytest.mark.parametrize("test_data", [])
# def test_placeholder():
#     pass

logger = logging.getLogger(__name__)


def test_posts_api(posts_test_data):
    for test in posts_test_data:
        response = client.get(test["endpoint"])
    assert_status_code(response, test["expected_status"])

    if "expected_user_id" in test:
        assert_user_id(response, test["expected_user_id"])


def add(x, y):
    return x + y


def test_add():
    logger.debug("Loaded test data: %s", add(4, 5))
    assert add(4, 5) == 9


def test_get_posts():
    client.get_posts()
    logger.info("START test_get_posts")
    assert True


def test_failed():
    logger.debug("Loaded test data: %s", add(4, 5))
    assert add(4, 5) == 89
