#!/usr/bin/env python

def main(args):
	num1=int(input("Por favor, introduce un número: "))
	num2=int(input("Por favor, introduce un número: "))
	resultado=num1-num2
	print("El resultado de la restares es: ",resultado)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

