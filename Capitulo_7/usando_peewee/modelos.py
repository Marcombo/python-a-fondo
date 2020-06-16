import sqlite3

from peewee import SqliteDatabase, Model, CharField, BooleanField, DateField, ForeignKeyField, IntegerField, \
    IntegrityError

db = SqliteDatabase('peewee_ejemplo.db')


class ModeloBase(Model):
    class Meta:
        database = db


class Perfil(ModeloBase):
    nombre = CharField(unique=True)
    puede_editar = BooleanField()


class Usuario(ModeloBase):
    nombre = CharField()
    apellido = CharField()
    f_nacimiento = DateField()
    perfil = ForeignKeyField(Perfil, backref='usuarios')


class Post(ModeloBase):
    texto = CharField()
    fecha = DateField()
    likes = IntegerField()
    autor = ForeignKeyField(Usuario, backref='posts')


if __name__ == '__main__':
    # creando las tablas
    db.connect()
    db.create_tables([Perfil, Usuario, Post])

    try:
        # agregando contenido
        for nombre, editable in (('Admin', True), ('Editor', True), ('Visitante', False)):
            p = Perfil.create(nombre=nombre, puede_editar=editable)
            p.save()

        for nombre, apellido, fecha, perfil_id in [('Paco', 'Lopez', '1998-08-03', 2),
                                                   ('Maria', 'Gomez', '1982-10-28', 1),
                                                   ('Antonio', 'Lopez', '1967-02-21', 2)]:
            u = Usuario.create(nombre=nombre, apellido=apellido, f_nacimiento=fecha, perfil=perfil_id)
            u.save()

        for autor_id, texto, fecha, likes in [(1, 'Mi primera entrada', '2020-10-28', 4),
                                              (1, 'Mi segunda entrada', '2020-11-09', 1),
                                              (2, '¿Como hacer ejercicio?', '2020-09-08', 40),
                                              (3, 'Dietas saludables', '2020-07-19', 15)]:
            p = Post.create(autor=autor_id, texto=texto, fecha=fecha, likes=likes)
            p.save()
    except (sqlite3.IntegrityError, IntegrityError):
        pass  # ya creados los datos

    # contando cantidad de perfiles
    cnt_perfiles = Perfil.select().count()
    print(f'Cantidad de perfiles: {cnt_perfiles}')

    # haciendo consultas con uniones
    usuarios_query = Usuario.select().where(Usuario.apellido.startswith('L'))
    print(f'Usuarios comenzando por L: {[u.nombre for u in usuarios_query]}')

    editores = Usuario.select().join(Perfil).where(Perfil.nombre == 'Editor').execute()
    for e in editores:
        print(f'Editor: {e.nombre} {e.apellido}')
