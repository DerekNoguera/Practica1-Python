
# import keyboard
# posicion_mario = 5
# posicion_enemigo = 10
# movimientos = 0
# nombre = ""

# def juego():
#     global x
#     x = input("Ingresa el nombre del jugador: ")
#     print( f"Bienvenido {x} a tu aventura en el Reino Champiñón")
# juego()

# sprint = True 

# def adelanteMovimiento():
#     global sprint
#     global posicion_mario
#     if sprint == True:
#         posicion_mario = posicion_mario + 3
#         print()
#         print(f"Holaa {x}")
#         sprint=False
#     posicion_mario = posicion_mario + 1
#     print(f"La posicion de {x} es {posicion_mario}")
#     colision()
# def atrasMovimiento():
#     global posicion_mario
#     posicion_mario = posicion_mario - 1
#     print(f"La posicion de {x} es {posicion_mario}")
#     colision()

# def colision():
#     if posicion_mario >= posicion_enemigo:
#         print("")
#         print("Los jugadores han chocado")

# keyboard.on_press_key("W", lambda _: adelanteMovimiento())
# keyboard.on_press_key("S", lambda _: atrasMovimiento())
# print(f"W para mover a {x} adelante y S para moverlo atras y ESC para salir.")

# keyboard.wait("esc")
import keyboard
import sys
posicion_mario = 5
posicion_enemigo = 10
movimientos = 0
nombre = ""

def juego():
    global x
    x = input("Ingresa el nombre del jugador: ")
    print( f"Bienvenido {x} a tu aventura en el Reino Champiñón")
juego()

def adelanteMovimiento():
    global posicion_mario
    posicion_mario = posicion_mario + 1
    print(f"La posicion de {x} es {posicion_mario}")
    colision()
    
def sprint(): 
    global posicion_mario
    print(f"Holaaa {x}")
    posicion_mario = posicion_mario + 3
    print(f"La posicion de {x} es {posicion_mario}")
    colision()
    
def atrasMovimiento():
    global posicion_mario
    posicion_mario = posicion_mario - 1
    print(f"La posicion de {x} es {posicion_mario}")
    colision()

def colision():
    if posicion_mario >= posicion_enemigo:
        print("")
        print("Los jugadores han chocado")
        print("Juego terminado")
        sys.exit()
        
keyboard.on_press_key("W", lambda _: adelanteMovimiento())
keyboard.on_press_key("S", lambda _: atrasMovimiento())
keyboard.on_press_key("X", lambda _: sprint())
print(f"W para mover a {x} adelante, S para moverlo atras, X para correr y ESC para salir.")

keyboard.wait("esc")

