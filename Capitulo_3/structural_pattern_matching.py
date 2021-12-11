from enum import Enum


def comprobar_nombre(nombre):
    match nombre:
        case 'Oscar':
            print('Correcto!')
        case 'El Pythonista':
            print('Ha estado cerca!')
        case _:
            print('No es correcto')


class Color(Enum):
    Blue = '#0000FF'
    Red = '#FF0000'
    Yellow = '#FFFF00'

def temperatura_color(color):
    match color:
        case 'gris':
            return 'Neutro'
        case Color.Yellow | Color.Red:
            return 'Cálido'
        case Color.Blue:
            return 'Frío'
        case str(x) if int(x[1:], base=16) > 256:
            return 'Cálido'

if __name__ == '__main__':
    nombre = input('Introduzca un nombre: ')
    comprobar_nombre(nombre)

    print(temperatura_color('gris'))
    print(temperatura_color(Color.Blue))
    print(temperatura_color('#F0F022'))