from Capitulo_4.clase_herencia_v2 import Atleta, Pintor, Persona


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


if __name__ == '__main__':
    ppra = PersonaPintorRAtleta('juana de arco', forma_fisica=45)
    print(f'Info de PersonaPintorRAtleta: {ppra.info()}')


    #pap = PersonaPintorAtleta('juan gonzalez', forma_fisica=8)
    #print(pap.velocidad())
   # #print(pap.info())
    #print(pap.pintar())
    #print(PersonaPintorAtleta.__mro__)
#
    #print(f'Velocidad de PersonaPintorRAtleta: {ppra.velocidad()}')
    #papr = PersonaAtletaPintorR('francisco gonzalez', forma_fisica=45)
    #print(f'info de PersonaAtletaPintorR: {papr.info()}')
    #print(f'Velocidad de PersonaAtletaPintorR: {papr.velocidad()}')
    #print(PersonaPintorRAtleta.__mro__)
    #print(PersonaAtletaPintorR.__mro__)
