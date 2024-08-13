# Crea una clase Casa que contenga una composición de objetos Habitación. Cada
# habitación debe tener una descripción.

from typing import Any


class Habitacion:
    
    def __init__(self, descripcion):
        self.descripcion = descripcion
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion):
        if len(descripcion) < 5:
            raise ValueError('La descripción debe tener al menos 5 caracteres.')
        self.__descripcion = descripcion

class Casa:
    def __init__(self,):
        self.__habitaciones = []
        
    def set_habitacion(self, habitacion):
        self.__habitaciones.append(habitacion)
    
    def mostrar_habitacion(self):
        for i, habitacion in enumerate(self.__habitaciones, 1):
            print(f"Habitación {i}: {habitacion.descripcion}")
    
habitacion1 = Habitacion(descripcion='Sala con vista al jardín')
habitacion2 = Habitacion(descripcion='Cuarto Principal')

casa = Casa()
casa.set_habitacion(habitacion1)
casa.set_habitacion(habitacion2)
casa.mostrar_habitacion()

# ______________________________________________________________________________________

# Diseña una clase Coche que utilice composición para contener objetos Motor y
# Ruedas. Crea un método que simula conducir el coche y mostrar la velocidad.

import time

class Motor:
    def __init__(self, modelo:str) -> None:
        self.__validar_tipo(modelo, str)
        self.__modelo = modelo
    
    @property
    def modelo(self):
        return self.__modelo
    
    def __validar_tipo(self, elemento, tipo):
        if not isinstance(elemento, tipo):
            raise TypeError(f"Expected argument to be a {tipo}, got {type(elemento).__name__}")
    
class Ruedas:
    def __init__(self, modelo:str, cantidad:int) -> None:
        self.__validar_tipo(modelo, str)
        self.__validar_tipo(cantidad, int)
        self.__modelo = modelo
        self.__cantidad = cantidad
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    def __validar_tipo(self, elemento, tipo):
        if not isinstance(elemento, tipo):
            raise TypeError(f"Expected argument to be a {tipo}, got {type(elemento).__name__}")
    
class Carro:
    def __init__(self, modelo:str, velocidad_maxima:int, aceleracion:int, motor:Motor, ruedas:Ruedas) -> None:
        self.__validar_tipo(modelo, str)
        self.__validar_tipo(velocidad_maxima, int)
        self.__validar_tipo(aceleracion, int)
        self.__validar_tipo(motor, Motor)
        self.__validar_tipo(ruedas, Ruedas)
        self.__modelo = modelo
        self.__velocidad_maxima = velocidad_maxima
        self.__aceleracion = aceleracion
        self.__motor = motor
        self.__ruedas = ruedas
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def velocidad_maxima(self):
        return self.__velocidad_maxima
    
    @property
    def aceleracion(self):
        return self.__aceleracion
    
    @property
    def motor(self):
        return self.__motor
    
    @property
    def ruedas(self):
        return self.__ruedas
    
    @motor.setter
    def motor(self, motor:Motor):
        self.__motor = motor
    
    @ruedas.setter
    def ruedas(self, ruedas:Ruedas):
        self.__ruedas = ruedas
    
    def __validar_tipo(self, elemento, tipo):
        if not isinstance(elemento, tipo):
            raise TypeError(f"Expected argument to be a {tipo}, got {type(elemento).__name__}")
                
    def conducir(self, velocidad_maxima):
        def acelerar(self, velocidad_maxima):
            velocidad = 0
            while velocidad < velocidad_maxima:
                velocidad += self.aceleracion
                time.sleep(1)
                yield velocidad
        if velocidad_maxima > self.velocidad_maxima:
                velocidad_maxima = self.velocidad_maxima
        for velocidad_actual in acelerar(self, velocidad_maxima):
            print(f"velocidad actual: {velocidad_actual} km/h")
            
motor = Motor(modelo="I6")
ruedas = Ruedas(modelo="Drifty boi tires", cantidad=4)
carro = Carro(modelo="BMW E36", velocidad_maxima=220, aceleracion=10, motor=motor, ruedas=ruedas)
carro.conducir(80)
    
    
    
# Imagina que estás construyendo un juego de rol. Diseña clases Personaje y Habilidad.
# Utiliza composición para que un personaje pueda tener varias habilidades.

class Habilidad:
    
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    def __str__(self): 
        return f'Habilidad de {self.nombre}'


class Personaje:
    
    def __init__(self, nombre, habilidades = None):
        self.__nombre = nombre
        self.__habilidades = habilidades if habilidades else []
        
    def set_habilidad(self, habilidad):
        self.__habilidades.append(habilidad)
        
    def mostrar_habilidad(self):
        print(f'Personaje: {self.__nombre}')
        if not self.__habilidades:
            print('No tiene habilidades.')
        else:
            for i, habilidad in enumerate(self.__habilidades, 1):
                print(i, habilidad)
   
   
habilidad1 = Habilidad('Ataque V') 
Habilidad2 = Habilidad('Fuerza II')
habilidad3 = Habilidad('Speed II')

personaje1 = Personaje(nombre='Derek')
personaje1.set_habilidad(habilidad1)
personaje1.set_habilidad(Habilidad2)
personaje1.set_habilidad(habilidad3)

personaje1.mostrar_habilidad()