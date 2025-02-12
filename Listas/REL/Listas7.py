def main(args):
    from decimal import Decimal
    alu = list()
    for j in range (1,4):
        asi = list()
        for i in range(1,3):
            a = input(f"\nDame el nombre de la asignatura {i} del alumno {j}: ")
            n = Decimal(input(f"\nDame la nota para la asignatura {i} del alumno {j}: "))
            asi.append((a, n))
        alu.append(asi)
    print(f"\nASIGNATURAS")
    print("===========")
    for j in range(1, 4):
        print(f"\nAlumno {j}")
        print("========")
        for a, n in alu[j-1]:
            print(f"{a} ---- {n}")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)