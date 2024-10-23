def main(args):
    n= int(input("Introduce un número entero positivo: "))
    if n < 2:
        es_primo = True
    else:
        for bcl in range(2, int(n*0.5)+1):
           if n%bcl == 0:
               es_primo = False
               break
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
