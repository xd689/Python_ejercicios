def main(args):
	"""
	#abrimos el archivo. Si no especificamos nada el modo será lectura.
	try:
		archivo=open("ficheroTexto1.txt")
	except FileNotFoundError:
	    print("Archivo no encontrado")
	    
	#############################################################################
	#             recorrido línea a línea usando la capacidad iterable
	#############################################################################
	for linea in archivo:
		print(linea)
	
	#podemos eliminar el salto de línea para que no sean dos (el que está en el fichero texto y el que añade print)
	archivo.seek(0) #nos situamos al inicio del fichero
	
	
	for linea in archivo:
		print(linea.rstrip())
		
	#cuando terminamos podemos cerrar el fichero
	archivo.close()
	
	"""
	"""
	#############################################################################
	#             lectura del archivo completo en una cadena read()
	#############################################################################
	
	#abrimos el archivo
	try:
		archivo=open("ficheroTexto1.txt")
	except FileNotFoundError:
	    print("Archivo no encontrado")
	
	#usamos el método read() que devolverá todo el contenido en una cadena de texto
	contenido=archivo.read()
	print("\n CONTENIDO COMPLETO\n")
	print(contenido)
	
		
	#cerramos el archivo
	archivo.close()
	"""
	"""
	#############################################################################
	#             lectura de una o varias líneas de un archivo readline()
	#############################################################################
	
	#abrimos el archivo
	try:
		archivo=open("ficheroTexto1.txt")
	except FileNotFoundError:
	    print("Archivo no encontrado")
	    
	    
	print('IMPRIMIMOS SOLO UNA LÍNEA CON READLINE()')
	linea=archivo.readline()
	print(linea)
	print('IMPRIMIMOS SOLO 3 CARACTERES CON READLINE()')
	linea=archivo.readline(3)
	print(linea)
	
	archivo.seek(0) #nos situamos al principio
	print("ARCHIVO COMPLETO USANDO EOF()")
	
	linea=archivo.readline()
	while not linea=="":
		print(linea)
		linea=archivo.readline()
	
	archivo.close()
	
	"""
	#############################################################################
	#             lectura del archivo completo en una lista readlines()
	#############################################################################
	
	#abrimos el archivo
	try:
		archivo=open("ficheroTexto1.txt")
	except FileNotFoundError:
	    print("Archivo no encontrado")
	
	#usamos el método readlines() que devolverá todo el contenido en una lista
	contenido=archivo.readlines()
	for elemento in contenido:
		print(elemento)
	print("\n CONTENIDO USANDO UNA LISTA\n")
	print(contenido[3])
	
	#cerramos el archivo
	archivo.close()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))