def main(args):
	import random
	numero_secreto = random.randint(1, 100)
	print(numero_secreto)
	print("¡Bienvenido al juego de adivinanza de números!")
	i = int(1)
	contador = 0
	while contador != numero_secreto:
		contador = int(input("Introduce tu número: "))
		if contador > numero_secreto:
			i += 1
			print ("El número es menor.")
		elif contador < numero_secreto:
			i += 1
			print ("El número es mayor.")
		else:
			print("¡Felicidades! Has adivinado el número en", i,"intentos.")
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
