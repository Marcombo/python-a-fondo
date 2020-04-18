class Animal:
    pass


class Gato(Animal):
    """Clase que representa un Gato"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 100

    def comer(self):
        self.hambre -= 5


def f_init(self, nombre):
    self.nombre = nombre
    self.hambre = 100


def comer(self):
    self.hambre -= 5


GatoT = type('Gato', (Animal,), {'__doc__': """Clase que representa un Gato""",
                                 '__init__': f_init,
                                 'comer': comer})

if __name__ == '__main__':
    g1 = Gato('felix')
    print(type(g1))
    print(g1.__doc__)
    print(Gato.__mro__)
    print(dir(g1))
    g2 = GatoT('tom')
    print(type(g2))
    print(g2.__doc__)
    print(GatoT.__mro__)
    print(dir(g2))
