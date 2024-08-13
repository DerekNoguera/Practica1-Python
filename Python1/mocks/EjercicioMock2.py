#Ejercicio 2 Mock
# Dada la clase APIClient y utilizando el fixtures, Mock, y el decorador @patch, 
        # crear dos tests:
# El primer test simulamos que el get es exitoso y devuelve un resultado 200,
        # que mock.get (request.get) se llamó al menos 1 vez, y que get_data devolvió True.
# El segundo test simulamos que el get falla y devuelve un resultado 404 
        # y se levanta la exepción HTTPError
# Pista: tenemos que hacer uso de return_value

# Documentacion del decorador patch =
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
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

