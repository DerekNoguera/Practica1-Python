
#                               H E R E N C I A
class Persona:
    #Se le declaran los atributos de la persona
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print (f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
        
        
class Empleado(Persona):
    # El Empleado HEREDA los atributos de la Persona
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        #Usa el Super() para llamar un constructor dentro de un contrustor'
        # Te ahorra codigo y evita errores, se le pasas los atributos que tenia y
        # se agrean los nuevos
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    # def hablar(self):
    #     print("Hola xxdddddddd")

Roberto = Empleado("Roberto", 23, 'Tico', "Programador", 100000) # Se envian los valores de los atributos
print(Roberto.nacionalidad)
Roberto.hablar()
        