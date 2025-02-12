def main(args):
    from decimal import Decimal
    l=[('HLC', Decimal('10.0')), ('IAW', Decimal('2.35')), ('SAD', Decimal('8.75')), ('ASO', Decimal('9.25'))]
    print('====ASIGNATURAS INTRODUCIDAS====')
    print(l[0])
    print(l[1])
    print(l[2])
    print(l[3])
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)