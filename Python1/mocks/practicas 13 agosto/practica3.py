#Práctica 5 Mock



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



# Modificar la clase APIClient vista en clase para manejar el error 404 (Not Found) y el error 500 (Internal Server Error)
# Utilizar response_mock para los escenarios donde la API responda con los errores anteriormente mencionados y verificar el mensaje especifico (en otras palabras si el error es 404 que además de levantar el error, el error contenga el texto "404 not found")

# Utilizar: https://jsonplaceholder.typicode.com/posts