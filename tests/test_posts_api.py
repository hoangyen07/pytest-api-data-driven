import pytest
from client.api_client import APIClient
from utils.assertions import assert_status_code, assert_user_id


client = APIClient()


# @pytest.mark.parametrize("test_data", [])
# def test_placeholder():
#     pass


def test_posts_api(posts_test_data):
    print(posts_test_data)
    for test in posts_test_data:
        response = client.get(test["endpoint"])
        print(response)
    assert_status_code(response, test["expected_status"])

    if "expected_user_id" in test:
        assert_user_id(response, test["expected_user_id"])


def add(x, y):
    return x + y


def test_add():
    assert add(4, 5) == 9
