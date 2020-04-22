import re
from dataclasses import dataclass

from Constantes import MARCAS_DE_COCHES, FORMATOS_Y_TIPOS


@dataclass
class Coche:
    marca: str
    modelo: str
    num_puertas: str

    def __post_init__(self):
        f_cadenas = Formateador('Formateador de cadenas', FORMATOS_Y_TIPOS[str])
        self.marca = f_cadenas.comprueba_valor(self.marca)
        self.modelo = f_cadenas.comprueba_valor(self.modelo)

        f_int = Formateador('Formateador de enteros', FORMATOS_Y_TIPOS[int])
        self.num_puertas = f_int.comprueba_valor(self.num_puertas)

        if self.marca.upper() not in MARCAS_DE_COCHES:
            raise ValueError('Marca de coche no disponible')


@dataclass
class Formateador:
    nombre: str
    regex: str

    def comprueba_valor(self, valor):
        matches = re.match(self.regex, valor)
        if not matches:
            raise ValueError(f'Valor incorrecto "{valor}" usando formateador {self.nombre}')
        else:
            return matches[0]


if __name__ == '__main__':
    while True:
        try:
            marca_coche = input('Introduzca la marca del coche: ')
            modelo_coche = input('Introduzca el modelo del coche: ')
            num_puertas = input('Introduzca el número de puertas: ')

            c = Coche(marca_coche, modelo_coche, num_puertas)
            print(f'El coche definido es: {c}')
        except ValueError as e:
            print(f'Error: {e}')
        except KeyboardInterrupt:
            print('Finalizando programa')
            break
        print()
