def main(args):
    x = ("@2asir.net","192.168.1.1")
    l=list()
    for i in range(1,3):
        n = input("Introduce nombre de usuario: ")
        a1 = input("Introduce el primer apellido del usuario: ")
        a2 = input("Introduce el segundo apellido del usuario: ")
        s = n.casefold()
        s1 = a1.casefold()
        s2 = a2.casefold()
        user=s1[0:2]+s2[0:2]+s[0:2]
        t=(n+", "+a1+", "+a2+", ", user+"_aliesma2324"+x[0], "192.168.10."+str(i))
        l.append(t)
    for n, user, ip in l:
        print("El usuario es: ",user, "La ip asignada es:",ip)
        print("El nombre completo es: ",n)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))