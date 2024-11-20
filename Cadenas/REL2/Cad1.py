def buscainterfaz(interfaz,linea):
    if interfaz in linea:
        return interfaz
    return 0
def main(args):
    linea="iface eth0 inet static"
    interfazabuscar="eth0"
    print(buscainterfaz(interfazabuscar,linea))
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))