"""Ejemplo de una clase contenedor que implementa muchos de los métodos mágicos de contenedores"""
import re


class Paso:
    def __init__(self, instrucciones, ingredientes):
        self.instrucciones = instrucciones
        self.ingredientes = {}
        for ing_cad in ingredientes.split('\n'):
            if ing_cad:
                self.ingredientes.update(self.obtener_ingredientes(ing_cad))

    @staticmethod
    def obtener_ingredientes(cadena_ingrediente: str) -> dict:
        cantidad, ingrediente = re.findall('(?P<cantidad>\d+)g-(?P<ingrediente>.+)', cadena_ingrediente)[0]
        return {ingrediente: float(cantidad)}

    def __repr__(self):
        resultado = f'{self.instrucciones}'
        if self.ingredientes:
            resultado += f' usando {",".join(self.ingredientes.keys())}'
        return resultado


class Receta:
    def __init__(self, nombre, pasos_txt):
        self.nombre = nombre
        self.pasos = []
        for pasos_cad in pasos_txt.split(';'):
            instrucciones, ingredientes = pasos_cad.split('|')
            self.pasos.append(Paso(instrucciones, ingredientes))

    def __contains__(self, item):
        for paso in self.pasos:
            if item in paso.ingredientes:
                return True
        return False

    def __len__(self):
        return len(self.pasos)

    def __getitem__(self, item):
        return self.pasos[item]

    def __iter__(self):
        self.__n = 0
        return self

    def __next__(self):
        if self.__n < len(self.pasos):
            resultado = self.pasos[self.__n]
            self.__n += 1
            return resultado
        else:
            raise StopIteration


if __name__ == '__main__':
    rec = Receta('Empanadas',
                 'Mezclar|\n2g-Sal\n420g-Harina;Expandir|;Rellenar|\n4g-Huevo;Freir|\n3g-Aceite;Servir|')

    print('Está Huevo en: ', 'Huevo' in rec)

    for idx, paso in enumerate(rec):
        print(f'Paso {idx + 1}: {paso}')
