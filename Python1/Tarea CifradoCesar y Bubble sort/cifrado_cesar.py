
def main(x = None,Num = None):

    resul1 = ""
    textArrelado = []
    if x is None:
        x = str(input("Cadena a cifrar: ")).lower()
    if Num is None:
         Num = int(input("A cuantos números lo quieres cifrar: "))
    for i in x:
        dato=chr(ord(i) + Num)
        textArrelado.append(dato)
    for i in textArrelado:
        resul1 += i
    print(f"Cadena cifrada {resul1}")  

    # newArreglo = []
    # resul = ""
    # x = str(input("Cadena a decifrar:  ")).lower()
    # for i in x:
    #     dato=chr(ord(i) - Num)
    #     newArreglo.append(dato)
    # for i in newArreglo:
    #     resul += i
    # print(f"Cadena decifrada {resul}")
    return (resul1)
    
if __name__ == "__main__":
    main()