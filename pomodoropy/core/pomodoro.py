#!/usr/bin/env python2.7
__author__ = "santiago"
__date__ = "$15/09/2011 23:56:23$"

import estados as estados
from temporizador import Temporizador


class ProcesoPomodoro():
    """
    Clase que controla el proceso de pomodoro.
    """

    SECUENCIA_DE_ESTADOS = [estados.ESTADO_TRABAJANDO,
                            estados.ESTADO_DESCANSO_CORTO,
                            estados.ESTADO_TRABAJANDO,
                            estados.ESTADO_DESCANSO_CORTO,
                            estados.ESTADO_TRABAJANDO,
                            estados.ESTADO_DESCANSO_CORTO,
                            estados.ESTADO_TRABAJANDO,
                            estados.ESTADO_DESCANSO_LARGO]

    def __init__(self):
        self._estaCorriendo = False

    def start(self):
        """Pone en funcionamiento el timer. """
        self._estadoActual = 0
        self._estaCorriendo = True

    def get_estado(self):
        """Retorna el estado actual"""
        if self._estaCorriendo:
            return ProcesoPomodoro.SECUENCIA_DE_ESTADOS[self._estadoActual]
        else:
            return estados.ESTADO_PARADO

    def avanzar_estado(self):
        """
        Avanza el timer al estado siguiente.
        Si el timer estaba parado se mantiene en el estado parado
        """

        if self._estaCorriendo:
            self._estadoActual += 1
            self._estadoActual %= len(ProcesoPomodoro.SECUENCIA_DE_ESTADOS)


class ControladorPomodoro(object):

    def __init__(self):
        self._temporizador = Temporizador()
        self._proceso = ProcesoPomodoro()

    def iniciar_pomodoro(self):
        self._proceso.start()
        self._lanzar_temporizador()

    def avanzar_estado(self):
        self._proceso.avanzar_estado()
        self._lanzar_temporizador()

    def _lanzar_temporizador(self):
        estado_actual = self._proceso.get_estado()
        self._temporizador.set_duracion(estado_actual.get_duracion())
        self._temporizador.iniciar_cuenta_regresiva()


def _main():
    print "Main Pomodoro Timer"
    controladorPomodoro = ControladorPomodoro()
    controladorPomodoro.iniciar_pomodoro()
    for i in range(16):
        controladorPomodoro.avanzar_estado()


if __name__ == "__main__":
    main()
