#!/usr/bin/env python2.7
__author__ = "santiago"
__date__ = "$15/09/2011 23:16:56$"

from core import ControladorPomodoro


def main():
    print "Main Pomodoro Timer"
    controladorPomodoro = ControladorPomodoro()
    controladorPomodoro.iniciar_pomodoro()
    for i in range(16):
        controladorPomodoro.avanzar_estado()

if __name__ == "__main__":
    main()


