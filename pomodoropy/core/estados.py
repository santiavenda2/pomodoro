#!/usr/bin/env python2.7
__author__="santiago"
__date__ ="$16/09/2011 01:03:11$"

class EstadoPomodoro(object):
    """
    Clase que representa un estado de Pomodoro
    """

    def __init__(self, nombre, duracion):
        self._nombre = nombre
        self._duracion = duracion

    def get_nombre(self):
        return self._nombre

    def get_duracion(self):
        return self._duracion

    def __str__(self):
        return self.get_nombre()

# Estados definidos
ESTADO_PARADO = EstadoPomodoro("Parado", float('inf') )
ESTADO_TRABAJANDO = EstadoPomodoro("Trabajando", 25 )
ESTADO_DESCANSO_CORTO = EstadoPomodoro("Descanso corto",5 )
ESTADO_DESCANSO_LARGO = EstadoPomodoro("Descanso largo", 30 )

ESTADOS_DEFINIDOS = [ESTADO_PARADO, ESTADO_TRABAJANDO,
                    ESTADO_DESCANSO_CORTO, ESTADO_DESCANSO_LARGO]
if __name__ == "__main__":
    print "Estados definidos: "
    for estado in ESTADOS_DEFINIDOS:
        print estado.get_nombre()

