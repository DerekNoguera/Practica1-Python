# EJERCICIO 1
def mostrar_inventario_actual(lista_invetario: dict[str, int]) -> None:
    for i in lista_invetario:
        print(i, lista_invetario[i])
inventario={"Manzanas": 10, "Peras": 5, "Platanos": 8}
mostrar_inventario_actual(inventario)


# EJERCICIO 2
def mostar_orden_de_apuestas(apuestas:list[str]) -> None:
    for i in enumerate(apuestas):
        print(f"Apuesta {i}")
apuestas = ["rojo", "negro", "rojo", "verde"]
mostar_orden_de_apuestas(apuestas)

# EJERCICIO 3

def encontrar_valores_absolutos(numeros: list[int]) -> list[list]:
    x = map(abs, numeros[0:100])
    print(list(x))

numeros = [-3, -2, 0, 1, 2, 3]
encontrar_valores_absolutos(numeros)


# EJERCICIO 4

def encontrar_inventario_bajo(lista_inventario: dict[str, int]) -> dict[str, int]:
    lista_inventario = dict(filter(lambda x: x[1] < 4, lista_inventario.items()))
    print(lista_inventario)
    return lista_inventario
inventario = {"manzana": 2, "peras": 5, "platanos":1}
encontrar_inventario_bajo(inventario)

# EJERCICIO 5

def encontrar_longitudes_de_palabras(lista_palabras: list[str])-> dict[str,int]:
    x = dict(map(lambda palabra: (palabra, len(palabra)), lista_palabras))
    print(x)
    return x
palabras=["Hola", "Bienvenido", "Adios"]
encontrar_longitudes_de_palabras(palabras)

# EJERCICIO 6 
def hey_reprobados(notas: list[int]) -> bool:
    r = any(map(lambda x: (x < 60), notas ))
    print(r)
notas1 = [70,80,50,65]
hey_reprobados(notas1)

# EJERCICIO 7

def somos_todos_palindromos(palindromos: list) -> bool:
    r = all(map(lambda x: x == "".join(reversed(x)), palindromos))
    print(r)
palindromos = ["reconocer", "sometemos", "arenera"]
somos_todos_palindromos(palindromos)

# EJERCICIO 8

def hay_duplicados(lista: list) -> bool: 
    x = len(lista)
    y = list(set(lista))
    if y == x:
        print(True)
    else:
        print(False)
lista = [1,2,3,4,5,1]
hay_duplicados(lista)

# EJERCICIO 9 
def ordenar_por_valor_absoluto(numeros: list[int]) -> list[int]:
    x = sorted(numeros, key=abs)
    print(x)
numeros = [-3,-2,0,1]
ordenar_por_valor_absoluto(numeros)

# EJERCICIO 10

def diferencia_de_edad_mas_grande(edades: list[int])-> int:
    x = max(edades)
    y= min(edades)
    r = x - y
    print(r)
    
    pass
edades=[10,20,30,40]
diferencia_de_edad_mas_grande(edades)