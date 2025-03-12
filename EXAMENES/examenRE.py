#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#################################################################################################
####    Programa que analiza un fichero de log con las conexiones a un servidor y pasa a otro  ##
####    fichero la información de las conexiones fallidas.                                    ###
#################################################################################################
#Pedro José Notario Miñano
import re
import sys
import argparse

def leer_archivo(ruta):
	## Función que lee el archivo que recibe como parámetro y devuelve una lista con las 
	## líneas de
	archivo = open(ruta, 'r')
	l = archivo.readlines()
	archivo.close
	return l

def buscar_errores(l):
	## Funcion que recibe una lista con las lineas del fichero y devuelve una lista
	## con las filas en la que hubo un acceso
	errores = []
	patron = 'granted'
	for con in l:
		if re.findall(patron, con):
			errores.append(con)
	return errores

def guardar_informe(ruta_salida, errores):
	## Función que recibe la ruta del fichero de salida y la lista de intentos denegados
	## y guarda en el fichero solamente la fecha y hora de conexión y el usuario que intentó conectar
	archivo = open(ruta_salida, 'w')
	for i in range(len(errores)):
		archivo.write(errores[i])
	print("Errores escritos.")

def main():
	## Definición de los parámetros de script (fichero origen obligatorio, fichero salida opcional)
	## Si no se proporciona fichero de salida, se guardará en "informe.txt" en la misma carpeta
	## que esté el script
	parser = argparse.ArgumentParser(description="Informe accesos denegados")
	parser.add_argument("archivo",help="Ruta del archivo a leer")
	parser.add_argument("--ruta_salida",help="Ruta del archivo de salida")
	#parser.add_argument()
	args = parser.parse_args()
	ruta = args.archivo
	l = leer_archivo(ruta)
	if args.ruta_salida:
		ruta_salida = args.ruta_salida
	else:
		ruta_salida = "informe.txt"
	errores= buscar_errores(l)
	print("Lista con las conexiones: ")
	print(l)
	print("")
	print("Lista con los errores: ")
	print(errores)
	print("")
	guardar_informe(ruta_salida, errores)
	
## Cuerpo principla. Define el patrón y llama a las funciones

if __name__ == "__main__":
	try:main()
	except KeyboardInterrupt:
		print("\nInterrupción por el usuario.")
		sys.exit(1)
#El programa se ejecuta con python3 examen.py conexiones.txt
