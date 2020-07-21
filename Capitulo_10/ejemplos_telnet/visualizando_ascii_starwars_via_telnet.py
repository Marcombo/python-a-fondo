import os
import sys
import telnetlib
from time import sleep
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def ver_starwars(tnet):
    tnet.write(b'starwars\r\n')
    n_lines = 12  # numero de lineas enviadas en cada imagen
    while True:
        imagen = b''.join([tnet.read_some() for _ in range(n_lines)]).decode()
        sys.stdout.write(imagen)


if __name__ == '__main__':
    tnet = telnetlib.Telnet('telehack.com')
    info = tnet.read_until(b'\r\n.').decode()
    print(info)
    print('Visualizando la pelicula ASCII starwars en 5 segundos')
    sleep(5)
    ver_starwars(tnet)
