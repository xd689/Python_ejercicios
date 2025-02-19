import csv
def main(args):

# Datos que queremos escribir en el CSV
    datos = [
        ["Nombre", "Edad", "Ciudad"],
        ["Juan", "28", "Madrid"],
        ["Ana", "34", "Barcelona"],
        ["Luis", "45", "Valencia"]
    ]

# Nombre del archivo CSV
    archivo = "write_me.csv"

# Escribir en el archivo CSV
    with open(archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)

    print(f"Los datos han sido escritos en el archivo write_me.csv")
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)