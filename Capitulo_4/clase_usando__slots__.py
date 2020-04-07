"""Ejemplo de una clase haciendo uso de __slots__"""


class Punto3D:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == '__main__':
    p = Punto3D(1, 2, 3)
    print(p.x)
    print(p.z)
    print(p.__dict__)
    p.nuevo_atributo = 4
