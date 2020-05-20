import csv
from dataclasses import dataclass

import pandas as pd


def lectura_csv(nombre_fichero):
    with open(nombre_fichero, 'r') as fr:
        reader = csv.reader(fr)
        for fila in reader:
            print(fila)


@dataclass
class Planeta:
    nombre: str
    masa: float
    radio: float

    def __post_init__(self):
        self.radio = float(self.radio)
        self.masa = float(self.masa)

    @property
    def gravedad(self):
        g_constante = 6.673e-11
        return g_constante * self.masa / (self.radio ** 2)


def lectura_de_planetas(nombre_fichero):
    with open(nombre_fichero, 'r') as fr:
        reader = csv.reader(fr)
        tiene_cabecera = csv.Sniffer().has_header(fr.read(1024))
        fr.seek(0)  # colocando la posición de lectura al inicio de nuevo
        if tiene_cabecera:
            cabecera = next(reader)  # se ignora la cabecera
        for fila in reader:
            yield Planeta(*fila)


def escritura_de_planetas(nombre_fichero, fichero_salida):
    with open(fichero_salida, 'w') as fw:
        columnas = ['nombre', 'masa', 'radio', 'diametro']
        writer = csv.DictWriter(fw, fieldnames=columnas, extrasaction='ignore')
        writer.writeheader()
        for planeta in lectura_de_planetas(nombre_fichero):
            valores = planeta.__dict__
            valores['diametro'] = planeta.radio ** 2
            writer.writerow(valores)


def lectura_y_escritura_usando_pandas(fichero_entrada, fichero_salida):
    df = pd.read_csv(fichero_entrada)
    # Se aplican las modificaciones en el dataframe
    print(df.head())
    df['Diametro'] = df['Radio'] ** 2
    df.to_csv(fichero_salida, index=False)


if __name__ == '__main__':
    planetas = lectura_csv('planetas.csv')
    print(planetas)
    for p in lectura_de_planetas('planetas.csv'):
        print(f'La gravedad en {p.nombre} es {p.gravedad}')

    escritura_de_planetas('planetas.csv', 'nuevos_planetas.csv')
    lectura_y_escritura_usando_pandas('planetas.csv', 'nuevos_planetas_pandas.csv')
