from datetime import datetime
import re
#Crea una función que tome una fecha de nacimiento como entrada y calcule la edad
#actual.


def calcular_edad():
    x = datetime.now()
    
    y = int(input("Ingresa tu year de nacimiento: "))
    m = int(input("Ingresa tu mes de nacimiento: "))
    d = int(input("Ingresa tu dia de nacimiento: "))

    fecha_nacimiento = datetime(y, m, d)
    diferencia = x - fecha_nacimiento
    años = diferencia.days // 365
    meses = (diferencia.days % 365) // 30
    dias = (diferencia.days % 365) % 30

    print(f'Has vivido {años} years, {meses} meses y {dias} dias.')
    print(f'En días serían {diferencia.days} días.')

calcular_edad()




# Escribe una expresión regular que busque todos los numeros de telefono de un texto.
# Los número deben tener esta forma 8888-8888.
def numerosTelefonicos():
    texto = """Hola soy derek y mi numero es 8899-9900"""

    patron = r'\b\d{4}-\d{4}\b'
    numeros_telefonos = re.findall(patron, texto)
    print(numeros_telefonos)
numerosTelefonicos()



#Crea dos funciones que permitan codificar y decodificar un texto en ascii que
#contenga una ñ. Para esto se recomienda cambiar el carácter por un grupo permitido
#poco convencional.

def codificar(texto):
    secuencia_reemplazo = '~N~'
    texto_codificado = texto.replace('ñ', secuencia_reemplazo)
    texto_codificado = texto_codificado.replace('Ñ', secuencia_reemplazo.upper())
    return texto_codificado

def decodificar(texto_codificado):

    secuencia_reemplazo = '~N~'
    texto_decodificado = texto_codificado.replace(secuencia_reemplazo, 'ñ')

    texto_decodificado = texto_decodificado.replace(secuencia_reemplazo.upper(), 'Ñ')
    return texto_decodificado

texto_original = "España es un país con muchas montañas y cañones."
texto_codificado = codificar(texto_original)
texto_decodificado = decodificar(texto_codificado)

print("Texto Original:", texto_original)
print("Texto Codificado:", codificar(texto_original))
print("Texto Decodificado:", decodificar(texto_codificado))
