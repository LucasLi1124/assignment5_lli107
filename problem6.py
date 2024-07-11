import re

def rename(original):
    """
    Renames a file from MM-DD-YYYY format to DD-MM-YYYY format.
    The file extension is preserved.
    """
    # Regular expression to match the MM-DD-YYYY format
    match = re.match(r'(\d{2})-(\d{2})-(\d{4})(\.\w+)', original)
    if match:
        # Extract the components of the date and the file extension
        month, day, year, extension = match.groups()
        # Reformat to DD-MM-YYYY
        new_filename = f"{day}-{month}-{year}{extension}"
        return new_filename
    else:
        # If the pattern doesn't match, return the original filename
        return original



assert rename("10-31-2019.jpg") == "31-10-2019.jpg"
assert rename("10-31-2019.jpg") != "31-10-2019"
assert rename("12-25-2020.png") == "25-12-2020.png"
assert rename("01-01-2021.gif") == "01-01-2021.gif"
assert rename("invalid-file-name.jpg") == "invalid-file-name.jpg"

# Example usage
filenames = [
    "10-31-2019.jpg",
    "12-25-2020.png",
    "01-01-2021.gif",
    "07-04-2023.jpeg",
    "invalid-file-name.jpg"
]

for filename in filenames:
    print(f"Original: {filename} -> Renamed: {rename(filename)}")

