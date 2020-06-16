from sqlalchemy import create_engine, Column, String, Integer, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class Perfil(Base):
    __tablename__ = 'perfiles'

    id = Column(Integer, primary_key=True)
    nombre_perfil = Column(String)
    puede_editar = Column(Boolean)


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    f_nacimiento = Column(Date)
    perfil_id = Column(Integer, ForeignKey('perfiles.id'))


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    autor_id = Column(Integer, ForeignKey('usuarios.id'))
    texto = Column(String)
    fecha = Column(Date)
    likes = Column(Integer)


if __name__ == '__main__':
    engine = create_engine('sqlite:///ejemplo_sqlite.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    usuarios = session.query(Usuario.nombre, Usuario.apellido).all()
    print(usuarios)
    posts_famosos = session.query(Post.texto).filter(Post.likes >= 10).all()
    print(posts_famosos)

    admins = session.query(Usuario.nombre).join(Perfil).filter(Perfil.nombre_perfil == 'Admin').all()
    print(admins)

    posts_no_admins = session.query(Post.texto, Usuario.apellido).join(Usuario).join(Perfil).filter(
        Perfil.nombre_perfil != 'Admin').all()
    print(posts_no_admins)
