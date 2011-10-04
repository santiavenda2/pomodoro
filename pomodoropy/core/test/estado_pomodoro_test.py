import unittest

from pomodoropy.estados import EstadoPomodoroParado, EstadoPomodoroTrabajando, EstadoPomodoroDescansoCorto,  EstadoPomodoroDescansoLargo

ESTADOS_DEFINIDOS = [EstadoPomodoroParado(), EstadoPomodoroTrabajando(), EstadoPomodoroDescansoCorto(), EstadoPomodoroDescansoLargo()]

class  Estado_pomodoro_TestCase(unittest.TestCase):

    def test_estado_pomodoro_tiene_un_nombre(self):
        for estado in ESTADOS_DEFINIDOS:
            assert len(estado.getNombre()) > 0

    def test_estado_pomodoro_tiene_una_duracion_mayor_o_igual_a_cero(self):
        for estado in ESTADOS_DEFINIDOS:
            assert estado.getDuracion() >= 0.0


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Estado_pomodoro_TestCase)

    unittest.TextTestRunner(verbosity=2).run(suite)

