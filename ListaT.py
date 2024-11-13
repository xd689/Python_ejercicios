def main(args):
    x = ("@2asir.net","192.168.1.1")
    l=list()
    for i in range(20,31):
        l.append("usuario"+str(i)+x[0])   
        l.append("192.168.1."+str(i))
    print(l)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))