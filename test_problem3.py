import unittest
import statistics
from problem3 import read_numbers_from_file, compute_statistics


class TestStatisticsModule(unittest.TestCase):

    def test_read_numbers_from_file(self):
        # Create a temporary file with known data for testing
        with open('test_numbers.txt', 'w') as f:
            f.write('\n'.join(['1', '2', '3', '4', '5']))

        # Test reading numbers from file
        expected = [1, 2, 3, 4, 5]
        result = read_numbers_from_file('test_numbers.txt')
        self.assertEqual(result, expected)

    def test_read_numbers_from_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_numbers_from_file('non_existent_file.txt')

    def test_read_numbers_from_file_value_error(self):
        # Create a temporary file with invalid data for testing
        with open('test_invalid_numbers.txt', 'w') as f:
            f.write('\n'.join(['1', 'two', '3']))

        with self.assertRaises(ValueError):
            read_numbers_from_file('test_invalid_numbers.txt')

    def test_compute_statistics(self):
        data = [1, 2, 3, 4, 5]
        expected_mean = statistics.mean(data)
        expected_median = statistics.median(data)
        expected_mode = statistics.mode(data)
        expected_variance = statistics.variance(data)
        expected_std_dev = statistics.stdev(data)

        mean, median, mode, variance, std_dev = compute_statistics(data)

        self.assertAlmostEqual(mean, expected_mean, places=2)
        self.assertAlmostEqual(median, expected_median, places=2)
        self.assertEqual(mode, expected_mode)  # Mode is an integer, not float
        self.assertAlmostEqual(variance, expected_variance, places=2)
        self.assertAlmostEqual(std_dev, expected_std_dev, places=2)

    def test_compute_statistics_no_mode(self):
        data = [1, 2, 2, 3, 3, 4, 5]
        expected_mean = statistics.mean(data)
        expected_median = statistics.median(data)
        try:
            expected_mode = statistics.mode(data)
        except statistics.StatisticsError:
            expected_mode = "No unique mode"
        expected_variance = statistics.variance(data)
        expected_std_dev = statistics.stdev(data)

        mean, median, mode, variance, std_dev = compute_statistics(data)

        self.assertAlmostEqual(mean, expected_mean, places=2)
        self.assertAlmostEqual(median, expected_median, places=2)
        self.assertEqual(mode, expected_mode)
        self.assertAlmostEqual(variance, expected_variance, places=2)
        self.assertAlmostEqual(std_dev, expected_std_dev, places=2)


if __name__ == "__main__":
    unittest.main()
