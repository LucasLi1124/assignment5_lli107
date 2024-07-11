import unittest
from problem2 import greatest_common_divisor


class TestGCD(unittest.TestCase):
    def test_gcd_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(100, 25), 25)
        self.assertEqual(greatest_common_divisor(17, 13), 1)

    def test_gcd_with_zero(self):
        self.assertEqual(greatest_common_divisor(10, 0), 10)
        self.assertEqual(greatest_common_divisor(0, 10), 10)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_gcd_same_numbers(self):
        self.assertEqual(greatest_common_divisor(7, 7), 7)
        self.assertEqual(greatest_common_divisor(100, 100), 100)

    def test_gcd_one(self):
        self.assertEqual(greatest_common_divisor(1, 1), 1)
        self.assertEqual(greatest_common_divisor(1, 100), 1)
        self.assertEqual(greatest_common_divisor(100, 1), 1)

    def test_gcd_large_numbers(self):
        self.assertEqual(greatest_common_divisor(123456, 7890), 6)
        self.assertEqual(greatest_common_divisor(987654, 123456), 6)


if __name__ == "__main__":
    unittest.main()
