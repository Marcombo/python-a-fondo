import random
import time
from time import sleep


def activar_medidor(minimo, maximo):
    """Esta función simula que en un caso real se conectaría con el sistema, bases de datos,
    utilizaría protocolos de conexión, intercambio de información, etc"""
    valor_medio = (minimo + maximo) / 2
    sleep(10)
    print('Medidor activado')
    return valor_medio


def desactivar_medidor():
    """Esta función simula el tiempo empleado en desmantelar el sistema de comprobación"""
    sleep(5)
    print('Medidor desactivado')
    return True


def valor_presion_actual(minimo=1, maximo=100):
    return random.choice(range(minimo, maximo))


def función_comprobar_presion(valor_a_probar, minimo=1, maximo=100):
    valor_medio = activar_medidor(minimo, maximo)
    if valor_a_probar > valor_medio:
        print(f'La presión es alta {valor_a_probar}')
    if valor_a_probar < valor_medio:
        print(f'La presión es baja {valor_a_probar}')
    if valor_a_probar == valor_medio:
        print(f'La presión es normal {valor_a_probar}')
    desactivar_medidor()


def corrutina_comprobar_presion(minimo=1, maximo=100):
    valor_medio = activar_medidor(minimo, maximo)
    try:
        while True:
            valor_a_probar = yield 'Corrutina inicializada'
            if valor_a_probar > valor_medio:
                print(f'La presión es alta {valor_a_probar}')
            if valor_a_probar < valor_medio:
                print(f'La presión es baja {valor_a_probar}')
            if valor_a_probar == valor_medio:
                print(f'La presión es normal {valor_a_probar}')
    except KeyboardInterrupt:
        desactivar_medidor()
        yield True
    except GeneratorExit:
        desactivar_medidor()


def coroutina(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr

    return start


def generador_numeros(n):
    for x in range(n):
        yield x


def listas_de_numeros(num):
    for n_elems in range(num):
        a = yield from generador_numeros(n_elems)
        print(f'Enviada lista de {n_elems} números')


def aplanar(lst):
    for elem in lst:
        if isinstance(elem, list):
            yield from aplanar(elem)
        else:
            yield elem


if __name__ == '__main__':
    inicio = time.time()
    for _ in range(5):
        v_actual = valor_presion_actual()
        función_comprobar_presion(v_actual)
    tardanza = time.time() - inicio
    print(f'Tiempo empleado {tardanza:.3}s')

    inicio = time.time()
    corrutina = corrutina_comprobar_presion()
    print(next(corrutina))
    inicializar = time.time() - inicio
    print(f'Tiempo empleado para inicializar {inicializar:.3}s')
    for _ in range(5):
        v_actual = valor_presion_actual()
        corrutina.send(v_actual)
    corrutina.throw(KeyboardInterrupt, 'Saliendo de la ejecución')  # se podría usar tambien corrutina.close()
    tardanza = time.time() - inicio
    print(f'Tiempo empleado {tardanza:.3}s')

    cc = listas_de_numeros(7)
    ccc = list(cc)
    print(ccc)

    lst = [1, 2, 3, [2, [34, 32], [245, 63], [4, [4, [[2]]]]]]
    print(list(aplanar(lst)))
