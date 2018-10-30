# WeMos D1 Mini -- RobotDyn 6-digit LED Display Tube
# D4 (GPIO2) ----- CLK
# D3 (GPIO0) ----- DIO
# 3V3 ------------ VCC
# G -------------- GND

# https://www.aliexpress.com/store/product/6-Digit-LED-0-36-Display-Tube-decimal-7-segments-GREEN-TM1637-disp-size-46x14mm/1950989_32800127265.html

# this module has two 3-digit 7-segment displays with decimal points
# they are both wired backwards!

# the TM1637 driver supports 6 digits (called grids in the datasheet)
# on a 4 digit display, digits left to right are typically controlled by grid1, grid2, grid3, grid4
# on this 6 digit display, digits left to right are grid3, grid2, grid1, grid6, grid5, grid4
# this means the write function needs to shiffle the order to match

import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(0))

# dim
tm.brightness(0)

# expected: 012345
# actual:   210543
tm.write([0x3F,0x06,0x5B,0x4F,0x66,0x6D])

# data = 012345
data = [0x3F,0x06,0x5B,0x4F,0x66,0x6D]
# expected: 012345
# actual:   012345
tm.write([data[2], data[1], data[0], data[5], data[4], data[3]])

# expected: abcdef
# actual:   cbafed
tm.show('abcdef')

# swap segments 0,2 and segments 3,5
def swap(segs):
	length = len(segs)
	if length == 4 or length == 5:
		segs.extend(bytearray([0] * (6 - length)))
	segs[0], segs[2] = segs[2], segs[0]
	if length >= 4:
		segs[3], segs[5] = segs[5], segs[3]
	return segs

# data = 012345
data = [0x3F,0x06,0x5B,0x4F,0x66,0x6D]
# expected: 012345
# actual:   012345
tm.write(swap(data))

# data = notbad
data = [84, 63, 120, 124, 119, 94]
# expected: notbad
# actual:   notbad
tm.write(swap(data))

# expected: abcdef
# actual:   abcdef
tm.write(swap(tm.encode_string('abcdef')))
