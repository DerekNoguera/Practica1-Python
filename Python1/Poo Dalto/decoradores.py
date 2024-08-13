def decorador(funcion):
    
    def funcion_modificada():
        print('Antes de llamar a la funcion ')
        funcion()
    return funcion_modificada()

# def saludo():
#     print('Hola Derek como estas')
    
# saludo_modificado = decorador(saludo)

# Lo de arriba es lo mismo que lo de abajo, se utiliza para ahorra tiempo y datos de crear otra variable
# para asignarle parametros


@decorador
def saludo():
    print('Hola Derek como estas')
    
