import string
import time

import functools


def temporiza(func):
    def función_interna(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        tiempo = time.time() - inicio
        print(f'Función {func.__name__} tardó {tiempo}s usando {args} y {kwargs}')
        return resultado

    return función_interna


def suma_elems(elems):
    acc = 0
    for x in elems:
        acc += x
    return acc


def convierte_formato(cad):
    lista_elems = list(cad)
    lista_final = []
    for c in lista_elems:
        elem = c.lower() if c.lower() > 'p' else c.upper()
        lista_final.append(elem)
    return ''.join(lista_final)


@temporiza
def suma_elems_decorada(elems):
    acc = 0
    for x in elems:
        acc += x
    return acc


@temporiza
def convierte_formato_decorada(cad):
    lista_elems = list(cad)
    lista_final = []
    for c in lista_elems:
        elem = c.lower() if c.lower() > 'p' else c.upper()
        lista_final.append(elem)
    return ''.join(lista_final)


@temporiza
@functools.lru_cache(maxsize=128)
def fibo_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)


if __name__ == '__main__':
    tempo_suma = temporiza(suma_elems)

    tempo_suma(range(10))
    tempo_suma([1, 236, 472, -436])

    tempo_formato = temporiza(convierte_formato)

    tempo_formato(string.ascii_letters)
    tempo_formato('En un lugar de la Mancha')

    suma_elems_decorada(range(10))
    suma_elems_decorada([1, 236, 472, -436])

    convierte_formato_decorada(string.ascii_letters)
    convierte_formato_decorada('En un lugar de la Mancha')

    fibo_recursivo(10)
