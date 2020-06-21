import time

from walrus import Walrus

if __name__ == '__main__':
    db = Walrus(host='localhost', port=6379, db=0)

    # asignacion y obtencion de variables
    db['titulo'] = 'Python a fondo'
    db['calorias'] = 8987
    print(db['titulo'])
    print(db.get('calorias'))
    print(db.get('nombre_perro'))

    # contendedores o tipos de datos
    h = db.Hash('planetas')
    h.update(mercurio=3.303e+23, venus=4.869e+24)
    print(h)
    for key, value in h:
        print(f'Nombre: {key} -> {value}')
    del h['tierra']
    print(h)
    print('venus' in h)

    # autocompletado
    ac = db.autocomplete()
    textos = [
        'Python es el mejor lenguaje del mundo',
        'La comunidad de python usa mucho software libre',
        'La mayoría de módulos de python son software libre',
        'Redis está construido usando Ruby'
    ]
    for txt in textos:
        ac.store(txt)
    print(list(ac.search('python')))
    print(list(ac.search('soft')))

    # cache expirando a los 3 segundos
    cache = db.cache()
    cache.set('secreto', '9s7d86s92', 3)
    print(cache.get('secreto'))
    time.sleep(3)
    print(cache.get('secreto'))
