# Simulando Colaboraciones
# Crea una prueba para la clase Libro que colabora con la clase Biblioteca.
# Crea un test al respecto.
# Utilizar un Mock para asegurar que el método prestar() de Biblioteca sea llamado al prestar un libro.
class Libro():
    def __init__(self, titulo:str, autor:str, unidades:int) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__unidades = unidades
        self.__unidades_prestadas = 0
        
    def prestar(self) -> bool:
        if self.__unidades_prestadas < self.__unidades:
            self.__unidades_prestadas += 1
            return True
        else:
            return False
       
class Biblioteca():
    def __init__(self, libros:list[Libro]) -> None:
        self.__libros = libros 
    
    @property
    def libros(self) -> list[Libro]:
        return self.__libros
    
    def buscar_libro(self, titulo:str) -> Libro:
        for libro in self.__libros:
            if libro._Libro__titulo == titulo:
                return libro
        return None
    
    def prestar_libro(self, titulo:str) -> bool:
        libro = self.buscar_libro(titulo)
        if libro:
            return libro.prestar()
        return False