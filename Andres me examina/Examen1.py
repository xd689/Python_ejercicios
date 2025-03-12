#Leer fichero entrada.txt pedido por argumento obligatorio.
#Generar un diccionario desde la entrada.
#Filtrar usuarios segun requisitos:
#ip no valida
#correo no valido o dominio no valido
#dni no valido
#Escribir contenido filtrado del diccionario en un fichero que puedes dar o no como argumento. 
import re
import sys
import argparse

def leer_fichero(ruta):
    archivo = open(ruta, 'r')
    l = archivo.readlines()
    archivo.close()
    return l

def genDicc(l):
    diccionarios = []
    patIP = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    patDom = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    patDni = r'^\d{8}[A-Za-z]$'
    for i in range(len(l)):
        sepa = l[i].split()
        if re.match(patIP, sepa[5]):
            if re.match(patDom, sepa[8]):
                if re.match(patDni, sepa[15]+sepa[18]):
                    dicc = {
                    "Usuario: ":sepa[2],
                    "IP: ":sepa[5],
                    "Mail: ":sepa[8],
                    "Dominio: ":sepa[11],
                    "Numero dni: ":sepa[15]+sepa[18]
                    }
                    diccionarios.append(dicc)
                else: print(f"El usuario {sepa[2]} no tiene un DNI valido.")
            else: print(f"El usuario {sepa[2]} no tiene un correo valido.")
        else: print(f"El usuario {sepa[2]} no tiene una IP valida.")
    return diccionarios

def escribir(s, d):
    archivo = open(s, 'w')
    for i in range(0,len(d)):
        archivo.write("Usuario: "+str(d[i]['Usuario: ']+"\n"))
        archivo.write("IP: "+str(d[i]['IP: ']+"\n"))
        archivo.write("Mail: "+str(d[i]['Mail: ']+"\n"))
        archivo.write("Dominio: "+str(d[i]['Dominio: ']+"\n"))
        archivo.write("Numero dni: "+str(d[i]['Numero dni: ']+"\n"))
    archivo.close()

def main():
    parser = argparse.ArgumentParser(description="Informe accesos denegados")
    parser.add_argument("archivo",help="ruta del archivo a leer")
    parser.add_argument("--write",help="ruta del archivo a escribir")
    args = parser.parse_args()
    ruta = args.archivo
    if args.write:
        salida = args.write
    else:
        salida = "diccionario.txt"
    genDicc(leer_fichero(ruta))
    escribir(salida, genDicc(leer_fichero(ruta)))

if __name__ == "__main__":
    try:main()
    except KeyboardInterrupt:
        print("\nInterrupción por el usuario.")
        sys.exit(1)