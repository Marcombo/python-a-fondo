from collections import Counter, defaultdict

from modelos import Estadisticas


def obtener_estadisticas(ruta_a_fichero: str) -> Estadisticas:
    """Obtiene las estadisticas del fichero analizado en un objeto Stats"""
    num_lineas, num_palabras, num_caracteres = 0, 0, 0
    letras = defaultdict(int)
    with open(ruta_a_fichero, 'r') as fr:
        for line in fr.readlines():
            num_lineas += 1
            palabras = len(line.split())
            num_palabras += palabras
            num_caracteres += len(line)
            for k, v in Counter(line.lower()).items():
                letras[k] += v

    return Estadisticas(num_lineas, num_palabras, num_caracteres, letras)


def obetener_texto(ruta_a_fichero: str) -> str:
    """Devuelve el texto que contiene el fichero"""
    with open(ruta_a_fichero, 'r') as fr:
        return fr.read()
