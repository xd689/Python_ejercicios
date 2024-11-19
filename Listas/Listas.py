def main(args):
    l=list()
    l.append("ñemaso")
    l.append("huesaso")
    l.append("jueputa")
    print(l)
    print("Sos un", l[0], "pedaso de", l[2], "mamame el", l[1])
    for i in l:
        print(i)
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)