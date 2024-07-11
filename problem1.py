def fahrenheit_to_celsius(fahrenheit):
    if isinstance(fahrenheit, (int, float)):
        return (fahrenheit - 32) * 5.0 / 9.0
    else:
        raise ValueError("Input must be a numeric value")

def get_user_input():
    while True:
        user_input = input("Enter temperature in Fahrenheit: ")
        try:
            fahrenheit = float(user_input)
            return fahrenheit
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    print("Temperature Converter: Fahrenheit to Celsius")
    fahrenheit = get_user_input()
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit is {celsius:.2f} Celsius")

if __name__ == "__main__":
    main()


