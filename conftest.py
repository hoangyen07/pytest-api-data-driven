import json
import pytest


@pytest.fixture(scope="session")
def posts_test_data():
    with open("data/posts_test_data.json") as f:
        return json.load(f)
