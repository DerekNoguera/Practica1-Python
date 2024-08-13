# Polimorfisdo de Herencia, Subtipos o Subclases
# Se pueden enviar sin Herencia pero solamente funciona en python pq es de tipado dinamico
# en Java o C daria error pq los metodos sonido se tendrian que llamar distinto

class Animal:
    pass


class Gato(Animal):
    
    def Sonido(self):
        return "Miau!"
    
    
class Perro(Animal):
    
    def Sonido(self):
        return "Guau!"
    
    
def hacer_sonido(animal):
    print(animal.Sonido())


gato = Gato()
perro = Perro()

# print(gato.Sonido())
# print(perro.Sonido())

hacer_sonido(gato)
hacer_sonido(perro)


#  Crear una clase padre llamada Animal y dos subclases llamadas Gato y Perro.
#  La clase Animal debe tener un método llamado sonido que devuelva un string con el sonido del animal.
#  La clase Gato debe heredar de Animal y sobreescribir el método sonido para que devuelva "Miau!".
#  La clase Perro debe heredar de Animal y sobreescribir el método sonido para que devuelva "Guau!".
#  Crear una función llamada hacer_sonido que toma un objeto Animal como parámetro y utiliza el método sonido para imprimir el sonido del animal.
#  Ejecutar la función con un objeto de cada subclase y comprobar que el sonido es el esperado.