import re

def es_correo_electronico(cadena):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, cadena))

# Programa que usa la función es_correo_electronico
if __name__ == "__main__":
    correos = [
        "ejemplo@dominio.com",
        "ejemplo.dominio.com",
        "ejemplo@dominio",
        "ejemplo@dominio.c",
        "@dominio.com"
    ]
    
    for correo in correos:
        if es_correo_electronico(correo):
            print(f"'{correo}' es un correo electrónico válido.")
        else:
            print(f"'{correo}' no es un correo electrónico válido.")
