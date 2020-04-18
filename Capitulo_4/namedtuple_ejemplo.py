from collections import namedtuple


class Info(namedtuple('Rectangulo', 'base altura')):
    @property
    def perimetro(self):
        return 2 * self.base + 2 * self.altura

    @property
    def area(self):
        return self.base + self.altura


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
