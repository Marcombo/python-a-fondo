import shelve

from Capitulo_6.formato_con_delimitadores.ficheros_delimitados_csv_tsv import lectura_de_planetas

if __name__ == '__main__':
    nombre_db = 'planetas'
    d = shelve.open(nombre_db)

    planetas = list(lectura_de_planetas('planetas.csv'))

    d['planetas'] = planetas

    tierra = [p for p in planetas if p.nombre == 'Tierra'][0]
    p_mayores = [p for p in planetas if p.radio > tierra.radio]
    p_menores = [p for p in planetas if p.radio < tierra.radio]
    d['planetas_mayores'] = p_mayores
    d['planetas_menores'] = p_menores

    d.close()

    d = shelve.open(nombre_db)
    print(f'Claves guardadas en shelve: {list(d.keys())}')
    print(f'Valores guardados en shelve: {list(d.items())}')
