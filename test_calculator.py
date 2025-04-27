import unittest
from calculadora import somar, subtrair, multiplicar, dividir

class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)

    def test_subtrair(self):
        self.assertEqual(subtrair(5, 2), 3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 2), 8)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_zero(self):
        self.assertEqual(dividir(5, 0), "Erro: divisão por zero")

if __name__ == '__main__':
    unittest.main()
