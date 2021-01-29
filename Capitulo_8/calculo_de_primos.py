import asyncio
import os
import threading
import time
from multiprocessing import Pool
import logging

logger = logging.getLogger(__name__)
DEBUG = True
logging_level = logging.DEBUG if DEBUG else logging.INFO
logger.setLevel(logging_level)
ch = logging.StreamHandler()
ch.setLevel(logging_level)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False  # divisible por un número, por tanto no es primo
    else:
        return True


def contar_primos(n_primos, n_iter):
    logger.debug(f'Comienzo de ejecución de {n_iter}')
    primos_encontrados = []
    valor_actual = 2
    while len(primos_encontrados) < n_primos:
        if es_primo(valor_actual):
            # logger.debug(f'Primo {valor_actual} encontrado por: {n_iter}')
            primos_encontrados.append(valor_actual)
        valor_actual += 1
    logger.debug(f'Fin de ejecución de {n_iter}')
    return primos_encontrados


async def contar_primos_async(n_primos, n_iter):
    logger.debug(f'Comienzo de ejecución de {n_iter} async')
    primos_encontrados = [1]
    valor_actual = 2
    while len(primos_encontrados) < n_primos:
        if es_primo(valor_actual):
            primos_encontrados.append(valor_actual)
        valor_actual += 1
    logger.debug(f'Fin de ejecución de {n_iter} async')
    return primos_encontrados


def ejecucion_secuencial(n_loops=4, n_primos=1000):
    for n in range(n_loops):
        contar_primos(n_primos, n)


def ejecucion_multiproceso(iteraciones, n_procesos, n_primos):
    p = Pool(n_procesos)
    params = [(n_primos, i) for i in range(iteraciones)]
    p.starmap(contar_primos, params)
    p.close()
    p.join()


def ejecucion_en_hilos(iteraciones, n_primos):
    hilos = []
    for n in range(iteraciones):
        t = threading.Thread(target=contar_primos, args=(n_primos, n))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()


async def ejecucion_asyncio(iteraciones, n_primos):
    tareas = []
    for n in range(iteraciones):
        ast = asyncio.create_task(contar_primos_async(n_primos, n))
        tareas.append(ast)
    for t in tareas:
        await t


if __name__ == '__main__':
    numeros_primos = 2500

    for iteraciones in [1, 4, 10, 20]:
        start = time.time()
        ejecucion_secuencial(iteraciones, numeros_primos)
        logger.info(f'Secuencial - {iteraciones} iter: {time.time() - start:.4}s')

        for n_procesos in [int(os.cpu_count() / 2) or 1, os.cpu_count(), os.cpu_count() * 2, 20]:
            start = time.time()
            ejecucion_multiproceso(iteraciones, n_procesos, numeros_primos)
            logger.info(f'Multi_proc - {iteraciones} iter, {n_procesos} procesos: {time.time() - start:.4}s')

        start = time.time()
        ejecucion_en_hilos(iteraciones, numeros_primos)
        logger.info(f'Threading - {iteraciones} iter: {time.time() - start:.4}s')

        start = time.time()
        asyncio.run(ejecucion_asyncio(iteraciones, numeros_primos))
        logger.info(f'Asyncio - {iteraciones} iter: {time.time() - start:.4}s')

