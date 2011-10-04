import unittest

import pomodoropy.estados as estados


class EstadoPomodoro_TestCase(unittest.TestCase):

    def test_estado_pomodoro_tiene_un_nombre(self):
        for estado in estados.ESTADOS_DEFINIDOS:
            assert len(estado.get_nombre()) > 0

    def test_estado_pomodoro_tiene_una_duracion_mayor_o_igual_a_cero(self):
        for estado in  estados.ESTADOS_DEFINIDOS:
            assert estado.get_duracion() >= 0.0


if __name__ == '__main__':
    testLoader = unittest.TestLoader()
    suite = testLoader.loadTestsFromTestCase(EstadoPomodoro_TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
