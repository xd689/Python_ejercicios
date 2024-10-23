def main(args):
	def menu():
		print("1. Sumar")
		print("2. Restar")
		print("0. Salir")
		op=int(input("Operación: "))
		return op
	operacion=menu()
	while operacion<0 or operacion>2:
		print("operación no válida")
		operacion=menu()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
