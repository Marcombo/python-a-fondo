import time


def es_palindromo(cadena):
    punto_medio = len(cadena) // 2 + 1
    for i in range(punto_medio):
        i_fin = - (i + 1)
        if cadena[i] != cadena[i_fin]:
            return False
    return True


def funcion_sin_usar():
    return time.time()
