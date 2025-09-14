import re

def isNotANumer(string):
    """Checks if a string contains only letters (no numbers or symbols).

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string contains only letters, False otherwise.
    """
    return bool(re.fullmatch(r"[A-Za-z]+", string))

def is_valid_pet_age(age_text):
    """
    Checks if the pet age is a positive integer (> 0).

    Args:
        age_text (str): The input to validate (usually read from console).

    Returns:
        bool: True if age_text represents an integer greater than 0, False otherwise.
    """
    # Accept only digits (no signs, no decimals) and greater than zero
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

# read pet age (must be > 0)
is_valid = False
while not is_valid:
    input_age = input("Introduzca una edad de la mascota valida (> 0): ")
    if is_valid_pet_age(input_age):
        pet_age = int(input_age)
        is_valid = True
    else:
        print("Edad no valida. Por favor, introduzca un numero entero.")

# read pet gender (must be Hembra/Macho)
is_valid = False
while not is_valid:
    input_gender = input("Introduzca el genero de la mascota (Hembra/Macho): ")
    if is_valid_gender(input_gender):
        pet_gender = input_gender.upper()
        is_valid = True
    else:
        print("Genero invalido. Por favor, introduzca'Hembra' or 'Macho'.")

