def main(args):
    mifrase=input("Introduzca una frase simple: ")
    print("HECHO USANDO LA CARACTERÍSTICA ITERABLE:\n")
    for letra in mifrase:
        print(letra)
    print(" ")
    print("HECHO USANDO RANGE:\n")
    for letra in range(len(mifrase)):
        print(mifrase[letra])
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
