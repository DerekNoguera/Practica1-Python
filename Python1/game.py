import keyboard
import random
filas = 3
columnas = 3
mapa = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
posiciones = [(i,j) for i in range(filas) for j in range(columnas)]
personaje1, robot = random.sample(posiciones,2)
print(f"Derek {personaje1}")
print(f"Robot {robot}")

x = input("Ingresa x: ")
if x == "x":
    print(robot)
def adelanteMovimiento():
    x =personaje1[0]
    print(x)
    
    
    
keyboard.on_press_key("W", lambda _: adelanteMovimiento())
# keyboard.on_press_key("S", lambda _: atrasMovimiento())
# keyboard.on_press_key("X", lambda _: sprint())
print(f"W para mover adelante, S para moverlo atras, X para correr y ESC para salir.")

keyboard.wait("esc")

