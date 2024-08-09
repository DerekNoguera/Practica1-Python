def decorator(func):
    def wrap(param):
        print("antes")
        func(param)
        print("después")
    return wrap

@decorator
def saludo(param):
    print("Hola", param)
saludo("mundo")
print()

#Ejercicio 1
# Escribir una function suma que reciba 2 parametros
# Escribir un decorador que muestre los parametros enviados y el resultador de la suma.

def sumaDeco(func_suma):
    def wrap(a,b):
        print(f"Numeros son {a} y {b}")   
        r = func_suma(a,b)  
        print(f"Print despues de la funcion")
        return r
    return wrap
   
@sumaDeco
def suma(a,b):
    print(a + b)
suma(3,3)
print()

#Ejercicio 2
# Escribir una funcion que imprima los numeros entre 1 a 1000.
# Escribir un decorador que imprima el tiempo de ejecución de la función.
 
import time
def decoImprimor(func_imprimir):
    def wrap():
        start = time.time()
        r = func_imprimir()
        fin = time.time() - start
        print(f"{fin} segundos")
        return r
    return wrap
    
@decoImprimor
def imprimir():
    time.sleep(1)
    for i in range(1001):
        # print(i)
        pass 
imprimir()