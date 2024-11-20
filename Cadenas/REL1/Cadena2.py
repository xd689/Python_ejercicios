def main(args):
    frase=input("Introduce tu oracion: ")
    c=0
    for i in frase:
        if i==" ":
              c+=1
    print(c, "espacios en la oracion.")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)