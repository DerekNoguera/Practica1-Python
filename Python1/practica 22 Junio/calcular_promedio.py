import ipdb


def calcular_promedio(numeros):
    if len(numeros) == 0:
        return False
    else:
        total = 0
        for numero in numeros:
            total+=numero
        promedio = total / (len(numeros))
        return promedio

if __name__ == "__main__":
    calcular_promedio()

