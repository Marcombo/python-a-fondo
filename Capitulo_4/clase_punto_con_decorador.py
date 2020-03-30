class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        """Posición en el eje de abscisas"""
        return self._x

    @x.deleter
    def x(self):
        del self._x

    @property
    def y(self):
        """El atributo y no puede ser eliminado"""
        return self._y

    @y.setter
    def y(self, valor):
        self._y = valor


if __name__ == '__main__':
    p1 = Punto(1, 2)

    print(p1.x, p1.y)

    p1.x = 5

    p1.y = 8

    del p1.y
