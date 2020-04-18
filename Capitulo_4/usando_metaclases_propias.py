class MetaclaseAnimal(type):
    def __new__(mcs, name, bases, attrs):
        if 'alas' not in attrs and 'aletas' not in attrs and 'patas' not in attrs:
            attrs['patas'] = 2
        if 'alas' in attrs and 'aletas' in attrs and 'patas' in attrs:
            raise TypeError(f'Clase "{name}" no puede definir alas, aletas y patas a la vez')
        return super(MetaclaseAnimal, mcs).__new__(mcs, name, bases, attrs)


class Animal(metaclass=MetaclaseAnimal):
    pass


class Gato(Animal):
    patas = 4


class Pato(Animal):
    pass


if __name__ == '__main__':
    g = Gato()
    p = Pato()
    print(f'Patas de un pato: {p.patas}')


    class Engendro(Animal):
        patas = 7
        alas = 3
        aletas = 4


    e = Engendro()
