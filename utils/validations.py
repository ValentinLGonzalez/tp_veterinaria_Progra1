import re

def is_not_a_number(string):
    """Checks if a string contains only letters (no numbers or symbols).

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string contains only letters, False otherwise.
    """
    return bool(re.fullmatch(r"[A-Za-z]+", string))

def is_valid_email(email):
    """ Validates if a string is a valid email address.
    
    This function uses a regular expression to check if the input string
    matches a common email format, including a username, an "@" symbol,
    a domain, and a top-level domain.

    Args:
        email (str): The string to be validated as an email address.

    Returns:
        bool: True if the string is a valid email, False otherwise.
    """
    return bool(re.fullmatch(r'^[\w\.-_]+@[\w\.-]+\.[A-Za-z]{2,3}$', email))

def is_valid_dni(dni):
    """ Validates if a string is a valid DNI (Argentine ID number) format.

    This function checks if the input string consists of either 7 or 8 digits,
    which is the standard format for an Argentine DNI.

    Args:
        dni (str): The string to be validated as a DNI.

    Returns:
        bool: True if the string is a valid DNI, False otherwise.
    """
    return bool(re.fullmatch(r'^([0-9]{8}|[0-9]{7})$', dni))

