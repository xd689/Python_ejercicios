import sys
import argparse

def leer(fichero):
    archivo = open(fichero, 'r')
    l = archivo.readlines()
    archivo.close()
    return l

def main():
    parser = argparse.ArgumentParser(description="Informe accesos denegados")
    parser.add_argument("ruta",help="description")
    args = parser.parse_args()
    fichero = args.ruta
    l = leer(fichero)
    print(l)

if __name__ == "__main__":
    try:main()
    except KeyboardInterrupt:
        print("\nInterrupción por el usuario.")
        sys.exit(1)