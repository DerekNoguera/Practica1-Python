
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





#                                HERENCIA MULTIPLE

# Cuando es Herencia multiple al llamar en empleadoArtista doble classes como Herencia
# EN Lugar de usar SUPER() usamos el nombre de la clase que llamamos como Herencia
# Persona.__init__(self, nombre, edad, nacionalidad)
# artista.__init__(self, habilidad)

class artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def Habilidad(self):
        return(f"{self.habilidad}")
        
        
class EmpleadoArtista(Persona,artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    # def Habilidad(self):
    #     print(f"No tengo habilidad jaja")
    # Presentarse hace referencia a la habilidad de arriba, se llama con SUPER() y no self
    # Pq debemos decirle de donde proviene y proviene de un Superior, osea 
    # de el que lo hereda. Si usara self.Habilidad, mostraria la habilidad de arriba que dice 
    # Que no tiene habiliada jaja
    def Presentarse(self):
        print(f"Hola soy: {self.nombre} y mi habilidad es {super().Habilidad()} y trabajo en {self.empresa}")

RobertoArtista = EmpleadoArtista("Roberto", 23, 'Tico',"Cantar", 100000, "Google")
RobertoArtista2 = artista("Cantar",)
RobertoArtista.Presentarse()


herencia = issubclass(EmpleadoArtista, artista or Persona)
instancia = isinstance(RobertoArtista2, Persona)
print(herencia) #TRUE
print(instancia) # FALSE pq solo Hereda de artista y hereda 'Cantar'
        