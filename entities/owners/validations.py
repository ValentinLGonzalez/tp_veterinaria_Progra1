import re

def is_valid_name(input):
    """
    si el string matchea el formato, true. sino false
    """
    return bool(re.fullmatch(r'^[A-Za-z]+$', input))
