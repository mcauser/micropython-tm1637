# MicroPython TM1637 quad 7-segment LED display driver

from machine import Pin
from time import sleep_us

_CMD_SET1 = const(64)  # 0x40 data set
_CMD_SET2 = const(192) # 0xC0 address command set
_CMD_SET3 = const(128) # 0x80 data control command set

# 0-9, a-f, blank, dash
_SEGMENTS = [63,6,91,79,102,109,125,7,127,111,119,124,57,94,121,113,0,64]

class TM1637(object):
    """Library for the quad 7-segment LED display modules based on the TM1637
    LED driver."""
    def __init__(self, clk, dio, brightness=7):
        self.clk = clk
        self.dio = dio

        if not 0 <= brightness <= 7:
            raise ValueError("Brightness out of range")
        self._brightness = brightness

        self.clk.init(Pin.IN)
        self.dio.init(Pin.IN)
        self.clk(0)
        self.dio(0)

    def _start(self):
        self.dio.init(Pin.OUT)
        sleep_us(50)

    def _stop(self):
        self.dio.init(Pin.OUT)
        sleep_us(50)
        self.clk.init(Pin.IN)
        sleep_us(50)
        self.dio.init(Pin.IN)
        sleep_us(50)

    def _write_comm1(self):
        self._start()
        self._write_byte(_CMD_SET1)
        self._stop()

    def _write_comm3(self):
        self._start()
        self._write_byte(_CMD_SET3 + self._brightness + 7)
        self._stop()

    def _write_byte(self, b):
        # send each bit
        for i in range(8):
            self.clk.init(Pin.OUT)
            sleep_us(50)
            self.dio.init(Pin.IN if b & 1 else Pin.OUT)
            sleep_us(50)
            self.clk.init(Pin.IN)
            sleep_us(50)
            b >>= 1
        self.clk.init(Pin.OUT)
        sleep_us(50)
        self.clk.init(Pin.IN)
        sleep_us(50)
        self.clk.init(Pin.OUT)
        sleep_us(50)

    def brightness(self, val=None):
        """Set the display brightness 0-7."""
        if val is None:
            return self._brightness
        if not 0 <= val <= 7:
            raise ValueError("Brightness out of range")
        self._brightness = val
        self._write_comm1()
        self._write_comm3()

    def write(self, segments, pos=0):
        """Display up to 4 segments moving right from a given position.
        The MSB in the 2nd segment controls the colon between the 2nd
        and 3rd segments."""
        if not 0 <= pos <= 3:
            raise ValueError("Position out of range")
        self._write_comm1()

        # write COMM2 + first digit address
        self._start()
        self._write_byte(_CMD_SET2 + pos)
        for seg in segments:
            self._write_byte(seg)
        self._stop()
        self._write_comm3()

    def encode_digit(self, digit):
        """Convert a character 0-9, a-f to a segment."""
        return _SEGMENTS[digit & 0x0f]

    def encode_string(self, string):
        """Convert an up to 4 character length string containing 0-9, a-f,
        space, dash to an array of segments, matching the length of the
        source string."""
        segments = bytearray(4)
        for i in range(0, min(4, len(string))):
            segments[i] = self.encode_char(string[i])
        return segments

    def encode_char(self, char):
        """Convert a character 0-9, a-f, space or dash to a segment."""
        o = ord(char)
        # space
        if o == 32:
            return _SEGMENTS[16]
        # dash
        if o == 45:
            return _SEGMENTS[17]
        # uppercase A-F
        if o >= 65 and o <= 70:
            return _SEGMENTS[o-55]
        # lowercase a-f
        if o >= 97 and o <= 102:
            return _SEGMENTS[o-87]
        # 0-9
        if o >= 48 and o <= 57:
            return _SEGMENTS[o-48]
        raise ValueError("Character out of range")

    def hex(self, val):
        """Display a hex value 0x0000 through 0xffff, right aligned."""
        string = '{:04x}'.format(val & 0xffff)
        self.write(self.encode_string(string))

    def number(self, num):
        """Display a numeric value -999 through 9999, right aligned."""
        # limit to range -999 to 9999
        num = max(-999, min(num, 9999))
        string = '{0: >4d}'.format(num)
        self.write(self.encode_string(string))

    def numbers(self, num1, num2, colon=True):
        """Display two numeric values -9 through 99, with leading zeros
        and separated by a colon."""
        num1 = max(-9, min(num1, 99))
        num2 = max(-9, min(num2, 99))
        segments = self.encode_string('{0:0>2d}{1:0>2d}'.format(num1, num2))
        # colon on
        if colon:
            segments[1] |= 0x80
        self.write(segments)
