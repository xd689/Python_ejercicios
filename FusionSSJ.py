def main(args):
	def menu():
		print("1. Cancelar")
		print("2. Gotenks")
		print("3. Vegetto")
		print("4. Zamas Potara")
		controlador=int(input("¿De qué fusión quieres datos?: "))
		return controlador
	controlador=menu()
	while controlador<1 or controlador>4:
		print("Elige una de las 3 fusiones disponibles.")
		controlador=menu()
	fusion=(("Goten","Trunks"),("Vegetta","Goku"),("Zamas","Goku black"))
	ssj=(("SSJ3"),("SSJ4"),("Pink SSJ"))
	for i in fusion:
		if controlador==1:
			print("Cancelando el programa de información de fusiones Saiyan...")
			return 0
		if controlador==2:
				if "Goten" in i and "Trunks" in i:
					print("La fusión Gotenks está formada por ",i[0]," y ",i[1])
					print("Puede alcanzar el estado ",ssj[0])
		if controlador==3:
				if "Vegetta" in i and "Goku" in i:
					print("La fusión Vegetto está formada por ",i[0]," y ",i[1])
					print("Puede alcanzar el estado ",ssj[1])
		if controlador==4:	
				if "Zamas" in i and "Goku black" in i:
					print("La fusión Zamas Potara está formada por ",i[0]," y ",i[1])
					print("Puede alcanzar el estado ",ssj[2])
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))