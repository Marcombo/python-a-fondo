import telnetlib

if __name__ == '__main__':
    tnet = telnetlib.Telnet('telehack.com')
    info = tnet.read_until(b'\r\n.').decode()
    print(info)
    # Pidiendo el comando cal
    tnet.write(b'cal\r\n')
    info = tnet.read_until(b'\r\n.').decode()
    print(info)
    # Usando rot13 para convertir texto
    tnet.write(b'rot13 Python a fondo\r\n')
    info = tnet.read_until(b'\r\n.').decode()
    print(info)
