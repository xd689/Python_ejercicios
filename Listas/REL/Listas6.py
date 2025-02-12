def main(args):
    from decimal import Decimal
    asi = list()
    for i in range(1,6):
        a = input(f"Dame la asignatura {i}: ")
        n = Decimal(input(f"Dame la nota para {a}: "))
        asi.append((a, n))
    asp = [a for a in asi if a[1] < Decimal('5.0')]
    print("\nASIGNATURAS SUSPENSAS")
    print("=====================")
    for a, n in asp:
        print(f"{a} ---- {n}")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)