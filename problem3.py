import statistics

def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{filename}' does not exist.")
    except ValueError:
        raise ValueError(f"Error: The file '{filename}' contains non-integer values.")

def compute_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    try:
        mode = statistics.mode(data)
    except statistics.StatisticsError:
        mode = "No unique mode"
    variance = statistics.variance(data)
    std_dev = statistics.stdev(data)
    return mean, median, mode, variance, std_dev

def print_statistics(mean, median, mode, variance, std_dev):
    print(f"mean: {mean}")
    print(f"median: {median}")
    print(f"mode: {mode}")
    print(f"variance: {variance}")
    print(f"standard deviation: {std_dev}")
