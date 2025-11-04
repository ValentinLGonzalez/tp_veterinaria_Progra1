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
    return bool(re.fullmatch(r'^[\w\.-_]+@[\w\.-]+\.[A-Za-z]{2,3}$', email))

def is_valid_dni(dni):
    return bool(re.fullmatch(r'^([0-9]{8}|[0-9]{7})$', dni))

def is_valid_phone(phone):
    return bool(re.fullmatch(r'^11[0-9]{8}$', phone))
