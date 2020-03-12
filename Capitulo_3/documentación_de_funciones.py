def suma_pares(elems):
    """Suma los elementos pares encontrados en elems
    :param elems: lista de números a sumar
    :return integer: numero resultante de la suma de los pares
    """
    return sum(x for x in elems if not x % 2)


def cambia_tamaño(cad: str):
    "Cambia el tamaño de cada letra de la cadena cad"
    return cad.swapcase()


if __name__ == '__main__':
    print(help(suma_pares))
    print(suma_pares.__doc__)
