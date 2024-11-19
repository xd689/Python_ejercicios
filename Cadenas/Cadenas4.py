def main(args):
    frase=input("Introduce tu frase: ")
    a=input("Introduce el caracter que vamos a contar: ")
    c=0
    for i in frase:
        if i == a:
            c+=1
    print("Hay",c,a,"en la frase")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)