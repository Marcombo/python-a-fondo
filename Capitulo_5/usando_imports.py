from json import dumps
import math
from collections import defaultdict as ddict


def funcion_erronea(a):
    import algun_modulo_no_existente
    print('Esta funcion devuelve un error')


def calculo(x):
    resultado = math.sin(x)
    res_dict = ddict(int)
    res_dict['x'] += resultado
    return res_dict


if __name__ == '__main__':
    valor = 0
    for x in range(5):
        res_dict = calculo(x + 1)
        valor += res_dict['x']
        print(dumps(res_dict))
    print(f'El valor final es: {valor}')
