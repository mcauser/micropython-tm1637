# WeMos D1 Mini -- RobotDyn 4-digit LED Display Tube
# D4 (GPIO2) ----- CLK
# D3 (GPIO0) ----- DIO
# 3V3 ------------ VCC
# G -------------- GND

# https://www.aliexpress.com/store/product/4-Digit-LED-0-36-Display-Tube-decimal-7-segments-RED-TM1637-disp-size-30x14mm/1950989_32795908218.html

# this module has a 4-digit 7-segment display with decimal points

# the TM1637 driver supports 6 digits (called grids in the datasheet)
# on this display, digits left to right are controlled by grid1, grid2, grid3, grid4
# grid5 and grid6 are not connected

import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))

# dim
tm.brightness(0)

# 1234
tm.write([0x06, 0x5B, 0x4F, 0x66])

# 1.234
tm.write([0x06 | 128, 0x5B, 0x4F, 0x66])

# 12.34
tm.write([0x06, 0x5B | 128, 0x4F, 0x66])

# 1.2.3.4.
tm.write([0x06 | 128, 0x5B | 128, 0x4F | 128, 0x66 | 128])

# help
tm.show('help')
