# To change this template, choose Tools | Templates
# and open the template in the editor.
#!/usr/bin/env python2.6
__author__="santiago"
__date__ ="$16/09/2011 01:03:11$"

NOMBRE_ESTADO_TRABAJANDO = "trabajando"
NOMBRE_ESTADO_DESCANSO_CORTO = "descanso corto"
NOMBRE_ESTADO_DESCANSO_LARGO = "descanso largo"
NOMBRE_ESTADO_PARADO = "Parado"
DURACION_ESTADO_PARADO = float('inf')
DURACION_ESTADO_TRABAJANDO = 25.0
DURACION_ESTADO_DESCANSO_CORTO = 5.0
DURACION_ESTADO_DESCANSO_LARGO = 30.0


class EstadoPomodoro(object):

    pass

class EstadoPomodoroParado(EstadoPomodoro):

    def getNombre(self):
        return NOMBRE_ESTADO_PARADO

    def getDuracion(self):
        return DURACION_ESTADO_PARADO

class EstadoPomodoroTrabajando(EstadoPomodoro):

    def getNombre(self):
        return NOMBRE_ESTADO_TRABAJANDO

    def getDuracion(self):
        return DURACION_ESTADO_TRABAJANDO

class EstadoPomodoroDescansoCorto(EstadoPomodoro):

    def getNombre(self):
        return NOMBRE_ESTADO_DESCANSO_CORTO

    def getDuracion(self):
        return DURACION_ESTADO_DESCANSO_CORTO

class EstadoPomodoroDescansoLargo(EstadoPomodoro):

    def getNombre(self):
        return NOMBRE_ESTADO_DESCANSO_LARGO

    def getDuracion(self):
        return DURACION_ESTADO_DESCANSO_LARGO
    
if __name__ == "__main__":
    print "Hello World"
