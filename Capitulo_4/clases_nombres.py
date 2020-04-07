"""Ejemplo de una clase haciendo uso de __slots__"""


class Foo:
    _atributo_cls_protegido = 0
    __atributo_cls_privado = 0

    def __init__(self, x):
        self.x = x
        self._x = x * 2
        self.__x = x * 3

    def obtener_x(self):
        return self.x

    def obtener_x_protegida(self):
        return self._x

    def obtener_x_privada(self):
        return self.__x


if __name__ == '__main__':
    f = Foo(2)
    print(dir(f))
    print(f.x)
    print(f._x)
    print(f.__x)
    print(f._Foo__x)

    print(Foo._atributo_cls_protegido)
    print(Foo.__atributo_cls_privado)
    print(Foo._Foo__atributo_cls_privado)
