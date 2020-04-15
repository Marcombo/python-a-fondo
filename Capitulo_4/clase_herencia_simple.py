class MiStr:
    def __init__(self, cadena):
        self.cadena = cadena

    def longitud(self):
        return len(self.cadena)

    def info(self):
        return self.cadena


class MiStrMayus(MiStr):
    def info(self):
        return self.cadena.upper()


class MiStrMinus(MiStr):
    def info(self):
        return self.cadena.lower()


if __name__ == '__main__':
    m_str = MiStr('Hola Mundo')
    print(m_str.longitud())
    print(m_str.info())
    m_str_mayus = MiStrMayus('Hola Mundo')
    print(m_str_mayus.longitud())
    print(m_str_mayus.info())
    m_str_minus = MiStrMinus('Hola Mundo')
    print(m_str_minus.info())
