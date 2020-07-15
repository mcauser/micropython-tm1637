import unittest

import tm1637

CLK = 1
DIO = 0


class TestTm1637(unittest.TestCase):
    def setUp(self):
        self.tm = tm1637.TM1637(clk=CLK, dio=DIO)

    def test_encode_digit(self):
        self.assertEqual(self.tm.encode_digit(0), 63)
        self.assertEqual(self.tm.encode_digit(8), 127)
        self.assertEqual(self.tm.encode_digit(0x0f), 113)
        self.assertEqual(self.tm.encode_digit(15), 113)
        # 15 or 0x0f generates a segment that can output a F character
        self.assertEqual(self.tm.encode_digit(15), 113)
        self.assertEqual(self.tm.encode_digit(0x0f), 113)

    def test_encode_string(self):
        self.assertEqual(self.tm.encode_string('   1'),
                         bytearray(b'\x00\x00\x00\x06'))
        self.assertEqual(self.tm.encode_string('2   '),
                         bytearray(b'[\x00\x00\x00'))
        self.assertEqual(self.tm.encode_string('1234'), bytearray(b'\x06[Of'))
        self.assertEqual(self.tm.encode_string('-12-'), bytearray(b'@\x06[@'))
        self.assertEqual(self.tm.encode_string('cafe'), bytearray(b'9wqy'))
        self.assertEqual(self.tm.encode_string('CAFE'), bytearray(b'9wqy'))
        self.assertEqual(self.tm.encode_string('a'), bytearray(b'w'))
        self.assertEqual(self.tm.encode_string('ab'), bytearray(b'w|'))

    def test_encode_char(self):
        self.assertEqual(self.tm.encode_char('1'), 6)
        self.assertEqual(self.tm.encode_char('9'), 111)
        self.assertEqual(self.tm.encode_char('-'), 64)
        self.assertEqual(self.tm.encode_char('a'), 119)
        self.assertEqual(self.tm.encode_char('F'), 113)


if __name__ == '__main__':
    unittest.main()
