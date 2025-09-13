import re
# from utils.validations import is_not_a_number

def is_valid_matricula(matricula):
    """
        Validates if a text string has the matricula format (MN + 5 digits)
    Args:
        matricula: The text string to validate

    Returns:
        True if the string meets the format, False otherwise
    """
    return bool(re.fullmatch('^MN[0-9]{5}$', matricula))

def is_valid_name(input):
    """
        Validates if a text string has the input format only alphanimeric chars
    Args:
        input: The text string to validate

    Returns:
        True if the string meets the format, False otherwise
    """
    return bool(re.fullmatch(r'^[A-Za-z]+$', input))