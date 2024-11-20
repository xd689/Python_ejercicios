from decimal import Decimal

def matriz():
    n = list()
    for i in range(0,3):
        f = list()
        for j in range(0,3):
            c = int(input(f"Dame el valor de la posicion {i, j} de la matriz: "))
            f.append(c)
        n.append(f)
    return n

def suma(m1,m2):
    n1 = list()
    for i in range(0,3):
        f1 = list()
        for j in range(0,3):
            c1 = m1[i][j]+m2[i][j]
            f1.append(c1)
        n1.append(f1)
    return n1

def main(args):
    m1 = matriz()
    m2 = matriz()
    sum = suma(m1,m2)
    print(sum)
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)