# EJERCICIO 1
from typing import Generator
print("Ejercicio 1")
def personas_aplandas(lista_personas: list[dict[str, str | dict]]) -> None:
    return  (
        {f'Direccion {persona["direccion"]["calle"]}, numero {persona["direccion"]["numero"]}' for persona in lista_personas}
            for persona in lista_personas
        )
 
datos_anidados = [
    {
       "Nombre": "Juan",
        "Edad": 30,
        "direccion": {"calle": "calle principal", "numero": 123}
    },
    {
      "nombre": "Maria",
      "edad": 25,
      "direccion": {"calle": "Avenido Central", "numero": 456}
    }
]
result = personas_aplandas(datos_anidados)
print(list(result))

def mostrar_orden_de_apuestas(apuestas: list[str]) -> None:
    resultado = [f"Apuesta {apu} es {apuesta}" for apu, apuesta in enumerate(apuestas, start=1)]
    return resultado
apuestas = ["rojo", "negro", "rojo", "verde"]
resultado = mostrar_orden_de_apuestas(apuestas)
print(resultado)


# EJERCICIO 3
print("Ejercicio 4")
def encontrar_valores_absolutos(numeros: list[int])->list[int]:
    return [abs(x) for x in numeros]
numeros=[-3 ,-2 ,-1 , 0 , 1 , 2 , 3 ]
print(encontrar_valores_absolutos(numeros))




# EJERCICIO 4
print("Ejercicio 4")
def encontrar_inventario_bajo(lista_inventario: dict[str, int])->dict[str, int]:
    return {key: v for key,v in lista_inventario.items() if v < 4}
lista_inventario = {"manzanas": 2, "peras":5, "platanos":1}
print(encontrar_inventario_bajo(lista_inventario))




  # EJERCICIO 5
def encontrar_longitudes_de_palabras(lista_palabras: list[str]) -> dict[str, int]:
    return {palabra: len(palabra) for palabra in palabras if len(palabra)}
palabras = ["hola", "bienvenido", "adiós"]
print(encontrar_longitudes_de_palabras(palabras))




# EJERCICIO 6
print("Ejercicio 6")
def hay_reprobados(notas:list[int]) -> bool:
    return any([x < 60 for x in notas])
notas1 = [70,80,50,65]
print(hay_reprobados(notas1))




 # EJERCICIO 7
def son_todos_palindromos(palindromos: list[str]) -> bool:
    return all(palabra == palabra[::-1] for palabra in palindromos)
palindromos = ["reconocer", "sometemos", "arenera"]
print(son_todos_palindromos(palindromos))




# EJERCICIO 8
print("Ejercicio 8")
def contar_palabras_par(palabras: list[str])-> int:
    return len(([x for x in palabras if len(x) % 2 == 0]))
palabras = ["casa","perro","gato","elefante", "jirafa"]
print(contar_palabras_par(palabras))