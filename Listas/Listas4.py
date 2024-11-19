def main(args):
    from decimal import Decimal
    from operator import itemgetter
    l = [('HLC', Decimal('10.0')), ('IAW', Decimal('2.35')), ('SAD', Decimal('8.75')), ('ASO', Decimal('9.25')), ('SRI',Decimal('6.45'))]
    ls = sorted(l, key=itemgetter(1))
    print('ASIGNATURAS INTRODUCIDAS')
    print(l)
    print(" ")
    print('ASIGNATURAS ORDENADAS POR NOTA')
    print(ls)
    print(" ")
    print('ASIGNATURAS ---- NOTAS')
    for a, n in ls:
        print(f"{a} ---- {n}")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)