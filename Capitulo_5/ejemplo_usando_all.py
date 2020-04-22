from mi_modulo import *

def primera_funcion(a):
    cadena = str(a)
    return ' '.join([hola_mundo(), cadena])

if __name__ == '__main__':
    print(primera_funcion('gato'))
