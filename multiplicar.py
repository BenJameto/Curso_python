def multiplicar(num1, num2):
    return num1*num2

resultado = multiplicar(4,4)
print(resultado)


import unittest
class pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(multiplicar(4,6),24)
        self.assertEqual(multiplicar(4,6),25)

if __name__ == '__main__':
    unittest.main()