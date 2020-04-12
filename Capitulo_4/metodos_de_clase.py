class Foo(object):
    x = 10

    def __init__(self, x):
        self.x = x

    @classmethod
    def get_x_clase(cls):
        return cls.x


class Animal:

    def __init__(self, tipo, volumen, masa):
        self.tipo = tipo
        self.volumen = volumen
        self.masa = masa

    @classmethod
    def desde_str(cls, cadena):
        tipo, volumen, masa = cadena.split(',')
        return cls(tipo, volumen, masa)

    @classmethod
    def gato(cls):
        return cls('Gato', 120, 3.8)

    @classmethod
    def perro(cls):
        return cls('Perro', 500, 25.4)


if __name__ == '__main__':
    f = Foo(2)
    print(f.x)
    print(f.get_x_clase())
