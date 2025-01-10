def main(args):
    l = ['ER MARDITO DIABLO.\n', 'LOCURA LOCO ER HUESO.\n', 'BALBARO.\n']
    with open('/home/usuario/ficheroTexto1.txt', 'w') as f:
        f.writelines(l)
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)