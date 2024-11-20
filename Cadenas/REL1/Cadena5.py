def main(args):
    f = input("Introduce una fracción: ")
    fp = (f.split("/"))
    d = int(fp[0])
    n = int(fp[1])
    fr = d/n
    print("El resultado de la fraccion es:",fr)
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)