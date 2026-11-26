import unittest
from calc import add, divide, subtract


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(7, 3), 4)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
