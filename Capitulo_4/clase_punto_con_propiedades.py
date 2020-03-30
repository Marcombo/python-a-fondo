class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def setx(self, valor):
        raise Exception('Valor x no puede ser modificado')

    def delx(self):
        del self._x

    x = property(getx, setx, delx, 'Posición en el eje de abscisas')

    def gety(self):
        return self._y

    def sety(self, valor):
        self._y = valor

    def dely(self):
        raise Exception('El atributo y no puede ser eliminado')

    y = property(gety, sety, dely, 'Posición en el eje de ordenadas')


if __name__ == '__main__':
    p1 = Punto(1, 2)

    print(p1.x, p1.y)

    p1.x = 5

    p1.y = 8

    del p1.y
