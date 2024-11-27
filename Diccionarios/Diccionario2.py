def meterDatos():
    contadol=int(input("Cuantos jueguitos quieres añadir: "))
    sexy={}
    for i  in range(contadol):
        game = input("Dime el titulaso: ")
        pub = input("Dime la publicadora: ")
        dev = input("Dime el desarrolador: ")
        sexy.update(f"{game,pub,dev}")
        print(sexy)

def mostrarDatos(datos):
    for servidor in datos:
        print(servidor)
    #
    for servidor in datos:
        print(f"{servidor}--->{datos[servidor]}")
    #
    for servidor in datos:
        print(f"{servidor}")
        for dato in datos[servidor]:
            print(f"\t{dato}--->{datos[servidor][dato]}")
    #
    for servidor in datos:
        print(f"{servidor}")
        for clave,valor in datos[servidor].items():
            if clave == 'DNS':
                for a in valor:
                    print(a)
    #
    for servidor in datos:
        print(f"{servidor}")
        for clave,valor in datos[servidor].items():
            if clave != 'DNS':
                print(f"\t{clave}--->{valor}")
            else:
                for a in valor:
                    print(f"DNS--->{a}")        

def main(args):
    datos={
        'Serv1':{
            "ip":"192.168.8.1",
            "mask":"255.255.255.0",
            "gateway":"192.168.8.1",
            "DNS":["1.1.1.1","8.8.8.8"]
        },
        'Serv2':{
            "ip":"192.168.8.2",
            "mask":"255.255.255.0",
            "gateway":"192.168.8.1",
            "DNS":["1.1.1.1","8.8.8.8"]
    }        
    }
    meterDatos()
    mostrarDatos(datos)
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)