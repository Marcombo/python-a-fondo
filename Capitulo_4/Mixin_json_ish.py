import json
from dataclasses import dataclass


class JSONISH:
    """Mixin que permite guardar en un archivo json los atributos de la instancia y sus valores"""
    json_nombre_fichero = None

    def __init__(self):
        if not self.json_nombre_fichero:
            nombres_padres = [x.__name__ for x in self.__class__.__mro__ if x.__name__ != 'object']
            nombres = '_'.join(nombres_padres)
            self.json_nombre_fichero = nombres + '.json'

    def save_json(self):
        variables = vars(self)
        json.dump(variables, open(self.json_nombre_fichero, 'wa'))


@dataclass
class Persona:
    nombre: str
    apellidos: str
    telefono: str
    edad: int

    def __post_init__(self):
        super().__init__()


@dataclass
class Piloto(Persona, JSONISH):
    equipo: str
    categoria: str


@dataclass
class PilotoParticular(Persona, JSONISH):
    equipo: str
    categoria: str
    json_nombre_fichero = 'piloto_especial.json'


if __name__ == '__main__':
    ana = Persona('Ana', 'Encabo', '+34 67584532', 54)
    ana.save_json()

    marc = Piloto(equipo='Honda', categoria='MotoGP', nombre='Marc', apellidos='Marquez', telefono='47897321', edad=28)
    marc.save_json()

    rossi = PilotoParticular(equipo='Yamaha', categoria='MotoGP', nombre='Valentino', apellidos='Rossi',
                             telefono='487392', edad=35)
    rossi.save_json()
