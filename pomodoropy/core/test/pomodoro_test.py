
import unittest

from  pomodoropy.PomodoroTimer import PomodoroTimer

class  Pomodoro_TestCase(unittest.TestCase):
    def setUp(self):
        self.pomodoroTimer = PomodoroTimer()
    

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_pomodoro_timer_se_crea_en_estado_parado(self):
        estadoEsperado = PomodoroTimer.ESTADO_PARADO
        self.assertEqual(self.pomodoroTimer.getEstado(), estadoEsperado)

    def test_pomodoro_timer_se_puede_iniciar(self):
        self.pomodoroTimer.start()

    def test_pomodoro_timer_inicia_en_estado_trabajando(self):
        self.pomodoroTimer.start()
        estado = self.pomodoroTimer.getEstado()
        estadoEsperado = PomodoroTimer.ESTADO_TRABAJANDO
        self.assertEqual(estado, estadoEsperado)

    def test_pomodoro_timer_cambiar_a_siguiente_estado(self):
        self.pomodoroTimer.start()
        self.pomodoroTimer.avanzarEstado()
        estado = self.pomodoroTimer.getEstado()
        estadoEsperado = PomodoroTimer.ESTADO_DESCANSO_CORTO
        self.assertEqual(estado, estadoEsperado)

    def test_pomodoro_timer_secuencia_de_estados(self):
        self.pomodoroTimer.start()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_TRABAJANDO,
                            "El timer debe iniciar en estado: "+PomodoroTimer.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_DESCANSO_CORTO,
                            "El segundo estado debe ser "+PomodoroTimer.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_TRABAJANDO,
                            "El tercer estado debe ser "+PomodoroTimer.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_DESCANSO_CORTO,
                            "El cuarto estado debe ser "+PomodoroTimer.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_TRABAJANDO,
                            "El quinto estado debe ser "+PomodoroTimer.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_DESCANSO_CORTO,
                            "El sexto estado debe ser "+PomodoroTimer.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_TRABAJANDO,
                            "El septimo estado debe ser "+PomodoroTimer.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_DESCANSO_LARGO,
                            "El octavo estado debe ser "+PomodoroTimer.ESTADO_DESCANSO_LARGO)

    def test_pomodoro_timer_ciclo_terminado(self):
        self.pomodoroTimer.start()
        for i in range(8):
            self.pomodoroTimer.avanzarEstado()

        self.pomodoroTimer.getEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_TRABAJANDO,
                            "Al Finalizar el descanso largo el timer debe volver al estado inicial"+PomodoroTimer.ESTADO_TRABAJANDO)

        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_DESCANSO_CORTO,
                            "El segundo estado debe ser "+PomodoroTimer.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_TRABAJANDO,
                            "El tercer estado debe ser "+PomodoroTimer.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_DESCANSO_CORTO,
                            "El cuarto estado debe ser "+PomodoroTimer.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_TRABAJANDO,
                            "El quinto estado debe ser "+PomodoroTimer.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_DESCANSO_CORTO,
                            "El sexto estado debe ser "+PomodoroTimer.ESTADO_DESCANSO_CORTO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_TRABAJANDO,
                            "El septimo estado debe ser "+PomodoroTimer.ESTADO_TRABAJANDO)
        self.pomodoroTimer.avanzarEstado()
        self.assertEqual(self.pomodoroTimer.getEstado(), PomodoroTimer.ESTADO_DESCANSO_LARGO,
                            "El octavo estado debe ser "+PomodoroTimer.ESTADO_DESCANSO_LARGO)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Pomodoro_TestCase)

    unittest.TextTestRunner(verbosity=2).run(suite)


