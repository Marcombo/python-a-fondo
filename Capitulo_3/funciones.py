import hashlib
import json


def extraer_identificadores(cadena_original, sep=' '):
    return cadena_original.split(sep)


def aplicar_sha256(lst):
    hashes = []
    for cad in lst:
        m = hashlib.sha256()
        m.update(cad.encode('utf-8'))
        hashes.append(m.hexdigest())

    return hashes


def aplicar_md5(lst):
    md5s = []
    for cad in lst:
        m = hashlib.md5(cad.encode('utf-8'))
        md5s.append(m.hexdigest())

    return md5s


def escribir_a_fichero(data, nombre_fichero='out.txt'):
    with open(nombre_fichero, 'w') as f:
        for d in data:
            f.write(d + '\n')
    return nombre_fichero


def escribir_a_json(data, nombre_fichero='out.json'):
    with open(nombre_fichero, 'w') as f:
        json.dump(data, f)
    return nombre_fichero


if __name__ == '__main__':
    cadena_original = 'texto<>a<>guardar'
    identificadores = extraer_identificadores(cadena_original, sep='<>')
    shas = aplicar_sha256(identificadores)
    nombre_fichero = escribir_a_fichero(shas)
    print(f'Sha256 de cadena original escrita en {nombre_fichero}')
    md5s = aplicar_md5(identificadores)
    nombre_fichero = escribir_a_json(shas)
    print(f'md5s de cadena original escrita en {nombre_fichero}')
