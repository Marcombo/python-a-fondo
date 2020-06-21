import dbm


def escribe_db(nombre_db):
    # abriendo la base de datos
    with dbm.open(nombre_db, 'c') as db:
        db['usuario1'] = 'Paco Lopez'
        db['usuario1_likes'] = '34'
        db['url'] = 'www.elpythonista.com'
        db['titulo_libro'] = 'Python a Fondo'
        # Comprobando los datos usando bytes
        assert db[b'titulo_libro'] == b'Python a Fondo'
        del db['usuario1_likes']


def imprime_db(nombre_db):
    with dbm.open(nombre_db, 'r') as db:
        for clave in db.keys():
            print(f'{clave} -> {db[clave]}')


if __name__ == '__main__':
    nombre_db = 'dbm_db'
    escribe_db(nombre_db)
    imprime_db(nombre_db)
