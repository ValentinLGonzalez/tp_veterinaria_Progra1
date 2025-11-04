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

def is_valid_pet_weigth(weigth):
    if weigth.isdigit():
        return float(weigth) > 0
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