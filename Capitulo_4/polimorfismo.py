class FormateadorMayus:
    def formatea(self, cadena):
        return cadena.upper()


class FormateadorMinus:
    def formatea(self, cadena):
        return cadena.lower()


def formatear(obj, cadena):
    return obj.formatea(cadena)


class NumeroDecimal:
    def __init__(self, num_original):
        self._num = num_original
    def numero(self):
        return self._num


class NumBinario(NumeroDecimal):
    def numero(self):
        return bin(self._num)


class Hexadecimal(NumeroDecimal):
    def numero(self):
        return hex(self._num)


if __name__ == '__main__':
f_mayus = FormateadorMayus()
f_minus = FormateadorMinus()
print(formatear(f_mayus, 'El Perro CoRre'))
print(formatear(f_minus, 'El Perro CoRre'))

b = NumBinario(78)
h = Hexadecimal(78)
print(b.numero())
print(h.numero())
