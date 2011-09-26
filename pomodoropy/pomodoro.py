#!/usr/bin/env python2.7
__author__="santiago"
__date__ ="$15/09/2011 23:56:23$"

import estados as estados

class PomodoroTimer():

    SECUENCIA_DE_ESTADOS = [estados.get_estado_trabajando(), estados.get_estado_descanso_corto(),
                            estados.get_estado_trabajando(), estados.get_estado_descanso_corto(),
                            estados.get_estado_trabajando(), estados.get_estado_descanso_corto(),
                            estados.get_estado_trabajando(), estados.get_estado_descanso_largo()]

    def __init__(self):
        self.estaCorriendo = False

    def start(self):
        """Pone en funcionamiento el timer. """
        self.estadoActual = 0
        self.estaCorriendo = True
        
    def get_estado(self):
        """Retorna el estado actual"""
        if self.estaCorriendo :
            return PomodoroTimer.SECUENCIA_DE_ESTADOS[self.estadoActual]
        else:
            return estados.get_estado_parado()

    def avanzar_estado(self):
        """Avanza el timer al estado siguiente.
            Si el timer estaba parado se mantiene en el estado parado
        """
        if self.estaCorriendo :
            self.estadoActual += 1
            self.estadoActual %= len(PomodoroTimer.SECUENCIA_DE_ESTADOS)


if __name__ == "__main__":
    print "Main Pomodoro Timer"
    pomodoroTimer = PomodoroTimer()
    pomodoroTimer.start()
    for i in range(16):
        print pomodoroTimer.get_estado()
        pomodoroTimer.avanzar_estado()
    
