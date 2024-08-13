# class Estudiante:
#     def __init__(self,Nombre, edad, grado):
#         self.nombre = Nombre
#         self.edad = edad
#         self.grado = grado
#     def estudiar(self):
#         print(f'el estudiante {self.nombre} esta estudiando')
        
# nombreEstu = input("Ingresa el nombre de el estudiante: ")
# EdadEstu = input('Ingresa la edad de el estudiante: ')
# GradoEstu = input('Ingresa el grado de el estudiante: ')
# estudiante = Estudiante(nombreEstu, EdadEstu, GradoEstu)
# estudiante.estudiar()

class Estudiante:
    def __init__(self,Nombre, edad, grado):
        self.nombre = Nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print('Estudiando...')
        
nombreEstu = input("Ingresa el nombre de el estudiante: ")
EdadEstu = input('Ingresa la edad de el estudiante: ')
GradoEstu = input('Ingresa el grado de el estudiante: ')
estudiante = Estudiante(nombreEstu, EdadEstu, GradoEstu)

while True:
    estudiar = input()
    if (estudiar.lower() == 'estudiar'):
        estudiante.estudiar()
        break

