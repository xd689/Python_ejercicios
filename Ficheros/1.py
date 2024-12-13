def main(args):
#Recorrido del archivo linea a linea
    try:
        archivo=open("/home/usuario/ficheroTexto1.txt")
    except FileNotFoundError:
        print("Archivo no encontrado")
    for linea in archivo:
        print(linea)

#Recorrido del archivo linea a linea sin saltos por rstrip() y posicion en el inicio con seek(0) 
    archivo.seek(0)
    for linea in archivo:
        print(linea.rstrip())
    archivo.close()

#Recorrido del archivo en una cadena por read()
    try:
        archivo=open("/home/usuario/ficheroTexto1.txt")
    except FileNotFoundError:
        print("Archivo no encontrado")
    contenido=archivo.read()
    print("\n CONTENIDO COMPLETO\n")
    print(contenido)
    archivo.close()

#Elegir linea a leer del archivo de texto
    try:
        archivo=open("/home/usuario/ficheroTexto1.txt")
    except FileNotFoundError:
        print("Archivo no encontrado")
        print('IMPRIMIMOS SOLO UNA LÍNEA CON READLINE()')
    linea=archivo.readline()
    print(linea)
    print('IMPRIMIMOS SOLO 3 CARACTERES CON READLINE()')
    linea=archivo.readline(5)
    print(linea)
    return 0
if __name__ == "__main__":
    import sys
    main(sys.argv)