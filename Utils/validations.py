import re

def isNotANumer(string):
    """Checks if a string contains only letters (no numbers or symbols).

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string contains only letters, False otherwise.
    """
    return bool(re.fullmatch(r"[A-Za-z]+", string))