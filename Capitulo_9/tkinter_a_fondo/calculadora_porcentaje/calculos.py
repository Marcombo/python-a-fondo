from decimal import Decimal


def validacion_decimal(inp):
    try:
        d = Decimal(inp)
        return True
    except:
        return False


def calc_porcentaje(cantidad: Decimal, porcentaje: Decimal) -> Decimal:
    """Calcula el porcentaje sobre una cantidad"""
    return cantidad * (porcentaje / 100)
