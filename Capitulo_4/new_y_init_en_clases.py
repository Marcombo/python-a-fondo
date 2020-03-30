class Corredor():
    __numeros_usados = set()

    def __new__(cls, nombre, num=1):
        while num in cls.__numeros_usados:
            num += 1
        cls.__numeros_usados.add(num)
        instancia = super(Corredor, cls).__new__(cls)
        instancia.__init__(nombre)
        instancia.num = num
        return instancia

    def __init__(self, nombre):
        self.nombre = nombre

    def __del__(self):
        self.__numeros_usados.remove(self.num)


class Finalista:
    __finalizados = 0

    def __new__(cls, corredor):
        cls.__finalizados += 1
        puesto = cls.__finalizados
        instancia = super(Finalista, cls).__new__(cls)
        instancia.__init__(corredor)
        instancia._posicion = puesto
        return instancia

    def __init__(self, corredor):
        self.corredor = corredor

    @property
    def posicion(self):
        """Posición en que el corredor finalizó la carrera"""
        return self._posicion


if __name__ == '__main__':
    juan = Corredor('Juan')
    ana = Corredor('Ana')
    maria = Corredor('Maria')

    print(juan.num)
    print(maria.num)
    print(ana.num)

    del ana

    antonio = Corredor('Antonio')
    print(antonio.num)

    print(Corredor._Corredor__numeros_usados)

    maria_finalista = Finalista(maria)
    juan_finalista = Finalista(juan)

    print(maria_finalista.puesto, juan_finalista.puesto)

    juan_finalista.puesto = 1
