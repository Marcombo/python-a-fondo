class Planta:
    def __init__(self, nombre, tipo, altura):
        self.nombre = nombre
        self.tipo = tipo
        self.altura = altura

    def __eq__(self, otra_planta):
        return self.tipo == self.tipo

    def __gt__(self, otra_planta):
        return self.altura > otra_planta.altura

    def __ge__(self, otra_planta):
        return self.altura >= otra_planta.altura


if __name__ == '__main__':
    camelia = Planta('Camelia', 'Arbusto', 2)
    celindo = Planta('Celindo', 'Arbusto', 5)
    pino = Planta('Pino', 'Árbol', 9)

    print(camelia == celindo)
    print(camelia == pino)

    print(camelia > celindo)
    print(camelia < pino)
