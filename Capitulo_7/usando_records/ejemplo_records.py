import records

if __name__ == '__main__':
    db = records.Database('sqlite:///ejemplo_pydal.db')
    tablas = db.get_table_names()
    print(f'Tablas disponibles: {tablas}')
    usuarios = db.query('SELECT * FROM usuarios')
    primer_usuario = usuarios[0]
    print(f'El primer usuario es: {primer_usuario}')
    print(f'Datos de usuario: {primer_usuario.nombre} {primer_usuario.apellido}')
    print(f'Usuario como dict: {primer_usuario.as_dict()}')
    posts_populares = db.query('select * from posts where likes > :min_likes', min_likes=10)
    print(f'Post populares {posts_populares.all()}')
    print(posts_populares.export('df'))
    for formato_ex in ('csv', 'json'):
        with open('post_populares.' + formato_ex, 'w') as fw:
            fw.write(posts_populares.export(formato_ex))
