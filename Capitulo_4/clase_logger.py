import logging


class Logger:
    logger = None

    def __new__(cls, *args, **kwargs):
        if not cls.logger:
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.DEBUG)
            fh = logging.FileHandler(cls.__name__ + '.log')
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            cls.logger = logger
        instancia = super(Logger, cls).__new__(cls)
        instancia.__init__(*args, **kwargs)
        return instancia

    def __init__(self, *args, **kwargs):
        super(Logger, self).__init__(*args, **kwargs)

    def __getattribute__(self, item):
        if not item.startswith('__'):
            object.__getattribute__(self, 'logger').info(f'Accediendo al atributo {item}')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__getattribute__(self, 'logger').info(f'Asignando al atributo "{key}" el valor "{value}"')
        object.__setattr__(self, key, value)


class Foo(Logger):
    pass


if __name__ == '__main__':
    ll = Logger()
    ll.volumen = 45
    ll.radio = 2
    ll.tipo = 'Circunferencia'
    print(f'Objeto de tipo {ll.tipo} con un volumen de {ll.volumen} y radio {ll.radio}')

    f = Foo()
    f.altura = 12
    f.peso = 89
    print(f.altura * f.peso)
