class Login():
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
    
    def auth(self, username: str, password: str) -> bool:
        users = self.__db_connection.user_list()
        for user in users:
            if username == user["username"] and password == user["password"]:
                return True
        return False
        
import pytest
from unittest.mock import Mock

@pytest.fixture
def login_mock():
    mock_connection = Mock()
    mock_connection.user_list.return_value = [{"username": 'test', "password": 'test'}]
    return Login(mock_connection)

def test_auth(login_mock):
    assert login_mock.auth(username='test', password='test') == True