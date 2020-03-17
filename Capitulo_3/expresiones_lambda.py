"""Ejemplos de uso de expresiones lambda en diferentes casos"""


# simple función identidad
def identidad(x):
    return x


lambda x: x

# Llamada de funciones anónimas directamente
print(f'Llamada directa a función anonima: {(lambda x: x + 5)(10)}')

# Creación de variables como funciones
f_x3 = lambda x: x * 3
print(f'Función en variable f_x3(10): {f_x3(10)}')
print(f'Función en variable f_x3(45): {f_x3(45)}')

f_resta = lambda x, y: x - y if x > 0 else y - x
print(f'función especial resta(5, 10): {f_resta(5, 10)}')
print(f'función especial f_resta(-50, 10): {f_resta(-50, 10)}')


# creación de funciones parciales
def f_principal(n):
    return lambda x: x * n


multi_5 = f_principal(5)
multi_8 = f_principal(8)
print(f'Funcion parcial multi_5(10): {multi_5(10)}')
print(f'Funcion parcial multi_8(7): {multi_8(7)}')

# Ordenación de listas


# Uso como parámetros en funciones
