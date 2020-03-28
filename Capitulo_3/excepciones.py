def busca_elemento_simple(obj, indice_o_clave):
    return obj[indice_o_clave]


def busca_elemento(obj, indice_o_clave):
    try:
        return obj[indice_o_clave]
    except IndexError:
        print(f'Índice "{indice_o_clave}" utilizado no accesible')
    except KeyError:
        print(f'Clave "{indice_o_clave}" utilizada no encontrada')
    except Exception as e:  # cualquier tipo de excepción
        print(f'Excepción inesperada "{e}"')
        return -1


def capitalizar(elem):
    return elem.capitalize()


def formatea(elem):
    limpio = elem.trim()
    capitalizado = capitalizar(limpio)
    return capitalizado


def formateador(elementos):
    resultado = []
    for elem in elementos:
        resultado.append(formatea(elem))


def elevando_excepciones():
    while True:
        valor = int(input('Introduzca un número entero positivo: '))
        if valor < 0:
            raise ValueError(f'El número introducido {valor} no es positivo')
        else:
            print(valor)


if __name__ == '__main__':
    print(formateador(' Jose '))
    print(formateador(2))

    obj = [1, 2, 3]
    print(busca_elemento(obj, 2))
    print(busca_elemento(obj, 90))

    obj = dict(color='Verde', tipo='coche')
    print(busca_elemento(obj, 'color'))
    print(busca_elemento(obj, 'marca'))

    busca_elemento({1, 2, 3}, 'pepe')

    try:
        while True:
            res = int(input('Introduzca un número: '))
            print(f'El cuadrado de ese número es {res**2}')
    except KeyboardInterrupt:
        print('Finalizando programa, gracias')
