
class Vehiculo:
    def __init__(self, ruedas: int, peso: float):
        """Ruedas: en uso
           Peso: se expresa en Kg como punto flotante"""
        self.ruedas = ruedas
        self.peso = peso


def guess_type(v: Vehiculo):
    match v:
        case Vehiculo(ruedas=2, peso=x):
            if x > 100:
                return 'Moto'
            return 'Bicicleta'
        case Vehiculo(ruedas=3, peso=x):
            return 'Triciclo'
        case Vehiculo(ruedas=4, peso=x) if v.peso < 2500:
            return 'Coche'
        case Vehiculo(ruedas=4, peso=x) if v.peso < 3000:
            return 'Coche pesado'
        case Vehiculo(ruedas=y, peso=x) if y > 4:
            return 'Camión'
        case x:
            return f'{x} no identificado'


if __name__ == '__main__':
    v1 = Vehiculo(2, 14.3)
    v2 = Vehiculo(2, 153.2)
    v3 = Vehiculo(4, 1500.5)
    v4 = Vehiculo(4, 2700.89)
    v5 = Vehiculo(6, 3500.43)
    print("Vehiculo(2, 14.3) -> ", guess_type(v1))  # Bicicleta
    print("Vehiculo(2, 153.2) -> ",guess_type(v2))  # Moto
    print("Vehiculo(4, 1500.5) -> ",guess_type(v3))  # Coche
    print("Vehiculo(4, 2700.89) -> ",guess_type(v4))  # Coche pesado
    print("Vehiculo(6, 3500.43) -> ",guess_type(v5))  # Camión
