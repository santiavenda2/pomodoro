import sys
import time

CARACTER_INICIO_BARRA = '['
CARACTER_FIN_BARRA = ']'
CARACTER_BARRA = '='
CARACTER_ESPACIO = ' '
CARACTER_BORRADO_DE_LINEA = chr(27) + '[2K' + chr(27)+'[G'
SLEEP_TIME = 0.0000001
class Bar:
    """Clase que crea una barra de progreso con una longitud determinada"""

    def __init__(self, titulo="", longitud=100):
        ''' Inicializo las variables '''
        self._titulo = titulo
        self._longitud = longitud
        self._barras = 0
        self._blancos = 0
        self._porcentaje = 0
            
    def set_porcentaje(self, porcentaje, mensaje=""):
        ''' Seteo el porcentaje actual y muestro la barra de progreso'''
        if (porcentaje > 100):
            self._porcentaje = 100
        elif (porcentaje < 0):
            self._porcentaje = 0
        else:    
            self._porcentaje = porcentaje

        self._barras = int(self._longitud*self._porcentaje/100)
        self._blancos = self._longitud-self._barras
        self.show(mensaje)

    def show(self, mensaje):
        ''' Muestro por consola la barra '''
        sys.stdout.flush()
        sys.stdout.write(CARACTER_BORRADO_DE_LINEA)
        barra = self.armar_barra()
        sys.stdout.write(barra)
        sys.stdout.write(mensaje)
        time.sleep(SLEEP_TIME)

    def armar_barra(self):
        """Armo la barra de progreso"""
        barra = self._titulo + ' '
        barra += CARACTER_INICIO_BARRA
        barra += self._barras*CARACTER_BARRA
        barra += '>'
        barra += self._blancos*CARACTER_ESPACIO
        barra += CARACTER_FIN_BARRA
        return barra
        
    def unshow(self):
        ''' Finaliza el mostrado '''
        self.set_porcentaje(100)
        sys.stdout.write('\n')

if __name__ == "__main__":
    b = Bar(titulo="Principal", longitud=50)

    for i in range(100):
        time.sleep(0.1)
        b.set_porcentaje(i, mensaje=(" %02ld"%i)+"%")
    b.unshow()
