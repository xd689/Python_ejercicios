def main(args):
    x = ("@2asir.net","192.168.1.1")
    l=list()
    for i in range(40,51):
        t=("usuario"+str(i)+x[0], "192.168.10."+str(i))   
        l.append(t)
    for usuario, ip in l:
        print("El usuario es: ",usuario, "La ip asignada es:",ip)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))