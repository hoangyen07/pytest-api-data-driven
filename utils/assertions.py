def assert_status_code(response, expected):
    print(response.json())
    assert response.status_code == expected


def assert_user_id(response, expected_user_id):
    body = response.json()
    print(body)
    assert body["userId"] == expected_user_id
