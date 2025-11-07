from utils.constants import HEADER_OWNER
from utils.entitiesHelper import get_next_id_by_file
from utils.filesHelper import append_line_to_file, read_file_csv_with, save_all_to_file, read_all_file_csv

file_name = "./data/owners.txt"

def owner_read_handler(entity, condition):
    """Filters an entity based on a given condition.

    This handler function evaluates a given entity against a condition function.
    If the condition is satisfied, the entity is returned. Otherwise, it
    returns False.

    Args:
        entity (Any): The entity object to be evaluated (e.g., an Owner instance).
        condition (callable): A function that takes the entity as its single
            argument and returns True if the condition is met, False otherwise.

    Returns:
        Any | bool: The original entity if the condition is met, otherwise False.
    """
    if condition(entity):
        return entity
    else:
        return False

def get_data_owner_by_dni(_dni):
    """Retrieves an active owner's data from the data source by their DNI.

    This function searches the owner data file for a specific owner
    identified by their DNI. It only considers owners who are marked
    as 'active'.

    Args:
        _dni (str): The DNI (National Identity Document) of the owner to retrieve.

    Returns:
        list: A list containing the row data of the found active owner.
              Returns an empty list if no active owner with the given DNI is found.
    """
    return read_file_csv_with(file_name, owner_read_handler, lambda o: o[HEADER_OWNER.index("dni")] == _dni and bool(o[HEADER_OWNER.index("active")]) == True)

def get_data_owner_by_id(_id):
    """Retrieves a single active owner from the data source by their unique ID.

    This function searches the owner data file for an owner that matches the
    provided ID and is marked as active.

    Args:
        _id (str): The unique identifier of the owner to find.

    Returns:
        dict or object or None: The data corresponding to the found active owner.
                                Returns None if no active owner with the specified
                                ID is found.
    """
    return read_file_csv_with(file_name, owner_read_handler, lambda o: o[HEADER_OWNER.index("owner_id")] == _id and bool(o[HEADER_OWNER.index("active")]) == True)

def get_next_owner_id():
    """Calculates and returns the next available ID for an owner.

    This function determines the next sequential ID for a new owner
    based on the existing IDs in the data file. It calls the
    generic `get_next_id_by_file` function to perform the calculation.

    Returns:
        int: The next available numeric ID to assign to a new owner.
    """
    return get_next_id_by_file(file_name)

def owner_append_handler(entity):
    """Converts an owner entity tuple into a CSV formatted string.

    Args:
        entity (tuple): A tuple containing the owner's data in the following
            order: (owner_id, dni, nombre, apellido, email, telefono, active).

    Returns:
        str: A comma-separated string representing the owner's data,
             ready to be written to a file.
    """
    owner_id, dni, nombre, apellido, email, telefono, active = entity
    return f'{owner_id},{dni},{nombre},{apellido},{email},{telefono},{active}'

def save_data_owner(new_owner):
    """Saves a new owner's data to the data file.

    This function appends a new owner's record to the designated data file.
    It uses a specific handler to format the owner's data before writing.

    Args:
        new_owner (Owner): The owner object containing the data to be saved.

    Returns:
        bool: The return value from `append_line_to_file`, typically
              True if the data was successfully appended, False otherwise.
    """
    return append_line_to_file(file_name, owner_append_handler, new_owner)

def get_all_owners():
    """Retrieves all owner records from the data source.

        Returns:
            list[dict]: A list of dictionaries, where each dictionary represents an owner.
    """
    return read_all_file_csv(file_name)

def save_all_owners(owners):
    """Saves a list of owner objects to a persistent storage file.

    This function utilizes a generic file-saving utility, providing it with
    the specific file name and data handling logic required for owner objects.

    Args:
        owners (list): A list of owner objects to be saved.

    Returns:
        bool: True if the data was saved successfully, False otherwise.
    """
    return save_all_to_file(file_name, owner_append_handler, owners)
