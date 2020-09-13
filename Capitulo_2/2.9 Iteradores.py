import random
import string


class MiRange:
    def __init__(self, num_max):
        self.num_max = num_max
        self.num_actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_actual < self.num_max:
            n = self.num_actual
            self.num_actual += 1
            return n
        else:
            raise StopIteration()


class IteradorPersonalizado:
    def __init__(self, max_elementos, opciones=string.ascii_letters):
        self.max_elementos = max_elementos
        self.indice_iterador = 0
        self.opciones = opciones

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice_iterador >= self.max_elementos:
            raise StopIteration()
        else:
            self.indice_iterador += 1
            return random.choice(self.opciones)


class IteradorFibonacci:
    def __init__(self):
        self.idx = 2
        self.v_previo = 0  # Primer valor
        self.v_actual = 1  # Segundo valor

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        v_previo = self.v_previo  # Guardado el valor previo temporalmente
        self.v_previo = self.v_actual
        self.v_actual = self.v_actual + v_previo
        return self.idx, self.v_actual


class IteradorAleatorioInfinito:
    def __init__(self, num_elementos):
        self.elementos = range(num_elementos)

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.elementos)


if __name__ == '__main__':
    num_elementos = 12
    mi_range = MiRange(num_elementos)
    for elem in mi_range:
        print(elem)

    print(list(MiRange(num_elementos)))

    num_elementos = 100
    iter_aleatorio = IteradorAleatorioInfinito(num_elementos)

    for _ in range(10):
        print(next(iter_aleatorio))

    iter_fibo = IteradorFibonacci()
    print(next(iter_fibo))
    print(next(iter_fibo))
    print(next(iter_fibo))
    print(next(iter_fibo))

    iter_fibo = IteradorFibonacci()
    valores_fibo = []
    for _ in range(10):
        valores_fibo.append(next(iter_fibo))
    print(valores_fibo)


    iter_personalizado = IteradorPersonalizado(7)
    elems = list(iter_personalizado)
    print(elems)
