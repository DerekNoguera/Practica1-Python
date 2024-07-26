import datetime

def fechaNacimiento():
    d = int((input("Ingresa el dia en que naciste en numero: ")))
    m = int(input("Ingresa el mes en que naciste en numero: "))
    y = int(input("Ingresa el año en que naciste en numero: "))
    print(f"Dia {d}, mes {m}, año {y}")
    timeNow = datetime.datetime.now()
    yearVivido = timeNow.year - y
    mesVivido = timeNow.month - m
    diasVividos = timeNow.day - d
    print(f"Llevas vivido \033[32m{yearVivido}\033[97m años, \033[32m{mesVivido}\033[97m meses vividos y \033[32m{diasVividos}\033[97m dias vividos")
if __name__ == "__main__":
    fechaNacimiento()

# function tel_argentino_valido( $tel ) {

#     $num = preg_replace( f'/\D+/', '', $tel)}
#     devolver si coincidió con el regex
#     return preg_match(
#         '/^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$/D',
#         $num
#     );
# }