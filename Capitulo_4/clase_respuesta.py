"""Ejemplo de una clase Respuesta la cual guarda las respuesta de un hipotetico examen con el nombre del alumno que ha
contestado la respuesta y el valor de la respuesta"""


class Respuesta:
    def __init__(self, res_correcta, nombre_alumno, res_alumno):
        self.respuesta_correcta = res_correcta
        self.nombre_alumno = nombre_alumno
        self.res_alumno = res_alumno

    def valor_respuesta(self):
        if self.respuesta_correcta == self.res_alumno:
            return 0.5
        return -1

    def __add__(self, other):
        if isinstance(other, Respuesta):
            return self.valor_respuesta() + other.valor_respuesta()
        else:
            return self.valor_respuesta() + other

    def __radd__(self, other):
        return self.__add__(other)


if __name__ == '__main__':
    respuestas = [Respuesta(True, 'Juan', True),
                  Respuesta(False, 'Juan', True),
                  Respuesta(True, 'Juan', True),
                  Respuesta(True, 'Juan', True)]
    print(respuestas[0].valor_respuesta(), respuestas[0].valor_respuesta())
    print(respuestas[0] + respuestas[1])
    total = 0
    for res in respuestas:
        total += res.valor_respuesta()
    print(f'Puntuación total = {total}')
