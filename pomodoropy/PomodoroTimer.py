#!/usr/bin/env python2.6
__author__="santiago"
__date__ ="$15/09/2011 23:56:23$"



class PomodoroTimer():



    SECUENCIA_DE_ESTADOS = [ESTADO_TRABAJANDO, ESTADO_DESCANSO_CORTO,
                            ESTADO_TRABAJANDO, ESTADO_DESCANSO_CORTO,
                            ESTADO_TRABAJANDO, ESTADO_DESCANSO_CORTO,
                            ESTADO_TRABAJANDO, ESTADO_DESCANSO_LARGO]

    def __init__(self):
        self.estaCorriendo = False

    def start(self):
        print "pomodoro timer corriendo"
        self.estadoActual = 0
        self.estaCorriendo = True
        
    def getEstado(self):
        if self.estaCorriendo :
            return PomodoroTimer.SECUENCIA_DE_ESTADOS[self.estadoActual]
        else:
            return PomodoroTimer.ESTADO_PARADO

    def avanzarEstado(self):
        if self.estaCorriendo :
            self.estadoActual += 1
            self.estadoActual %= len(PomodoroTimer.SECUENCIA_DE_ESTADOS)


if __name__ == "__main__":
    print "Main Pomodoro Timer"
    pomodoroTimer = PomodoroTimer()
    for i in range(16):
        print pomodoroTimer.getEstado()
        pomodoroTimer.avanzarEstado()
    
