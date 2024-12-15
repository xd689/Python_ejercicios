from decimal import Decimal
def creaServ(s):
    n = int(input("¿Cuantos servidores quieres crear?: "))
    for i in range(n):
        ns = input("Dime el nombre del servidor: ")
        serv = []
        n1 = int(input(f"¿Cuantos servicios tiene {ns}?: "))
        for j in range(n1):
            j += 1
            nServ = input(f"Dime el nombre del servicio {j} de {ns}: ")
            n2 = int(input(f"¿Cuantas instancias tiene el servicio {nServ}?: "))
            for k in range(n2):
                k += 1
                numS = Decimal(input(f"Dime cuanto consume la instancia {k} del servicio {nServ}: "))
                serv.append(numS)
                s[ns] = {
                    nServ:serv
                    }
    return(s)


def main(args):
    s = {}
    creaServ(s)
    print(s)
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)
