import re

def is_valid_name(input):
    """
        Validates if a text string has the input format only alphanimeric chars
    Args:
        input: The text string to validate

    Returns:
        True if the string meets the format, False otherwise
    """
    return bool(re.fullmatch(r'^[A-Za-z]+$', input))
