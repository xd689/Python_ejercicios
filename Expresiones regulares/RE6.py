def main(args):
    import re
    patron = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 
    texto = input("Introduzca una dirección de correo válida: ")
    coincidencia = re.match(patron, texto)
    if (coincidencia):
        inicio = coincidencia.start()
        fin = coincidencia.end()
        print(f'La dirección de correo {texto} es válida.')
    else:
        print("La dirección de correo no es válida.")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)