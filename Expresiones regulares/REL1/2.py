import re
import sys
import argparse
def contarFechas(texto):
    patron = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    fechas = re.findall(patron, texto)
    return len(fechas)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("texto", type=str)
    args = parser.parse_args()
    texto = args.texto
    numFechas = contarFechas(texto)
    print(f"Hay {numFechas} fechas en el texto")
    #"12-10-2022, 12-102022, 1210-2022, 12102022, 2022-10-12, 12/12/2023"