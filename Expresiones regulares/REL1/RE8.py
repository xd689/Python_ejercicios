def main(args):
    import re
    patron = r'([0-9]{3}-[0-9]{3}-[0-9]{3})|([0-9]{3}\.[0-9]{3}\.[0-9]{3})|[0-9]{9}'
    tlf = input('Introduce un número de telefono válido: ')
    coincidencia = re.finditer(patron, tlf)
    if (coincidencia):
        for coincidencias in coincidencia:
            inicio = coincidencias.start()
            fin = coincidencias.end()
            print('Se han encontrado números válidos.')
    else:
        print('No se han encontrado números válidos.')
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)