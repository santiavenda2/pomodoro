import unittest

import pomodoropy.temporizador as temp
import timeit


class  Temporizador_TestCase(unittest.TestCase):
#    def setUp(self):
#        self.foo = Temporizador_()
#

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None
#
#    def test_precision_de_temporizador_(self):
#        duracion = 5.0
#        precision = 0.01
#        t = timeit.Timer('temporizador.iniciar_cuenta_regresiva()',
#            "from pomodoropy.temporizador import Temporizador ; \
#            temporizador = Temporizador(); \
#            temporizador.set_duracion(%f)"%duracion)
#
#        tiempos = t.repeat(repeat=10, number=1)
#        for tiempo in tiempos:
#            self.assertLessEqual(abs(tiempo - duracion), precision)

    def test_formatear_hora_0_segundos(self):
        h, m, s = temp.formatear_tiempo_restante(0)
        self.assertEqual(h, 0)
        self.assertEqual(m, 0)
        self.assertEqual(s, 0)

    def test_formatear_hora_10_segundos(self):
        h, m, s = temp.formatear_tiempo_restante(10)
        self.assertEqual(h, 0)
        self.assertEqual(m, 0)
        self.assertEqual(s, 10)

    def test_formatear_hora_60_segundos(self):
        h, m, s = temp.formatear_tiempo_restante(60)
        self.assertEqual(h, 0)
        self.assertEqual(m, 1)
        self.assertEqual(s, 0)

    def test_formatear_hora_70_segundos(self):
        h, m, s = temp.formatear_tiempo_restante(70)
        self.assertEqual(h, 0)
        self.assertEqual(m, 1)
        self.assertEqual(s, 10)

    def test_formatear_hora_3670_segundos(self):
        h, m, s = temp.formatear_tiempo_restante(3670)
        self.assertEqual(h, 1)
        self.assertEqual(m, 1)
        self.assertEqual(s, 10)

if __name__ == '__main__':
    testLoader = unittest.TestLoader()
    suite = testLoader.loadTestsFromTestCase(Temporizador_TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
