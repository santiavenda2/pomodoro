
import unittest

import pomodoropy.pomodoro as pomodoro
import pomodoropy.estados as estados


class Pomodoro_TestCase(unittest.TestCase):

    def setUp(self):
        self.pomodoroTimer = pomodoro.ProcesoPomodoro()

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_pomodoro_timer_se_crea_en_estado_parado(self):
        estadoEsperado = estados.ESTADO_PARADO
        self.assertEqual(self.pomodoroTimer.get_estado(), estadoEsperado)

    def test_pomodoro_timer_se_puede_iniciar(self):
        self.pomodoroTimer.start()

    def test_pomodoro_timer_inicia_en_estado_trabajando(self):
        self.pomodoroTimer.start()
        estado = self.pomodoroTimer.get_estado()
        estadoEsperado = estados.ESTADO_TRABAJANDO
        self.assertEqual(estado, estadoEsperado)

    def test_pomodoro_timer_puede_cambiar_a_siguiente_estado(self):
        self.pomodoroTimer.start()
        self.pomodoroTimer.avanzar_estado()
        estado = self.pomodoroTimer.get_estado()
        estadoEsperado = estados.ESTADO_DESCANSO_CORTO
        self.assertEqual(estado, estadoEsperado)

    def test_pomodoro_timer_secuencia_de_estados(self):
        self.pomodoroTimer.start()
        self.assertEqual(self.pomodoroTimer.get_estado(),
                            estados.ESTADO_TRABAJANDO,
                            "El timer debe iniciar en estado: %s"%
                            estados.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_DESCANSO_CORTO,
                            "El segundo estado debe ser %s"%estados.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_TRABAJANDO,
                            "El tercer estado debe ser %s"%estados.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_DESCANSO_CORTO,
                            "El cuarto estado debe ser %s"%estados.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_TRABAJANDO,
                            "El quinto estado debe ser %s"%estados.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_DESCANSO_CORTO,
                            "El sexto estado debe ser %s"%estados.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_TRABAJANDO,
                            "El septimo estado debe ser %s"%estados.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_DESCANSO_LARGO,
                            "El octavo estado debe ser %s"%estados.ESTADO_DESCANSO_LARGO)

    def test_pomodoro_timer_ciclo_terminado(self):
        self.pomodoroTimer.start()
        for i in range(8):
            self.pomodoroTimer.avanzar_estado()

        self.pomodoroTimer.get_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_TRABAJANDO,
                            "Al Finalizar el descanso largo el timer debe volver al estado inicial: %s"
                            %estados.ESTADO_TRABAJANDO)

        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_DESCANSO_CORTO,
                            "El segundo estado debe ser %s"%estados.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_TRABAJANDO,
                            "El tercer estado debe ser %s"%estados.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_DESCANSO_CORTO,
                            "El cuarto estado debe ser %s"%estados.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_TRABAJANDO,
                            "El quinto estado debe ser %s"%estados.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_DESCANSO_CORTO,
                            "El sexto estado debe ser %s"%estados.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_TRABAJANDO,
                            "El septimo estado debe ser %s"%estados.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzar_estado()
        self.assertEqual(self.pomodoroTimer.get_estado(), estados.ESTADO_DESCANSO_LARGO,
                            "El octavo estado debe ser %s"%estados.ESTADO_DESCANSO_LARGO)


if __name__ == '__main__':
    testLoader = unittest.TestLoader()
    suite = testLoader.loadTestsFromTestCase(Pomodoro_TestCase)

    unittest.TextTestRunner(verbosity=2).run(suite)


