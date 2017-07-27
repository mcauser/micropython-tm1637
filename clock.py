#!/usr/bin/env python3

from tm1637 import TM1637
from time import time, sleep, localtime

DIO=0
CLK=1

def show_clock(tm):
    t = localtime()
    sleep(1 - time() % 1)

    tm.numbers(t.tm_hour, t.tm_min, True)
    sleep(.5)
    tm.numbers(t.tm_hour, t.tm_min, False)

if __name__ == "__main__":
    print("\n")
    print("============================")
    print(" Starting clock application")
    print("============================")
    
    tm = TM1637(CLK, DIO)
    tm.brightness(1)
    
    while True:
        show_clock(tm)

