def assert_status_code(response, expected):
    assert response.status_code == expected


def assert_user_id(response, expected_user_id):
    body = response.json()
    assert body["userId"] == expected_user_id
