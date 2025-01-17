def main(args):
    import re
    patron = 'bella'
    texto = 'La vida es Bella'
    comp = re.compile(patron,re.I)
    coincidencia = comp.search(texto)
    if (coincidencia):
        inicio = coincidencia.start()
        fin = coincidencia.end()
        print('Se ha encontrado "{}" en "{}" desde {} hasta {} ("{}")'.format(patron, texto, inicio, fin, texto[inicio:fin]))
    else:
        print("El patrón no está en el texto")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)