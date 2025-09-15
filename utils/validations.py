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

def is_valid_pet_age(age_text):
    """
    Checks if the pet age is a positive integer (> 0).

    Args:
        age_text (str): The input to validate (usually read from console).

    Returns:
        bool: True if age_text represents an integer greater than 0, False otherwise.
    """
    if age_text.isdigit():
        return int(age_text) > 0
    return False

def is_valid_gender(gender_text):
    """
    Checks if the gender value is valid. Only 'Hembra' or 'Macho' are accepted.

    Args:
        gender_text (str): The input to validate (usually read from console).

    Returns:
        bool: True if the value is 'Hembra' or 'Macho' (case-insensitive), False otherwise.
    """
    if gender_text is None or len(gender_text) == 0:
        return False
    value = gender_text.upper()
    return value == "HEMBRA" or value == "MACHO"

def is_valid_phone(phone):
    return bool(re.fullmatch(r'^15[0-9]{8}$', phone))
