def main(args):
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
    for i in range(1):
        s = input("what will you add: ")
        c = input(f"introduce {s} please: ")
        car.update({s : c})

    print(car)
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)