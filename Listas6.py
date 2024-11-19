def main(args):
    from decimal import Decimal
    asignaturas = list()
    for i in range(1,6):
        asignatura = input(f"Dame la asignatura {i}: ")
        nota = Decimal(input(f"Dame la nota para {asignatura}: "))
        asignaturas.append((asignatura, nota))
    asignaturas_suspensas = [a for a in asignaturas if a[1] < Decimal('5.0')]
    print("\nASIGNATURAS SUSPENSAS")
    print("=====================")
    for asignatura, nota in asignaturas_suspensas:
        print(f"{asignatura}: {nota}")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)