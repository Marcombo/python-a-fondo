def range_personal(inicio, fin, paso=1):
    final = inicio
    while final < fin:
        yield final
        final += paso


def fibo_generador():
    previo = 0
    actual = 1
    yield 0
    while True:
        yield actual
        previo, actual = actual, actual + previo


if __name__ == '__main__':
    fibo_f = fibo_generador()
    print(f'Los 15 primeros elementos de fibo: {[next(fibo_f) for _ in range(15)]}')

    print(f'Range personal: {list(range_personal(0, 20, 3))}')
