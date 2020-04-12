class Animal:
    def __init__(self, tipo, volumen, masa):
        self.tipo = tipo
        self.volumen = volumen
        self.masa = masa

    @classmethod
    def desde_str(cls, cadena):
        tipo, volumen, masa = cadena.split(',')
        return cls(tipo, float(volumen), float(masa))

    @classmethod
    def gato(cls):
        return cls('Gato', 120, 3.8)

    @classmethod
    def perro(cls):
        return cls('Perro', 500, 25.4)

    def peso(self):
        return self.masa * self.gravedad()

    @staticmethod
    def gravedad():
        return 9.8


if __name__ == '__main__':
    cebra = Animal('Cebra', 15000, 150)
    elefante = Animal.desde_str('Elefante,300000,2600')
    gato = Animal.gato()
    perro = Animal.perro()
    print(type(cebra), type(elefante), type(gato), type(perro))

    print(Animal.gravedad())
    print(elefante.peso())
