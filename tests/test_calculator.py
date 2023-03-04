import unittest
from calculator_class import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()

    # test for addition
    def test_addition(self):
        self.assertEqual(self.c.add(2, 3), 5)
        self.assertEqual(self.c.add(0, 0), 0)
        self.assertEqual(self.c.add(-2, -3), -5)

    # test for subtraction
    def test_subtraction(self):
        self.assertEqual(self.c.subtract(5, 2), 3)
        self.assertEqual(self.c.subtract(2, 5), -3)
        self.assertEqual(self.c.subtract(0, 0), 0)

    #  test for multiplication
    def test_multiplication(self):
        self.assertEqual(self.c.multiply(4, 6), 24)
        self.assertEqual(self.c.multiply(0, 10), 0)
        self.assertEqual(self.c.multiply(-2, 3), -6)

    # test for multiplication
    def test_division(self):
        self.assertEqual(self.c.divide(8, 4), 2.0)
        self.assertRaises(ValueError, self.c.divide, 8, 0)
        self.assertAlmostEqual(self.c.divide(3, 2), 1.5, places=2)

if __name__ == '__main__':
    unittest.main()
