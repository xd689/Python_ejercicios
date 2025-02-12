def Crealineas(registros):
	i=0
	linea = []
	for i in range(len(registros)):
		lineaC = registros[i][0]+" "+registros[i][1]+" "+registros[i][2]+" "+registros[i][3]+" "+registros[i][4]
		linea.append(lineaC)
	return[linea]

def main(args):
# Datos a tratar
	registros = [
					("iface eth0", "inet static", "address 192.168.1.1", "netmask 255.255.255.0", "gateway 192.168.1.254"),
					("iface eth1", "inet static", "address 192.168.1.2", "netmask 255.255.255.0", "gateway 192.168.1.254")
				]

# Uso de las funciones
	lineas = Crealineas(registros)
	print("Contenido /etc/networks/interfaces:\n")
	for linea in lineas:
		print(linea)

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
