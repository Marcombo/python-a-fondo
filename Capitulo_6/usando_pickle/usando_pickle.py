import pickle

from Capitulo_6.formato_con_delimitadores.ficheros_delimitados_csv_tsv import lectura_de_planetas

if __name__ == '__main__':
    planetas = list(lectura_de_planetas('planetas.csv'))
    with open('pickled_planetas', 'wb') as fw:
        pickler = pickle.Pickler(fw)
        pickler.dump(planetas)
    
    with open('pickled_planetas', 'rb') as fr:
        planetas_serializados = pickle.Unpickler(fr).load()

    print(f'Planetas serializados {planetas_serializados}')
    assert planetas == planetas_serializados

