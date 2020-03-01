def foo_incorrect():
    modelo = 'coche'
    marca = 'Honda'
    ruedas = 4

    def pinchar_rueda():
        print(f'Inner ruedas: {ruedas}')
        ruedas -= 1

    print(f'Número de ruedas: {ruedas}')
    pinchar_rueda()
    print(f'Número de ruedas: {ruedas}')


def foo_correct():
    ruedas = 4
    def pinchar_rueda():
        nonlocal ruedas
        ruedas -= 1
    print(f'Número de ruedas: {ruedas}')
    pinchar_rueda()
    print(f'Número de ruedas: {ruedas}')


if __name__ == '__main__':
    foo_correct()
    foo_incorrect()
