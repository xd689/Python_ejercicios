def main(args):
    from decimal import Decimal
    from operator import itemgetter
    l = list()
    for i in range (1,6):
        ai=input(f"Introduce la asignatura {i}: ")
        ni=Decimal(input("Introduce la nota de esa asignatura (formato decimal por punto 0.00): "))
        l.append((ai, ni))
    ls = sorted(l, key=itemgetter(1))
    print('ASIGNATURAS ---- NOTAS')
    for a, n in ls:
        print(f"{a} ---- {n}")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)