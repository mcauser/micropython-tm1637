# WeMos D1 Mini -- Seeed Studio Grove 4 Digit Display
# D4 (GPIO2) ----- CLK
# D3 (GPIO0) ----- DIO
# 3V3 ------------ VCC
# G -------------- GND

# https://www.seeedstudio.com/Grove-4-Digit-Display-p-1198.html
# http://wiki.seeed.cc/Grove-4-Digit_Display/

# this module has a 4-digit 7-segment display with two dots between the 2nd and 3rd segments, referred to as the colon

import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))

# dim
tm.brightness(0)

# 1234
tm.write([0x06, 0x5B, 0x4F, 0x66])

# 12:34
tm.write([0x06, 0x5B | 128, 0x4F, 0x66])

# cool
tm.show('cool')
