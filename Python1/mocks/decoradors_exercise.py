def decorator(func):
    def wrap(a,b):
        print(f"primer número: {a}, segundo número: {b}, resultado: {func(a,b)}")
        return func(a,b)
    return wrap

@decorator
def suma(a,b):
    return a + b

@decorator
def resta(a,b):
    return a - b

@decorator
def multiplicacion(a,b):
    return a * b

@decorator
def division(a,b):
    return a / b

print(suma(1,2))
print(resta(1,2))
print(multiplicacion(1,2))
print(division(1,2))


import time

def decorator_execution_time(func):
    def wrap():
        start = time.time()
        func()
        end = time.time()
        print(f"Tiempo de ejecución: {end - start}")
    return wrap

@decorator_execution_time
def count():
    for i in range(10_000_000):
        pass
    
@decorator_execution_time
def count2():
    for i in range(1_000_000):
        pass
    
@decorator_execution_time
def count3():
    for i in range(200_000_000):
        pass

count()
count2()
count3()