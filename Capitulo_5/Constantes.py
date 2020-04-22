from Clases import Formateador

# Marcas de coches disponibles
MARCAS_DE_COCHES = ['HONDA', 'MAZDA', 'TOYOTA']

# Expresiones regulares para detectar cada tipo de dato
FORMATOS_Y_TIPOS = {
    int: '\d+',
    str: '[a-zA-Z]+',
}

FORMATEADORES = {
    int: Formateador('Formateador de enteros', FORMATOS_Y_TIPOS[int]),
    str: Formateador('Formateador de cadenas', FORMATOS_Y_TIPOS[str]),
}
