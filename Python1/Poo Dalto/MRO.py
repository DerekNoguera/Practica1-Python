#                               Metodo de resolucion de orden
class A:
    def hablar(self):
        print ("Hola desde A")
        
class F:
    def hablar(self): #
        print('Hola desde F')   
 
    
class B(A): 
    def hablar(self):
        print ("Hola desde B")

        
        
class C(F): 
    def hablar(self):  
        print ("Hola desde C")

        
        
class D(B,C): 
    def hablar(self):
        print ("Hola desde D")


d = D()
print(D.mro())
d.hablar()
print(issubclass(D, A))

# Si quiero saludar desde una clase en Espifico, tendria que llamar la clase, luego el objeto y la insatancia
# llamo el objeto de la class A
A.hablar(d)