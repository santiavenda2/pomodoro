__author__ = "santiago"
__date__ = "$21/09/2011 17:40:19$"

import time
from progressbar import Bar, FormatLabel, Percentage, ProgressBar, Timer

SEGUNDOS_EN_MINUTO = 60
SEGUNDOS_EN_HORA = 3600


class Temporizador(object):

    def __init__(self, descripcion=""):
        self._duracion = 0
        self._restante = 0
        self._descripcion = descripcion

    def set_duracion(self, duracion_en_segundos):
        self._duracion = duracion_en_segundos
        self._restante = duracion_en_segundos
        self.pbar = ProgressBar(widgets=[self._descripcion, Percentage(),
            Bar(marker='=', left='[', right=']'), Timer()],
            maxval=self._duracion).start()

    def iniciar_cuenta_regresiva(self):
        while (self._restante > 0):
            time.sleep(1.0)
            self._restante -= 1
            self.pbar.update(self._duracion - self._restante)

        self.pbar.finish()


if __name__ == "__main__":
    temporizador = Temporizador("Prueba")
    temporizador.set_duracion(5)
    temporizador.iniciar_cuenta_regresiva()


