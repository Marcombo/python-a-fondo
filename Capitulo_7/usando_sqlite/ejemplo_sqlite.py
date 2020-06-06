import sqlite3


def crear_tablas(con):
    cur = con.cursor()

    try:
        cur.execute('DROP TABLE perfiles')
        cur.execute('DROP TABLE usuarios')
        cur.execute('DROP TABLE posts')
    except Exception:
        print('No data on the database')

    cur.execute('''CREATE TABLE perfiles (id INTEGER PRIMARY KEY, 
                                          nombre_perfil TEXT, 
                                          puede_editar TEXT)''')

    cur.execute('''CREATE TABLE usuarios (id INTEGER PRIMARY KEY, 
                                          nombre TEXT, 
                                          apellido TEXT, 
                                          f_nacimiento TEXT, 
                                          perfil_id INTEGER,
                                          FOREIGN KEY (perfil_id) REFERENCES perfiles(id)
                                          )''')

    cur.execute('''CREATE TABLE posts (id INTEGER PRIMARY KEY, 
                                       autor_id INTEGER,
                                       texto TEXT,
                                       fecha TEXT,
                                       likes INTEGER,
                                       FOREIGN KEY (autor_id) REFERENCES usuarios(id)
                                       )''')


def insertar_datos(con):
    cur = con.cursor()

    cur.executescript('''
        DELETE FROM usuarios;
        DELETE FROM perfiles;
        DELETE FROM posts;
''')
    cur.execute('''INSERT INTO perfiles (nombre_perfil, puede_editar) 
                    values ('Admin', 'Y'),
                           ('Visitante', 'N'),
                           ('Editor', 'Y')''')

    cur.executescript('''INSERT INTO usuarios (nombre, apellido, f_nacimiento, perfil_id) 
                          values ('Paco', 'Lopez', '1998-08-03', 3),
                                 ('Maria', 'Gomez', '1982-10-28', 1),
                                 ('Antonio', 'Lopez', '1967-02-21', 3);
                                 
                          INSERT INTO posts (autor_id,  texto, fecha, likes)
                          values (1, 'Mi primera entrada', '2020-10-28', 4),
                                 (1, 'Mi segunda entrada', '2020-11-09', 1),
                                 (2, '¿Como hacer ejercicio?', '2020-09-08', 40),
                                 (3, 'Dietas saludables', '2020-07-19', 15);
                               ''')
    con.commit()


class MulSum2:
    """Agregación que multiplica cada valor y los suma todos"""

    def __init__(self):
        self.mul = 2
        self.acumulado = 0

    def step(self, value):
        self.acumulado += value * self.mul

    def finalize(self):
        return self.acumulado


class AccSimple:
    """Agregador simple"""

    def __init__(self):
        self.acumulado = 0

    def step(self, value):
        self.acumulado += value

    def finalize(self):
        return self.acumulado


if __name__ == '__main__':
    con = sqlite3.connect('ejemplo_sqlite.db')

    crear_tablas(con)
    insertar_datos(con)

    cur = con.cursor()
    cur.execute("SELECT * from usuarios WHERE apellido LIKE 'L%'")
    rows = cur.fetchall()
    print(f'Usuarios apellidados con L:\n {rows}')

    cur = con.cursor()
    cur.execute(
        "SELECT p.texto, p.likes, u.nombre, u.apellido from usuarios u, posts p WHERE p.autor_id = u.id and p.likes > 5 order by p.likes")
    rows = cur.fetchall()
    info = '\n'.join(' - '.join(map(str, r)) for r in rows)
    print(f'Post famosillos con autores:\n{info}')

    cur = con.cursor()
    cur.execute("SELECT u.nombre, count(*) from usuarios u, posts p WHERE p.autor_id = u.id group by u.nombre")
    rows = cur.fetchall()
    info = '\n'.join(f'{r[0]}->{r[1]}' for r in rows)
    print(f"Autores y likes:\n{info}")

    con.create_aggregate("acc_simple", 1, AccSimple)
    cur = con.cursor()
    cur.execute('select acc_simple(likes) from posts')
    row = cur.fetchone()
    print(f'Suma total de likes: {row[0]}')

    con.create_aggregate("mul_sum", 1, MulSum2)
    cur = con.cursor()
    cur.execute('select mul_sum(likes), acc_simple(likes) from posts')
    rows = cur.fetchall()
    print(f'Total multiplicado y simple de likes: {rows}')
