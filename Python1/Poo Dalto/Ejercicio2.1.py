# Ejercicio de herencia y uso de super:

# Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: Persona y
# Estudiante. La clase Persona tendrá los atributos de nombre y edad y un método que imprima el
# nombre y la edad de la persona. La clase Estudiante heredará de la clase Persona y también tendrá
# un atributo adicional: grado y un método que imprima el grado del estudiante.

# Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre (Persona).
# Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte de que
# todo funciona correctamente.


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f'Mi nombre es {self.nombre} y mi edad es {self.edad}')
        

class Estudiante(Persona):
    def __init__(self,nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def mostrar_Grado(self,):
        print(f'Mi grado es {self.grado}')

# Cree una instancia para los datos
estudiante = Estudiante("Dalto", 19, "10mo")
estudiante.mostrar_datos()
estudiante.mostrar_Grado()


    