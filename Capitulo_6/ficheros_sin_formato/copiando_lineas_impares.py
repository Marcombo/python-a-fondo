def copia_impares(fichero_origen, fichero_destino):
    with open(fichero_origen, 'r', newline='') as fr:
        with open(fichero_destino, 'w', newline='') as fw:
            idx = 0
            for linea in fr.readlines():
                if not idx % 2:
                    fw.write(linea)
                idx += 1


def copiar_trozos(fichero_origen, fichero_destino, saltos=100, tamano=10):
    with open(fichero_origen, 'r', newline='') as fr:
        with open(fichero_destino, 'w', newline='') as fw:
            line = fr.read(tamano)
            while line:
                fw.write(line)
                # Avanzando en el fichero
                new_seek = fr.tell() + saltos
                fr.seek(new_seek)
                # leyendo 10 caracteres
                line = fr.read(tamano)


def examinar_contenido(nombre_fichero):
    with open(nombre_fichero, 'r') as f:
        return f.read()


if __name__ == '__main__':
    fichero_origen = 'lorem_ipsum.txt'
    fichero_destino = 'impares_ipsum.txt'
    copia_impares(fichero_origen, fichero_destino)
    contenido = examinar_contenido(fichero_destino)
    print(contenido)

    fichero_origen = 'lorem_ipsum.txt'
    fichero_destino = 'trozos_ipsum.txt'
    copiar_trozos(fichero_origen, fichero_destino)
    examinar_contenido(fichero_destino)
