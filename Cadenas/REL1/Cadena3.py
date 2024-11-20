def main(args):
    f = "Me corro"
    df = len(f)
    df = f[::-1]
    print("La cadena inversa por corte es: ",df)
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)