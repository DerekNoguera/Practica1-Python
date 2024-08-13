#Ejercicio 1 Mock
# Dada la clase login crear un test usando fixtures y Mock, utilizando mock para reemplazar la lista de diccionarios
# que recibe el constructor de Login, y comprobamos que auth devuelva True.
# Pista: tenemos que hacer uso de return_value
class Login():
    def __init__(self, db_connection: list[dict]) -> None:
        self.__db_connection = db_connection
   
    def auth(self, username: str, password: str) -> bool:
        users = self.__db_connection.user_list()
        for user in users:
            if username == user["username"] and password == user["password"]:
                return True
        return False

