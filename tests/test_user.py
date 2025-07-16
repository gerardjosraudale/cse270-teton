import requests

def get_users_from_server(url):
    response = requests.get(url)
    return response.json()

def test_get_users_returns_expected_data(mocker):
    # Arrange
    sample_data = [
        {"username": "admin", "role": "Administrator"},
        {"username": "bob", "role": "Member"}
    ]
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.json.return_value = sample_data

    # Act
    result = get_users_from_server("http://127.0.0.1:8000/users")

    # Assert
    assert result == sample_data
    mock_get.assert_called_once_with("http://127.0.0.1:8000/users")
