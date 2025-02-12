#leer el archivo /etc/hosts como argumento desde consola
#cada linea en un diccionario
#añadir el nombre de host y su ip desde consola
#puede no estar o haber mas de 1
import sys
import re
import argparse
def leer(ruta):
    print(ruta)
    archivo = open(ruta[0], 'r')
    lineas = archivo.readlines()
    archivo.close()
    return lineas

def guardaLineas(lineas):
    dicc = {}
    for linea in lineas:
        partes = re.split(r'\s+', linea.strip())
        if len(partes) >= 2:
            ip = partes[0]
            host = partes[1]
            dicc[host] = ip
        print(partes)
    return dicc

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('ruta', help='Ruta del archivo hosts', nargs=1)
    args = parser.parse_args()
    print(leer(args.ruta))
    dicc = guardaLineas(leer(args.ruta))
    print(dicc)