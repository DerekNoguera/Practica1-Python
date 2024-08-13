class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo    
 
 
 
class Gato(Animal):
    def __init__(self, nombre, tipo , raza):
        super().__init__(nombre, tipo)
        self.raza = raza
    
    def Saludar(self):
        print('Hola soy el Gato: {self.nombre}')
            

class Ave(Animal):
    def __init__(self, nombre, tipo, plumage):
        super().__init__(nombre, tipo)
        self.plumaje =  plumage
        
    def Saludar(self):
        print(f'Hola soy la ave llamada {self.nombre} y mi plumage es {self.plumaje}')

aves = Ave(nombre="Pepito", tipo="Comelona", plumage="Suave")
gatos = Gato(nombre="Michi", tipo='Hombre', raza='Comelona')

aves.Saludar()
            
