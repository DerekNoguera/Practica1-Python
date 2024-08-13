import requests

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_data(self, endpoint: str):
        response = requests.get(f"{self.base_url}/{endpoint}")
        if response.status_code == 200:
            print("Success")
            return True
        else:
            raise requests.exceptions.HTTPError("Error")


import pytest
from unittest.mock import patch, Mock

@pytest.fixture
def api_client():
    return APIClient('https://jsonplaceholder.typicode.com')

@patch('requests.get')
def test_get_data_200(mock_get, api_client):
    mock_get.return_value = Mock(status_code=200)

    result = api_client.get_data('todos/1')
    mock_get.assert_called_with('https://jsonplaceholder.typicode.com/todos/1')
    assert result == True

@patch('requests.get')
def test_get_data_non_200(mock_get, api_client):
    mock_get.return_value = Mock(status_code=404)
    
    with pytest.raises(requests.exceptions.HTTPError):
        api_client.get_data('todos/1')
    mock_get.assert_called_with('https://jsonplaceholder.typicode.com/todos/1')

def test_get_data_with_response_mock(response_mock, api_client):
    with response_mock('GET https://jsonplaceholder.typicode.com/todos/1 -> 200 :Success', bypass=False):
        assert api_client.get_data('todos/1') == True

def test_get_data_with_response_mock_error(response_mock, api_client):
    with response_mock('GET https://jsonplaceholder.typicode.com/todos/1 -> 404 :Not found', bypass=False):
        with pytest.raises(requests.exceptions.HTTPError):
            api_client.get_data('todos/1')