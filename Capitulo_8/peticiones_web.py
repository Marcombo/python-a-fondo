import asyncio
import os
import threading
import time
from multiprocessing import Pool
import requests
import aiohttp
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

URL_A_USAR = 'https://www.githubstatus.com/'


def peticion_web(n):
    logger.debug(f'Petición número {n}')
    info = requests.get(URL_A_USAR)
    logger.debug(f'Finalizada petición {n}')
    return info.text


async def peticion_web_async(n):
    logger.debug(f'Pidiendo por {n} async')
    async with aiohttp.ClientSession() as s:
        info = await s.get(URL_A_USAR)
    logger.debug(f'Finalizada petición {n} async')
    return info.text


def ejecucion_secuencial(n_webs):
    for n_web in range(n_webs):
        peticion_web(n_web)


def ejecucion_multiproceso(n_procesos, n_webs):
    p = Pool(n_procesos)
    p.map(peticion_web, range(n_webs))
    p.terminate()
    p.join()


def ejecucion_en_hilos(n_webs):
    hilos = []
    for num_web in range(n_webs):
        t = threading.Thread(target=peticion_web, args=(num_web,))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()


async def ejecucion_asyncio(n_webs):
    tareas = []
    for num_web in range(n_webs):
        ast = asyncio.create_task(peticion_web_async(num_web))
        tareas.append(ast)
    for t in tareas:
        await t


if __name__ == '__main__':
    for n_webs in [20, 100, 200]:
        logger.info(f'----- Tiempos de ejecución de peticiones a {n_webs} webs usando {URL_A_USAR}  -----')
        for n_sec in [1, n_webs]:
            start = time.time()
            logger.info(f'Comienzo de ejecución secuencial de {n_webs} webs')
            ejecucion_secuencial(n_sec)
            logger.info(f'Ejecución secuencial de {n_sec} webs {time.time() - start:.4} segundos')

        for n_multiproceso in [int(os.cpu_count() / 2) or 1, os.cpu_count(), os.cpu_count() * 2, n_webs]:
            start = time.time()
            logger.info(f'Comienzo de ejecución multiproceso {n_multiproceso} procesos paralelos')
            ejecucion_multiproceso(n_multiproceso, n_webs)
            logger.info(f'Ejecución usando multiproceso: {time.time() - start:.4} segundos')

        start = time.time()
        logger.info(f'Comienzo de ejecución hilos')
        ejecucion_en_hilos(n_webs)
        logger.info(f'Ejecución usando hilos: {time.time() - start:.4} segundos')

        start = time.time()
        logger.info(f'Comienzo de ejecución asyncio')
        asyncio.run(ejecucion_asyncio(n_webs))
        logger.info(f'Ejecución usando asyncio: {time.time() - start:.4} segundos')
