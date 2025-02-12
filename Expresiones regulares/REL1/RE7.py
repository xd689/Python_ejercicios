def main(args):
    import re
    texto = "Hoy es 15-01-2025 y mañana será 16-01-2025."
    patron = r'\b\d{2}-\d{2}-\d{4}\b'
    coincidencias = re.finditer(patron, texto)
    if (coincidencias):
        for coincidencia in coincidencias:
            inicio = coincidencia.start()
            fin = coincidencia.end()
            print('Se han encontrado fechas en el texto.')
    else:
        print('No se han encontrado fechas en el texto.')
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)