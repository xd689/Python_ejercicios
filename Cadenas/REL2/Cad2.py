def verificaip(ip):
   ip = input("Introduce una dirección IP: ")
   if ip == ("192.168.1.1"):
       return True
   else:
       return False
def main(args):
    print(verificaip("192.168.1.1"))
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))