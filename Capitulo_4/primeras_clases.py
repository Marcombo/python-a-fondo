class Coche:
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo


class Gato:
    num_patas = 4
    orejas = 2
    nombres = []

    def __init__(self, nombre):
        self.nombre = nombre
        self.nombres.append(nombre)


if __name__ == '__main__':
    garfield = Gato('Garfield')
    bigotes = Gato('Bigotes')
    print(garfield.num_patas)
    print(bigotes.num_patas)
    bigotes.orejas = 1
    print(garfield.orejas)
    print(bigotes.orejas)

    print(Gato.nombres)
    print(Gato.orejas)
    print(Gato.num_patas)
    print(bigotes.nombres)
