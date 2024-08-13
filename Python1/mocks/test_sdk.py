import os
from sdk import SDK, EnvMissingError
import pytest

@pytest.fixture(scope="session", autouse=True)
def set_api_key():
    # Establecer la variable de entorno API_KEY para las pruebas
    os.environ["API_KEY"] = "test_api_key"
    yield
    # Limpiar la variable de entorno API_KEY después de las pruebas
    del os.environ["API_KEY"]

def test_my_class_with_env_variable():
    SDK()

def test_my_class_without_env_variable():
    # Asegúrate que la variable de entorno API_KEY no esté configurada
    if "API_KEY" in os.environ:
        del os.environ["API_KEY"]

    with pytest.raises(EnvMissingError):
        SDK()