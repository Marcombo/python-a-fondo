from dataclasses import dataclass
from struct import unpack

import pandas as pd


@dataclass
class Info:
    amigos: int
    nombre: str
    salario: int

    def __post_init__(self):
        self.nombre = self.nombre.strip()


def ancho_fijo_manual(fichero_origen, anchos):
    info = []
    headers = None
    with open(fichero_origen, 'r', newline='') as fr:
        for line in fr.readlines():
            if headers is None:
                headers = line
                continue  # omitiendo la primera línea de cabeceras
            inicio, fin = 0, anchos[0]
            amigos = int(line[inicio:fin])
            inicio, fin = anchos[0], sum(anchos[:2])
            nombre = line[inicio:fin]
            inicio, fin = sum(anchos[:2]), sum(anchos[:3])
            salario = int(line[inicio:fin])
            info.append(Info(amigos, nombre, salario))
    return info


def ancho_fijo_generico(fichero_origen, anchos_con_tipo):
    info = []
    headers = None
    with open(fichero_origen, 'r', newline='') as fr:
        for line in fr.readlines():
            if headers is None:
                headers = line
                continue  # omitiendo la primera línea de cabeceras
            acc = 0
            variables = []
            for ancho, tipo in anchos_con_tipo:
                inicio, fin = acc, acc + ancho
                valor = tipo(line[inicio:fin])
                variables.append(valor)
                acc += ancho
            info.append(Info(*variables))
    return info


def ancho_fijo_pandas(fichero_origen, anchos):
    return pd.read_fwf(fichero_origen, widths=anchos)


def ancho_fijo_struct(fichero_origen):
    formato = '6s16s8s'  # 6 amigos, 16 nombre, 7 salario y 1 por \n
    headers = None
    info = []
    with open(fichero_origen, 'rb') as fr:
        for line in fr.readlines():
            if headers is None:
                headers = line
                continue  # omitiendo la primera línea de cabeceras
            vals = unpack(formato, line)
            info.append(Info(*vals))
    return info


if __name__ == '__main__':
    fichero_origen = 'ejemplo_ancho_fijo.txt'

    info = ancho_fijo_struct(fichero_origen)
    print(info)

    anchos = [6,  # Num Amigos
              16,  # Nombre
              7]  # Salario

    info = ancho_fijo_manual(fichero_origen, anchos)
    print(info)

    anchos_con_tipo = [(6, int),  # Num Amigos
                       (16, str),  # Nombre
                       (7, int)]  # Salario
    ancho_fijo_generico(fichero_origen, anchos_con_tipo)
    print(info)

    info_df = ancho_fijo_pandas(fichero_origen, anchos)
    print(info_df)
    print(info_df.mean(axis=0))
