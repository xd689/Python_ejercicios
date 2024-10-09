#!/usr/bin/env python

def main(args):
    numero = int(0)
    numero2 = numero 
    for numero in range(0,10):
        numero = numero+1
        numero2 = numero2 + numero
        print (numero,"la suma de todos da como resultado: ",numero2)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
