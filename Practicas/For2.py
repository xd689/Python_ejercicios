#!/usr/bin/env python

def main(args):
    numero = 0
    for i in range(1,11):
        numero += i
        print (f"De 1 a {i} la suma de todos da como resultado: {numero}")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
