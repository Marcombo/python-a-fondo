from dataclasses import dataclass, field, asdict


class MiNumero:
    def __init__(self, valor=0.0):
        self.valor = valor

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.valor == other.valor
        return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return self.valor > other.valor
        return NotImplemented

    def __repr__(self):
        return f'MiNumero({self.valor})'


@dataclass(order=True)
class MiNumeroDC:
    valor: float = 0


class Resultado:
    def __init__(self, nombre, puntos, acumulado=0):
        self.nombre = nombre
        self.puntos = puntos
        self.total = puntos + acumulado

    def __gt__(self, other):
        return self.puntos > other.puntos

    def __eq__(self, other):
        return self.puntos == other.puntos


@dataclass
class ResultadoDC:
    nombre: str = field(compare=False)
    puntos: float = field(compare=True)
    acumulado: float = field(repr=False, default=0.0)
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.puntos + self.acumulado


if __name__ == '__main__':
    np = namedtuple('Punto', 'x y z def', rename=True, defaults=(0, 1))
    p1 = np(1, 4)
    print(p1._fields)
    print(p1.x, p1.y, p1.z, p1._3)
    print(p1._fields_defaults)
    print(p1._asdict())
    p1 = p1._replace(x=54, y=452)
    print(p1._asdict())

    rectangulos = [(3, 5), (1, 3), (45, 26)]
    for rec in rectangulos:
        i = Info(*rec)
        print(f'base: {i.base} alt: {i.altura} area: {i.area}cm^2 perimetro: {i.perimetro}cm')
