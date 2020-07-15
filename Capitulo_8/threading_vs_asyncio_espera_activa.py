import asyncio
import threading
import time
import logging

logger = logging.getLogger(__name__)
DEBUG = False
logging_level = logging.DEBUG if DEBUG else logging.INFO
logger.setLevel(logging_level)
ch = logging.StreamHandler()
ch.setLevel(logging_level)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def tarea(n_seg, n):
    logger.debug(f'Comienza {n}')
    time.sleep(n_seg)
    logger.debug(f'Terminado {n}')


def ejecucion_en_hilos(n_tareas, n_seg):
    hilos = []
    for n_tarea in range(n_tareas):
        t = threading.Thread(target=tarea, args=(n_seg, n_tarea))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()


async def tarea_async(n_seg, n):
    logger.debug(f'Comienza {n} async')
    await asyncio.sleep(n_seg)
    logger.debug(f'Terminado {n} async')


async def ejecucion_asyncio(n_tareas, n_seg):
    tareas = []
    for n_tarea in range(n_tareas):
        ast = asyncio.create_task(tarea_async(n_seg, n_tarea))
        tareas.append(ast)
    for t in tareas:
        await t


if __name__ == '__main__':
    tiempo_espera = 0.1
    for tiempo_espera in [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5]:
        for n_tareas in [1000, 2000]:
            start = time.time()
            logger.info(f'Comienzo de ejecución hilos')
            ejecucion_en_hilos(n_tareas, tiempo_espera)
            logger.info(
                f'Ejecución usando {n_tareas} hilos esperando {tiempo_espera}s: {time.time() - start:.4} segundos')

            start = time.time()
            logger.info(f'Comienzo de ejecución asyncio')
            asyncio.run(ejecucion_asyncio(n_tareas, tiempo_espera))
            logger.info(
                f'Ejecución usando {n_tareas} asyncio esperando {tiempo_espera}s: {time.time() - start:.4} segundos')
