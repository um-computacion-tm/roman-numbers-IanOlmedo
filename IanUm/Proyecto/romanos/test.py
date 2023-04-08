import unittest
from romanos_a_decimal import romantoDec
from romans import decimal_to_roman

class TestRomantoDecimal(unittest.TestCase):
    def test_I(self):
        resultado = romantoDec("I")
        self.assertEqual(resultado, 1)
    def test_II(self):
        resultado = romantoDec("II")
        self.assertEqual(resultado, 2)
    def test_III(self):
        resultado = romantoDec("III")
        self.assertEqual(resultado, 3)
    def test_V(self):
        resultado = romantoDec("V")
        self.assertEqual(resultado, 5)
    def test_X(self):
        resultado = romantoDec("X")
        self.assertEqual(resultado, 10)
    def test_L(self):
        resultado = romantoDec("L")
        self.assertEqual(resultado, 50)
    def test_C(self):
        resultado = romantoDec("C")
        self.assertEqual(resultado, 100)
    def test_D(self):
        resultado = romantoDec("D")
        self.assertEqual(resultado, 500)
    def test_M(self):
        resultado = romantoDec("M")
        self.assertEqual(resultado, 1000)

class TestDecimalToRoman(unittest.TestCase):

    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')
    
    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, "IV")
    
    def test_seis(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, "VI")

    def test_siete(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, "VII")

    def test_ocho(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, "VIII")

    def test_nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, "IX")


if __name__ == "__main":
    unittest.main()