def main(args):
    l=list()
    for i in range(1,6):
        a=input(f"Dame la asignatura {i}: ")
        l.append(a)
    print(l)
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)