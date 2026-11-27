import unittest
from calc import add, divide, multiply, subtract


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(7, 3), 4)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_multiply_with_negative_number(self):
        self.assertEqual(multiply(-4, 3), -12)
        self.assertEqual(multiply(-4, -3), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, -5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
