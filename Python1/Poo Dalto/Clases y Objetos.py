# class Celular():
#     marca = "Samsung"
#     modelo = 'S23'
#     camara = '48MP'

# celular1 = Celular()
# celular2 = Celular()
# print (celular1.marca)

#                                           CLASS
#                                          CONSTRUCTOR
#                                         M E T O D O S
class Celular: 
    def __init__(self, marca, camara, modelo):
        self.marca = marca
        self.camara = camara
        self.modelo = modelo
        
    def llamar(self):
        print(f"Estas haciendo un llamado desde: {self.marca} {self.modelo} ")
    def cortar(self):
        print(f"Estas cortando desde: {self.marca} {self.modelo} ")
    
    
celular1 = Celular("Samsung", "40mp", "S23")
celular2 = Celular("Iphone", "48mp", "15 pro")
celular2.llamar()
celular2.cortar()
