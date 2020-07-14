import concurrent.futures
import logging
import time

from Capitulo_8.calculo_de_primos import contar_primos
from Capitulo_8.peticiones_web import peticion_web

logger = logging.getLogger(__name__)
DEBUG = True
logging_level = logging.DEBUG if DEBUG else logging.INFO
logger.setLevel(logging_level)
ch = logging.StreamHandler()
ch.setLevel(logging_level)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def ejecucion_primos(n_iteraciones, n_procesos, n_primos):
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_procesos) as ex:
        futuros_primos = {ex.submit(contar_primos, n_primos, i): i for i in range(n_iteraciones)}
        for futuro in concurrent.futures.as_completed(futuros_primos):
            primos_calculados = futuro.result()
            iteracion = futuros_primos[futuro]
            logger.debug(f'Terminada iter {iteracion} con {len(primos_calculados)} primos calculados')


def ejecucion_webs(n_iteraciones):
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_iteraciones) as ex:
        for i, resultado in zip(range(n_iteraciones), ex.map(peticion_web, range(n_iteraciones))):
            logger.debug(f'Terminado {i}')


if __name__ == '__main__':
    n_procesos = 8
    n_primos = 2500
    n_iteraciones = 20

    start = time.time()
    logger.info(f'Comienzo cálculo de números primos')
    ejecucion_primos(n_iteraciones, n_procesos, n_primos)
    logger.info(f'Ejecución usando {n_iteraciones} iter, {n_procesos} procs {time.time() - start:.4} segundos')

    n_iteraciones = 200
    start = time.time()
    logger.info(f'Comienzo peticiones web')
    ejecucion_webs(n_iteraciones)
    logger.info(f'Ejecución pidiendo {n_iteraciones} webs {time.time() - start:.4} segundos')
