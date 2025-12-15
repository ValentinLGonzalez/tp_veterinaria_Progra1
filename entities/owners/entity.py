from entities.owners.data import get_data_owner_by_dni, get_next_owner_id, save_data_owner, get_all_owners, save_all_owners, get_data_owner_by_id
from entities.owners.validations import is_valid_name
from utils.arrayHelper import print_array_bidimensional, print_array
from utils.constants import EXCLUDED_PRINT_HEADERS, HEADER_OWNER
from utils.validations import is_valid_dni, is_valid_email, is_valid_phone

READABLE_HEADER = ["Dni", "Nombre", "Apellido", "Email", "Teléfono"]


def validate_owner_dni(input_dni):
    get_dni = get_data_owner_by_dni(input_dni)
    return (not bool(get_data_owner_by_dni(input_dni)) or get_dni[HEADER_OWNER.index("dni")] == input_dni) and is_valid_dni(input_dni)

def create_owner():
    """Creates a new owner by interactively prompting the user for their information.

    This function guides the user through the process of creating a new owner
    record. It iterates through a predefined set of fields (HEADER_OWNER).
    For each field, it prompts the user for input and validates it.

    - 'owner_id' is generated automatically.
    - 'active' is set to True by default.
    - 'dni' is validated for uniqueness and format.
    - 'email', 'nombre' (name), 'apellido' (surname), and 'telefono' (phone)
      are validated for correct formatting.

    The user is re-prompted until valid data is provided for each field.
    Once all information is collected and validated, the new owner's data is
    saved using the `save_data_owner` function.

    Returns:
        list: A list containing the details of the newly created owner.
    """
    new_owner = []
    for header in HEADER_OWNER:
        if header == "owner_id":
            new_owner.append(get_next_owner_id())
        elif header == "active":
            new_owner.append(True)
        elif header == "dni":
            valid_dni = False
            while not valid_dni:
                input_header = input(f'Ingresa un {header} válido: ')
                if not get_data_owner_by_dni(input_header) and is_valid_dni(input_header):
                    valid_dni = True
                    new_owner.append(input_header)
                else:
                    print("El dueño ya existe, ingrese otro DNI.")
        elif header == "email":
            valid_email = False
            while not valid_email:
                input_header = input(f'Ingresa un Email: ')
                if is_valid_email(input_header):
                    valid_email = True
                    new_owner.append(input_header)
                else:
                    print("El formato del email es inválido.")
        elif header == "nombre":
            valid_name = False
            while not valid_name:
                input_header = input(f'Ingresa un Nombre: ')
                if is_valid_name(input_header):
                    valid_name = True
                    new_owner.append(input_header)
                else:
                    print("El formato del nombre ingresado es inválido.")
        elif header == "apellido":
            valid_surname = False
            while not valid_surname:
                input_header = input(f'Ingresa un Apellido: ')
                if is_valid_name(input_header):
                    valid_surname = True
                    new_owner.append(input_header)
                else:
                    print("El formato del apellido ingresado es inválido.")
        elif header == "telefono":        
            valid_phone = False
            while not valid_phone:
                input_header = input(f'Ingresa un Telefono: ')
                if is_valid_phone(input_header):
                    valid_phone = True
                    new_owner.append(input_header)
                else:
                    print("El formato del telefono ingresado es inválido.")
    save_data_owner(new_owner)
    return new_owner


def read_owner_by_id(owner_id):
    """Retrieves a specific owner by their unique ID.

        Args:
            owner_id (any): The unique identifier of the owner to find.

        Returns:
            dict | None: A dictionary containing the owner's data if found, 
                         otherwise None.
        """
    return get_data_owner_by_id(owner_id)


def get_owner_by_dni(dni):
    """Retrieves an owner's data by their DNI.

    This function acts as a wrapper to fetch owner data from the data layer
    using the owner's National Identity Document (DNI).

    Args:
        dni (str): The DNI of the owner to search for.

    Returns:
        dict or None: A dictionary containing the owner's data if found,
                      otherwise None.
    """
    return get_data_owner_by_dni(dni)


def update_owner_by_id(updated_owner):
    """Updates an owner's record by their ID.

    Finds an owner by the ID provided within the `updated_owner` list,
    replaces their existing data with the new data, and persists the changes.

    Args:
        updated_owner (list): A list containing the updated data for the owner.
            The list must include the owner's ID at the correct index.

    Returns:
        list: The updated owner's data as a list if the owner was found and
              the update was successful.
        None: If no owner with the specified ID was found in the records.
    """
    all_owners = get_all_owners()
    current_owners_id = [owner[HEADER_OWNER.index("owner_id")] for owner in all_owners]
    updated_owner_id = updated_owner[HEADER_OWNER.index("owner_id")]
    if(updated_owner_id in current_owners_id):
        updated_owner_index = current_owners_id.index(updated_owner_id)
        all_owners[updated_owner_index] = updated_owner
        save_all_owners(all_owners)
        return all_owners[updated_owner_index]
    return None

def update_owner_data(current_owner):
    """Prompts the user to update the data for a given owner.
    This function creates a copy of the owner's data and then iterates through
    each attribute defined in the global `HEADER_OWNER` constant. It skips any
    headers found in `EXCLUDED_PRINT_HEADERS`.
    For each modifiable attribute (DNI, email, name, surname, phone), it
    prompts the user for new input and validates it using corresponding
    helper functions (e.g., `is_valid_dni`, `is_valid_email`). If the input is
    invalid, the user is prompted again until valid data is entered.
    Args:
        current_owner (list): A list representing the data of the owner to be updated.
    Returns:
        list: A new list containing the updated owner's information.
    """
    updated_entity = current_owner.copy()
    
    for header in HEADER_OWNER:
        if header in EXCLUDED_PRINT_HEADERS:
            continue
        elif header == "dni":
            valid_dni = False
            while not valid_dni:
                input_header = input(f'Ingresa un {header} válido: ')
                if is_valid_dni(input_header):
                    valid_dni = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El dueño ya existe, ingrese otro DNI.")
        elif header == "email":
            valid_email = False
            while not valid_email:
                input_header = input(f'Ingresa un Email: ')
                if is_valid_email(input_header):
                    valid_email = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El formato del email es inválido.")
        elif header == "nombre":
            valid_name = False
            while not valid_name:
                input_header = input(f'Ingresa un Nombre: ')
                if is_valid_name(input_header):
                    valid_name = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El formato del nombre ingresado es inválido.")
        elif header == "apellido":
            valid_surname = False
            while not valid_surname:
                input_header = input(f'Ingresa un Apellido: ')
                if is_valid_name(input_header):
                    valid_surname = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El formato del apellido ingresado es inválido.")
        elif header == "telefono":        
            valid_phone = False
            while not valid_phone:
                input_header = input(f'Ingresa un Telefono: ')
                if is_valid_phone(input_header):
                    valid_phone = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El formato del telefono ingresado es inválido.")
    return updated_entity

def delete_owner_by_id(owner_id):
    """Logically deletes an owner by setting their 'active' status to False.

    This function searches for an owner using the provided ID. If the owner is found,
    it marks them as inactive by changing their 'active' status to False in the
    data source. The change is then saved. If the ID is not found, the function
    does nothing.

    Args:
        owner_id: The unique identifier of the owner to be deleted.

    """
    all_owners = get_all_owners()
    current_owners_id = [owner[HEADER_OWNER.index("owner_id")] for owner in all_owners]
    if owner_id in current_owners_id:
        deleted_owner_index = current_owners_id.index(owner_id)
        all_owners[deleted_owner_index][HEADER_OWNER.index("active")] = False
        save_all_owners(all_owners)

def get_readable_owner(owner):
    """Extracts key information from an owner record into a structured tuple.
        This function takes a raw owner data list and extracts the most
        relevant fields for display or further processing, based on the
        indices defined in the global `HEADER_OWNER` constant.
        Args:
            owner (list): A list representing a single owner's record. The order
                          of elements must correspond to the `HEADER_OWNER` list.
        Returns:
            tuple: A tuple containing the owner's information in the following
                   order: (dni, name, surname, email, phone).
        """
    
    dni = owner[HEADER_OWNER.index("dni")]
    name = owner[HEADER_OWNER.index("nombre")]
    surname = owner[HEADER_OWNER.index("apellido")]
    email = owner[HEADER_OWNER.index("email")]
    phone = owner[HEADER_OWNER.index("telefono")]

    return (dni, name, surname, email, phone)

def get_all_owners_active():
    """Displays a list of all active owners.

    This function gets the complete list of owners, filters it to include
    only those marked as "active".
    """
    all_owners = get_all_owners()
    active_owners = list(
        filter(lambda o: o[HEADER_OWNER.index("active")] == "True", all_owners)
    )
    return active_owners