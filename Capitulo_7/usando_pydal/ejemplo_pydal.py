import datetime

from pydal import DAL, Field

db_main = DAL('sqlite://ejemplo_pydal.db')


def crear_tablas(db):
    try:
        db.perfiles.drop()
        db.usuarios.drop()
        db.posts.drop()
    except Exception:
        print('No data on the database')

    db.define_table('perfiles',
                    Field('id', type='id'),
                    Field('nombre_perfil'),
                    Field('puede_editar'),
                    )

    db.define_table('usuarios',
                    Field('id', type='id'),
                    Field('nombre'),
                    Field('apellido'),
                    Field('f_nacimiento', type='date'),
                    Field('perfil_id', type='integer')
                    )

    db.define_table('posts',
                    Field('id', type='id'),
                    Field('autor_id', type='integer'),
                    Field('texto'),
                    Field('fecha', type='date'),
                    Field('likes', type='integer'),
                    )


def insertar_datos(db):
    db.usuarios.truncate()
    db.perfiles.truncate()
    db.posts.truncate()

    db.perfiles.insert(nombre_perfil='Admin', puede_editar='Y')
    db.perfiles.insert(nombre_perfil='Visitante', puede_editar='N')
    db.perfiles.insert(nombre_perfil='Editor', puede_editar='Y')

    db.usuarios.insert(nombre='Paco', apellido='Lopez', f_nacimiento=datetime.datetime(1998, 8, 3), perfil_id=3)
    db.usuarios.insert(nombre='Maria', apellido='Gomez', f_nacimiento=datetime.datetime(1982, 10, 28), perfil_id=1)
    db.usuarios.insert(nombre='Antonio', apellido='Lopez', f_nacimiento=datetime.datetime(1967, 2, 21), perfil_id=3)

    db.posts.insert(autor_id=1, texto='Mi primera entrada', fecha=datetime.datetime(2020, 10, 28), likes=4)
    db.posts.insert(autor_id=1, texto='Mi segunda entrada', fecha=datetime.datetime(2020, 11, 9), likes=1)
    db.posts.insert(autor_id=2, texto='¿Cómo hacer ejercicio?', fecha=datetime.datetime(2020, 9, 8), likes=40)
    db.posts.insert(autor_id=2, texto='Dietas saludables', fecha=datetime.datetime(2020, 7, 19), likes=15)
    db.commit()


if __name__ == '__main__':
    crear_tablas(db_main)
    insertar_datos(db_main)
    query = db_main.usuarios.apellido.startswith('L')
    rows = db_main(query).select()
    print(f'Usuarios apellidados con L:\n {rows}')

    posts_relevantes = db_main(db_main.posts.likes > 10).select()
    print(f'Posts relevantes:\n {posts_relevantes}')
