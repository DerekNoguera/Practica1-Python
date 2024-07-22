import calculator

def main():
    while True:
        print("Bienvenido a la calculadora, por favor selecciona una operacion")
        option = input("(+,-,*,/,q): ")
        
        if option == "q":
            print("Terminando el programa")
            break
        if option not in ["+", "-", "*", "/",]:
            print(f"Error: opcion invalida {option}")
            continue
        
        try:
            num1 = float(input("Input de el primer numero: "))
            num2 = float(input("input de el segundo numero: "))
        except ValueError:
            print("Error, input invalido, por favor un numero como input")
            continue
        
        if option == "+":
            result = calculator.add(num1, num2)
        elif option == "-":
            result = calculator.subtract(num1, num2)
        elif option == '*':
            result = calculator.multiply(num1,num2)
        else:
            result = calculator.divide(num1, num2)
            
        print(f"El resultado de tu operacion es {result}")
if __name__ == "__main__":
    main()
