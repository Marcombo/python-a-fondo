import math


class Rectangulo:
    """Clase representando la figura geométrica del rectangulo"""

    def metodo_interno(self, lado: float = 2, *, altura: float = 10):
        """Metodo interno que calcula el lado elevado por la altura"""
        variable = 0
        resultado = lado ** altura
        return resultado


def pi(decimales: int = 2) -> float:
    """Devuelve el número pi con los decimales deseados, y por defecto 2"""
    return round(math.pi, decimales)


if __name__ == '__main__':
    print(Rectangulo.__doc__)
    print(Rectangulo.metodo_interno.__qualname__)
    print(Rectangulo.metodo_interno.__defaults__)
    print(Rectangulo.metodo_interno.__kwdefaults__)
    print(Rectangulo.metodo_interno.__globals__)
    print(pi.__code__)
    print(pi.__annotations__)
