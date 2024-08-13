class MiClass:
    def __init__(self):
        self.__privado = 'Hola'
        
    def _hablar(self):
        print(f'Hola ')

objeto = MiClass()

# No se puden acceder pq ambos son privados
# print(objeto.__privado)
# print(objeto.__hablar())



class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self, ):
       return self.__nombre
        
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    
# de esa manera se acceden a datos privados o muy privados
derek = Persona("Derek", 17)
nombre = derek.get_nombre()
print(nombre)


derek.set_nombre('Alexa')
nombre = derek.get_nombre()
print(nombre)