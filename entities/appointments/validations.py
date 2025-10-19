import re

#CONSTANTS
OPEN_WORK_HOUR = '08:00'
CLOSE_WORK_HOUR = '20:00'

#VALIDATIONS
def is_valid_appointment_time(time):
    """Validates that the time has the HH:MM format, within work hours.

    Args:
        time (str): The input time string.

    Returns:
        bool: True if valid, False otherwise.
    """
    if len(time) != 5 or time[2] != ":":
        print("Error: el formato de hora debe ser HH:MM.")
        return False
    
    hh, mm = time[:2], time[3:]

    if not (hh.isdigit() and mm.isdigit()):
        print("Error: la hora y minutos deben ser números.")
        return False

    hour, minute = int(hh), int(mm)

    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        print("Error: hora o minutos fuera de rango.")
        return False

    open_hour, open_minute = map(int, OPEN_WORK_HOUR.split(":"))
    close_hour, close_minute = map(int, CLOSE_WORK_HOUR.split(":"))

    if not ((hour > open_hour or (hour == open_hour and minute >= open_minute)) and
            (hour < close_hour or (hour == close_hour and minute <= close_minute))):
        print(f"Error: El horario debe estar entre {OPEN_WORK_HOUR} y {CLOSE_WORK_HOUR}.")
        return False

    return True

def is_valid_appointment_date(date):
    """Validates that the date has the DD.MM.YYYY format.

    Args:
        date (str): The input date string.

    Returns:
        bool: True if valid, False otherwise.
    """

    return bool(re.fullmatch(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$", date))