import trace


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre.title()

    def info(self, *args, **kwargs):
        return f'Mi nombre es: {self.nombre}'

    def velocidad(self):
        """Velocidad media en minutos por kilometro"""
        return 8


class Atleta(Persona):
    def __init__(self, nombre, forma_fisica: float):
        super(Atleta, self).__init__(nombre)
        self.forma_fisica = forma_fisica

    def info(self, *args, **kwargs):
        p_info = super(Atleta, self).info(*args, **kwargs)
        return f'{p_info} y soy atleta profesional'

    def velocidad(self):
        p_vel = super(Atleta, self).velocidad()
        return p_vel * (1 + self.forma_fisica / 10)


class Pintor(Persona):
    def info(self, *args, **kwargs):
        p_info = super(Pintor, self).info(*args, **kwargs)
        return f'{p_info} y soy Artista'

    def pintar(self):
        lineas = []
        for vals in ([9556, 9552, 9552, 9559], [9553, 9630, 9626, 9553], [9562, 9552, 9552, 9565]):
            lineas.append(''.join(map(chr, vals)))
        return '\n'.join(lineas)


class PersonaPintorAtleta(Atleta, Pintor):
    pass


class PintorRapido(Pintor):
    def info(self, *args, **kwargs):
        p_info = super(Pintor, self).info(*args, **kwargs)
        return f'{p_info} y soy pintor rápido'

    def velocidad(self):
        vel = super(PintorRapido, self).velocidad()
        return vel + 2


class PersonaPintorRAtleta(PintorRapido, Atleta):
    pass


class PersonaAtletaPintorR(Atleta, PintorRapido):
    pass


def main():
    ppra = PersonaPintorRAtleta('juana de arco', forma_fisica=45)
    print(f'Velocidad de PersonaPintorRAtleta: {ppra.velocidad()}')

    papr = PersonaAtletaPintorR('francisco gonzalez', forma_fisica=45)
    print(f'Velocidad de PersonaAtletaPintorR: {papr.velocidad()}')


if __name__ == '__main__':
    tracer = trace.Trace()
    tracer.run('main()')
