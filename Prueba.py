def main(args):
    def obten_mail(user):
        email = user[3][0]  # Accede al correo completo
        username = ""
        for char in email:
            if char != '@':
                username += char
            else:
                return username

    def obten_domain(user):
        email = user[3][0]
        domain = ""
        encontrado = False
        for char in email:
            if encontrado:
                domain += char
            elif char == '@':
                encontrado = True
                domain += char
        return domain

    user = (("Diablos",), ("Desktop_12",), ("10.10.10.10",), ("diablos12@diablomail.com",))
    username = obten_mail(user)
    domain = obten_domain(user)
    print("El email es:", username + domain)  # Muestra el correo completo
    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)
