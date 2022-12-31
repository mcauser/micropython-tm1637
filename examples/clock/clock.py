#!/usr/bin/env python3

from time import sleep, localtime

from tm1637 import TM1637

DIO = 0
CLK = 1


class Clock:
    def __init__(self, tm_instance):
        self.tm = tm_instance
        self.show_colon = False

    def run(self):
        while True:
            t = localtime()
            self.show_colon = not self.show_colon
            tm.numbers(t.tm_hour, t.tm_min, self.show_colon)
            sleep(1)


if __name__ == '__main__':
    tm = TM1637(CLK, DIO)
    tm.brightness(1)

    clock = Clock(tm)
    clock.run()
