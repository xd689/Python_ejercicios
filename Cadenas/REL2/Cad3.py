#función que extrae una ip de una cadena que siempre está en la misma
def extraer_ip(linea):
#escribe tu código aquí
    linea=linea.split(" ")
    if linea[2]==("192.168.1.1"):
        return "Es esta."
    return "No es esta."
    
def main(args):
    linea = "eth0: inet 192.168.1.1  netmask 255.255.255.0  broadcast 192.168.1.255"
    ip=extraer_ip(linea)
    print(ip)
# El resultado esperado sería: '192.168.1.1'
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))