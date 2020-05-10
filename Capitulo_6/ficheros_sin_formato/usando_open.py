import string


def escribir_fichero(nombre, lineas, encoding):
    with open(nombre, 'w') as f:
        linea = string.ascii_lowercase


def escribir_contenido(nombre_fichero):
    with open(nombre_fichero, 'w', encoding='latin-1') as fw:
        fw.write('El árbol es marrón')

    for errors in ['ignore', 'replace', 'backslashreplace', 'surrogateescape', 'strict', 'namereplace',
                   'xmlcharrefreplace']:
        try:
            with open(nombre_fichero, 'r', encoding='utf-8', errors=errors) as fr:
                print(fr.read())
                print(f'Contenido con errors={errors}: {fr.read()}')
        except:
            print(f'Error reading the file with errors={errors}')


if __name__ == '__main__':
    escribir_contenido('fichero.txt')
