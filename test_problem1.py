import unittest
from problem1 import fahrenheit_to_celsius
class TestTemperatureConverter(unittest.TestCase):

    def test_fahrenheit_to_celsius(self):
        # Test known conversions
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.00, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.00, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.00, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.00, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(0), -17.78, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(100), 37.78, places=2)

    def test_fahrenheit_to_celsius_edge_cases(self):
        # Test edge cases
        self.assertAlmostEqual(fahrenheit_to_celsius(0.0001), -17.78, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(-0.0001), -17.78, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(1e-9), -17.78, places=2)
        self.assertAlmostEqual(fahrenheit_to_celsius(-1e-9), -17.78, places=2)

    def test_invalid_user_input(self):
        # Test invalid inputs
        with self.assertRaises(ValueError):
            fahrenheit_to_celsius("not a number")

        with self.assertRaises(ValueError):
            fahrenheit_to_celsius(None)

        with self.assertRaises(ValueError):
            fahrenheit_to_celsius("")

if __name__ == "__main__":
    unittest.main()
