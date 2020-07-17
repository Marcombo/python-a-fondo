import argparse


def convierte_cadena(cadena, func):
    return getattr(str, func)(cadena)


def guarda_en_fichero(resultado, fichero_salida):
    with open(fichero_salida, 'w') as fw:
        fw.write(resultado)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Convertidor a fondo',
                                     description='Programa a convertir texto usando str desde consola, '
                                                 'por defecto el resultado se devuelve por consola')
    parser.add_argument('-m', dest='cadena', help='Cadena de caracteres a transformar', required=True)
    parser.add_argument('-f', dest='func', help='Función a realizar sobre la cadena', required=True,
                        choices=['title', 'lower', 'upper', 'split', 'splitlines', 'strip'])
    parser.add_argument('-o', type=str, help='Fichero donde escribir el contenido')
    args = parser.parse_args()
    resultado = convierte_cadena(args.cadena, args.func)
    if args.o:
        guarda_en_fichero(resultado, args.o)
    else:
        print(resultado)
