import re
import sys
import argparse
def es_correo_electronico(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("correos", nargs='+')
    args = parser.parse_args()
    for correo in args.correos:
        if es_correo_electronico(correo):
            print(f"'{correo}' es un correo electrónico válido.")
        else:
            print(f"'{correo}' no es un correo electrónico válido.")
#ejemplo@dominio.com ejemplo.dominio.com ejemplo@dominio ejemplo@dominio.c @dominio.com