import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(-5, -2), -3)
        self.assertEqual(subtract(0, 3), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
            # Valid base and argument
        result = logarithm(8, 2)
        self.assertAlmostEqual(result, 3.0, places=4)

    def test_log_invalid_base(self):
            # log with invalid base or argument should raise ValueError
        with self.assertRaises(ValueError):
            logarithm(-5, 2)
        with self.assertRaises(ValueError):
            logarithm(5, 1)
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(8, 2), 4.0)
        self.assertAlmostEqual(div(-9, 3), -3.0)
        self.assertAlmostEqual(div(7, 2), 3.5)

    def test_log_invalid_argument(self):
        # log(a, b) should raise ValueError if 'a' <= 0
        with self.assertRaises(ValueError):
            logarithm(-10, 2)
        with self.assertRaises(ValueError):
            logarithm(0, 2)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)  # negatives still valid

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-9)


# Do not touch this
if __name__ == "__main__":
    unittest.main()