# -*- coding: utf-8 -*-
import math


def hola_mundo():
    print('Hola Mundo')


def calcular_raiz_cuadrada(num):
    return math.sqrt(num)


def función_principal(longitud):
    hola_mundo()
    print([x * 2 for x in range(longitud)])
    while True:
        num = float(input('Introduzca un número: '))
        res = calcular_raiz_cuadrada(num)
        print(f'La raiz cuadrada de {num} es {res}')


if __name__ == '__main__':
    función_principal(10)
