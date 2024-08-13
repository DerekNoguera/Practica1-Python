def decorator(func):
    def wrap(param):
        print("antes")
        func(param)
        print("después")
    return wrap

@decorator
def saludo(param):
    print("Hola", param)

saludo("mundo");

def decorator2(parametro): #keylor
    def decorator(func): #function original
        def wrap(argumento): #mundo
            print(f"param: {parametro}")
            print(f"arg: {argumento}")
            print("antes")
            func(argumento)
            print("después")
        return wrap
    return decorator

@decorator2("Derek")
def saludo2(param):
    print("Hola", param)

saludo2("mundo");