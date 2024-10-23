def main(args):
	fusion=(("Goten","Trunks"),("Vegetta","Goku"),("Zamas","Goku black"))
	ssj=(("SSJ3"),("SSJ4"),("Pink SSJ"))
	for i in fusion:
		if "Goten" in i and "Trunks" in i:
			print("La fusión Gotenks está formada por ",i[0]," y ",i[1])
			print("Puede alcanzar el estado ",ssj[0])
			print("")
		if "Vegetta" in i and "Goku" in i:
			print("La fusión Vegetto está formada por ",i[0]," y ",i[1])
			print("Puede alcanzar el estado ",ssj[1])
			print("")
		if "Zamas" in i and "Goku black" in i:
			print("La fusión Zamas Potara está formada por ",i[0]," y ",i[1])
			print("Puede alcanzar el estado ",ssj[2])
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
