# #Práctica: Clases y herencia
# Crear una clase Persona, con los métodos nombre, apellidos, fecha de nacimiento,
# y un método que se llame saludar que diga: "Hola, me llamo {nombre y apellidos},
# y tengo {edad} años".
# Crear las clases Profesor y Estudiante que hereden de Persona y sobrescriban el
# método saludar para que diga: "Hola, soy el profesor/estudiante {nombre y apellidos},
# y tengo {edad} años".
# Crear una clase Clase que tenga las propiedades: nombre de la clase
# (ej.: Programación Backend), lista de estudiantes y profesor asignado.
# Un método que imprima el nombre y apellido de cada estudiante dentro de la clase,
# y otro método que imprima el mensaje "Clase: {nombre de la clase}, impartida por el profesor {nombre del profesor}"
from datetime import datetime

class Persona:
    def __init__(self, nombre, apellidos, fecha_de_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_de_nacimiento = fecha_de_nacimiento
    
    def saludar(self): #funcion saludar 
        edad = datetime.now().year - self.fecha_de_nacimiento
        return(f'Hola, me llamo {self.nombre} {self.apellidos} y tengo {edad}')
        
        
    
class Profesor(Persona):
    
    def __init__(self, nombre, apellidos, fecha_de_nacimiento):
        super().__init__(nombre, apellidos, fecha_de_nacimiento)
        
    def saludar(self):
        edad = datetime.now().year - self.fecha_de_nacimiento
        print(f'Hola soy estdiante {self.nombre} {self.apellidos} y tengo {edad}')
        


class Estudiante(Persona): 
    
    def __init__(self, nombre, apellidos, fecha_de_nacimiento):
        super().__init__(nombre, apellidos, fecha_de_nacimiento)
        
    def saludar(self):
        edad = datetime.now().year - self.fecha_de_nacimiento
        print(f'Hola soy estdiante {self.nombre} {self.apellidos} y tengo {edad}')
    
    def datos_estudiante(self):
        return (f'{self.nombre} {self.apellidos}')
        
   

class Materias:
    
    def __init__(self, nombre_clase, profesor,nombres_estudiantes):
        self.nombre_clase = nombre_clase
        self.profesor = profesor
        self.nombres_estudiantes = nombres_estudiantes
        
    def listar_estudiantes(self):
        for alumnos in self.nombres_estudiantes:
            print(alumnos)
        
    def Materia(self):
       print(f'La materia {self.nombre_clase} es impartida por {self.profesor}')
   



print('')

profesor1 = Profesor(nombre='Alexa', apellidos='Alvarez', fecha_de_nacimiento = 2002)
estudiante1 = Estudiante(nombre='Derek', apellidos='Noguera', fecha_de_nacimiento=2006)
estudiante2 = Estudiante(nombre='Alessandro', apellidos='Gonzalez', fecha_de_nacimiento=2006)
materias = Materias(
    nombre_clase='Programación Backend',
    profesor=profesor1.nombre,
    nombres_estudiantes=[estudiante1.datos_estudiante(), estudiante2.datos_estudiante()]
)


profesor1.saludar()
estudiante1.saludar()
estudiante2.saludar()
materias.Materia()
materias.listar_estudiantes()




