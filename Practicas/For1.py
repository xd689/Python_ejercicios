def main(args):
    numero = int(1)
    for numero in range(0,10):
        numero = numero+1
        print (numero)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
