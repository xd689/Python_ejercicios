#Leer fichero entrada.txt pedido por argumento obligatorio.
#Generar un diccionario desde la entrada.
#Escribir contenido filtrado del diccionario en un fichero que puedes dar o no como argumento. 
import sys
import argparse

def leer_fichero(ruta):
    archivo = open(ruta, 'r')
    l = archivo.readlines()
    return l

def genDicc(l):
    for i in range(len(l)):
        print(l[i])

def main():
    parser = argparse.ArgumentParser(description="Informe accesos denegados")
    parser.add_argument("archivo",help="ruta del archivo a leer")
    args = parser.parse_args()
    ruta = args.archivo
    genDicc(leer_fichero(ruta))
    print(leer_fichero(ruta))

if __name__ == "__main__":
    try:main()
    except KeyboardInterrupt:
        print("\nInterrupción por el usuario.")
        sys.exit(1)