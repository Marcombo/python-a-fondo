from dataclasses import dataclass


@dataclass
class Estadisticas:
    num_lineas: int
    num_palabras: int
    num_caracteres: int
    letras: dict