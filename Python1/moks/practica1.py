# Simulando Colaboraciones
# Crea una prueba para la clase Libro que colabora con la clase Biblioteca.
# Crea un test al respecto.
# Utilizar un Mock para asegurar que el método prestar() de Biblioteca sea llamado al prestar un libro.

class Biblioteca:
    def __init__(self, contenido) -> None:
        self.contenido = contenido
        
class Libro(Biblioteca):
    def __init__(self, contenido):
        super().__init__(contenido)
        
    def fun(self):
        for n, i in enumerate(self.contenido, 1):
            print(f"{n} {i}:")

x = {
    "Las 48 leyes del poder": "Libro de no se",
    "Patron Bitcoin": "Libro de no se",
}
biblioteca = Biblioteca(x)
mostrarLibros = Libro(x)
mostrarLibros.fun()
