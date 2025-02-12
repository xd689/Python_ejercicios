def main(args):
    import os
    print(os.getcwd())

    if os.name=='posix':
        ruta='/home/usuario/'
    else:
        ruta='c:/User'
    
    if(os.access(ruta,os.F_OK)):
        print("El directorio existe")

    if(os.access(ruta,os.F_OK) and os.access(ruta,os.W_OK)):
        print("El directorio existe y es writeable")

    os.chdir(ruta)
    print(os.getcwd())

    print(os.listdir())
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)