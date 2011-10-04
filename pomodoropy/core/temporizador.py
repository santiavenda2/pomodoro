__author__ = "santiago"
__date__ = "$21/09/2011 17:40:19$"

import time


class Temporizador(object):

    def __init__(self):
        self._duracion = 0
        self._restante = 0

    def set_duracion(self, duracion_en_segundos):
        self._duracion = duracion_en_segundos
        self._restante = duracion_en_segundos

    def iniciar_cuenta_regresiva(self):
        print self.mostrar_restante()
        while (self._restante > 0):
            time.sleep(1.0)
            self._restante -= 1
            print self.mostrar_restante()

    def mostrar_restante(self):
        h, m, s = formatear_tiempo_restante(self._restante)
        return "%02d:%02d" % (m, s)

#-------------------------------------------------#
#            Funciones Auxiliares                 #
#-------------------------------------------------#
SEGUNDOS_EN_MINUTO = 60
SEGUNDOS_EN_HORA = 3600


def formatear_tiempo_restante(restante_en_segundos):
    horas = restante_en_segundos / SEGUNDOS_EN_HORA
    minutos = (restante_en_segundos % SEGUNDOS_EN_HORA) / SEGUNDOS_EN_MINUTO
    segundos = (restante_en_segundos % SEGUNDOS_EN_HORA) % SEGUNDOS_EN_MINUTO
    return horas, minutos, segundos

if __name__ == "__main__":
    temporizador = Temporizador()
    temporizador.set_duracion(5)
    temporizador.iniciar_cuenta_regresiva()


