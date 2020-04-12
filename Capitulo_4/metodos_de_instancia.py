import math


class Cuadrado(object):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        """El aread del cuadrado es lado al cuadrado"""
        return self.lado ** 2

    def diagonal(self):
        """Se define como la raiz cuadrada del area multiplicada por 2"""
        return math.sqrt(self.area() * 2)


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro_punto):
        """Se define como la raiz cuadrada de los cuadrados de las diferencias"""
        xs = (self.x - otro_punto.x) ** 2
        ys = (self.y - otro_punto.y) ** 2
        return math.sqrt(xs + ys)

    def mover_x(self, cantidad):
        self.x += cantidad

    def mover_y(self, cantidad):
        self.y += cantidad


if __name__ == '__main__':
    c = Cuadrado(lado=5)
    print(c.area())
    print(c.diagonal())

    p1 = Punto(7, 5)
    p2 = Punto(4, 1)
    print(p1.distancia(p2))

    p1.mover_x(5)
    p2.mover_y(-10)
    print(p1.distancia(p2))
