def creaServ():
    s = {}
    n = int(input("¿Cuantos servidores quieres crear?: "))
    for i in range(n):
        ns = input("Dime el nombre del servidor: ")
        serv = []
        n1 = int(input(f"¿Cuantos servicios tiene {ns}?: "))
        for j in range(n1):
            nServ = input(f"Dime el nombre del servicio {j} de {ns}: ")
            serv.append(nServ)
        s.update({ns:{"Servicio":nServ}})
    print(s)
    return(s)


def main(args):
    creaServ()
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)
