import re

def validate_email(email):
    """
    Validates an email address based on the given rules.
    """
    # Regular expression pattern for a valid email address
    pattern = re.compile(
        r"^[A-Za-z0-9._%+-]{1,64}"    # Recipient name
        r"@"                           # @ symbol
        r"[A-Za-z0-9.-]{1,253}"        # Domain name
        r"\.[A-Za-z]{2,}$"             # Top-level domain
    )

    # Check if the email matches the pattern
    if pattern.match(email):
        return True
    else:
        return False


