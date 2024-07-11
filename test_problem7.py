from problem7 import validate_email
# Test suite
def test_validate_email():
    # Valid email addresses
    assert validate_email("johndoe@domainsample.com") == True
    assert validate_email("john.doe@domainsample.net") == True
    assert validate_email("john.doe43@domainsample.co.uk") == True
    assert validate_email("john.doe+spamfilter@domainsample.co.uk") == True

    # Invalid email addresses
    assert validate_email("@domainsample.com") == False
    assert validate_email("johndoedomainsample.com") == False
    assert validate_email("john.doe@.net") == False
    assert validate_email("john.doe43@domainsample") == False

    print("All tests passed!")

# Run the test suite
if __name__ == "__main__":
    test_validate_email()