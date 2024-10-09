#!/usr/bin/env python

def main(args):
	num1=int(input("Por favor, introduce un número: "))
	num2=int(input("Por favor, introduce un número: "))
	numaux=num1
	num1=num2
	num2=numaux
	
	print("Los números intercambiados son. ",num1 ,num2)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
