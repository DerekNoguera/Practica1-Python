import json
import yaml
#               1


datos = [
    {
        "nombre": "Pikachu",
        "tipo": "Electrico",
        "nivel": 25,
    },
    {
        "nombre": "Charmander",
        "tipo": "Fuego",
        "nivel": 18,
    },
    {
        "nombre": "Squirtle",
        "tipo": "Agua",
        "nivel": 20,
    }
]

with open("archivo.txt", "w") as f:
    archivo_yaml = yaml.dump(datos,f)
    
variable_yaml = yaml.dump(datos)
print(variable_yaml)

datos_leidos = yaml.safe_load(variable_yaml)
print(datos_leidos)



#                2
with open("archivo.json", "r") as f:
    archivo_yaml = json.load(f)
print(archivo_yaml)
    