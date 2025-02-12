#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import subprocess
import sys
import os

def ping_host(host, timeout=1):
    """
    Realiza un ping a un host y devuelve True si responde, False si no.
    """
    try:
        resultado = subprocess.run(
            ["ping", "-c", "1", "-W", str(timeout), host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return resultado.returncode == 0
    except Exception as e:
        print(f"Error al hacer ping a {host}: {e}")
        return False

def lee_hosts(nombrearchivo):
    """
    Lee los hosts de un archivo, ignorando líneas vacías y comentarios.
    """
    try:
        with open(nombrearchivo, "r") as file:
            hosts = [
                linea.strip() for linea in file.readlines()
                if linea.strip() and not linea.startswith("#")
            ]
        return hosts
    except FileNotFoundError:
        print(f"Error: El archivo '{nombrearchivo}' no existe.")
        sys.exit(1)
    except Exception as e:
        print(f"Error al leer el archivo '{nombrearchivo}': {e}")
        sys.exit(1)

def escribir_resultados(resultados, nombrearchivo="comprobar.txt"):
    try:
        with open(nombrearchivo, "w") as file:
            for resultado in resultados:
                file.write(resultado + "\n")
        print(f"Resultados guardados en {nombrearchivo}")
    except Exception as e:
        print(f"Error al escribir en el archivo '{nombrearchivo}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Verifica la conectividad de servidores desde un archivo.")
    parser.add_argument("--file",
                         type=str,
                         default="/etc/hosts",
                         help="Archivo que contiene los hosts o IPs a verificar (uno por línea). Por defecto usa /etc/hosts."
    )
    parser.add_argument("--timeout", 
                          type=int, 
                          default=1, 
                          help="Tiempo de espera para cada ping (en segundos)."
                        )
    
    args = parser.parse_args()
    
    print(f"Leyendo hosts desde: {args.file}")
    hosts = lee_hosts(args.file)
    
    if not hosts:
        print("No se encontraron hosts válidos en el archivo.")
        sys.exit(1)
    
    print("Verificando conectividad...")
    resultados = []
    for host in hosts:
        estado = "OK" if ping_host(host, timeout=args.timeout) else "FALLO"
        resultados.append(f"{host}: {estado}")
        print(f"{host}: {estado}")
    
    escribir_resultados(resultados)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción por el usuario.")
        sys.exit(1)
