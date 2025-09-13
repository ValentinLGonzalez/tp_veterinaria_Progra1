from entities.veterinarians.validations import is_valid_matricula, is_valid_name
from utils.arrayHelper import print_array
from utils.constants import EXCLUDED_PRINT_HEADERS, HEADER_VETERINARIAN
from utils.entitiesHelper import get_next_id
from utils.validations import is_valid_dni, is_valid_email

def create_veterinarian(array_veterinarians):
    """Creates a new veterinarian and appends it to the existing list.

    Iterates over the headers defined in HEADER_VETERINARIAN to build
    a new veterinarian record:
    - If the header is "veterinarian_id", it generates a unique ID with get_next_id.
    - If the header is "active", it sets the value to True.
    - If the header is "dni", it repeatedly asks the user to enter a valid DNI
      until a unique value is provided (validated by get_veterinarian_by_dni).
    - For all other headers, it asks the user to input the value via console.

    Args:
        array_veterinarians (list[list]): The current list of veterinarians,
            where each veterinarian is represented as a list of values.

    Returns:
        list: The newly created veterinarian represented as a list of values.
    """
    new_veterinarian = []
    for header in HEADER_VETERINARIAN:
        if header == "veterinarian_id":
            new_veterinarian.append(get_next_id(array_veterinarians))
        elif header == "active":
            new_veterinarian.append(True)
        elif header == "dni":
            valid_dni = False
            while not valid_dni:
                input_header = input(f'Ingresa un {header} válido: ')
                if not get_veterinarian_by_dni(input_header, array_veterinarians) and is_valid_dni(input_header):
                    valid_dni = True
                    new_veterinarian.append(input_header)
                print("El veterinario ya existe, ingrese otro DNI.")
        elif header == "matricula":
            valid_matricula = False
            while not valid_matricula:
                input_header = input(f'Ingresa una Matrícula válida: ')
                if is_valid_matricula(input_header):
                    valid_matricula = True
                    new_veterinarian.append(input_header)
                print("El número de matrícula es inválido.")
        elif header == "email":
            valid_email = False
            while not valid_email:
                input_header = input(f'Ingresa un Email: ')
                if is_valid_email(input_header):
                    valid_email = True
                    new_veterinarian.append(input_header)
                print("El formato del email es inválido.")
        elif header == "nombre":
            valid_name = False
            while not valid_name:
                input_header = input(f'Ingresa un Nombre: ')
                if is_valid_name(input_header):
                    valid_name = True
                    new_veterinarian.append(input_header)
                print("El formato del nombre ingresado es inválido.")
        elif header == "apellido":
            valid_surname = False
            while not valid_surname:
                input_header = input(f'Ingresa un Apellido: ')
                if is_valid_name(input_header):
                    valid_surname = True
                    new_veterinarian.append(input_header)
                print("El formato del apellido ingresado es inválido.")
        elif header == "telefono":        
            valid_phone = False
            input_header = input(f'Ingresa un Telefono: ')
            new_veterinarian.append(input_header)
            # while not valid_phone:
            #     input_header = input(f'Ingresa un Telefono: ')
                # if is_valid_phone(input_header):
                #     valid_phone = True
                #     new_veterinarian.append(input_header)
                # print("El formato del telefono ingresado es inválido.")
    array_veterinarians.append(new_veterinarian)
    return new_veterinarian

def read_veterinarian_by_id(veterinarian_id, array_veterinarians):
    """Retrieves an active veterinarian by its ID.

    Iterates through the list of veterinarians and returns the first one
    that matches the given ID and is marked as active.

    Args:
        veterinarian_id (str): The ID of the veterinarian to look up.
        array_veterinarians (list[list]): The list of veterinarians, where
            each veterinarian is represented as a list of values.

    Returns:
        list | None: The veterinarian record if found and active,
        otherwise None.
    """
    for veterinarian in array_veterinarians:
        if(veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")] == veterinarian_id and veterinarian[HEADER_VETERINARIAN.index("active")] == True):
            return veterinarian
    return None
                  
def update_veterinarian_by_id(updated_veterinarian, array_veterinarians):
    """Updates a veterinarian in the list by its ID.

    Searches for the veterinarian with the same ID as `updated_veterinarian`
    and replaces the old record with the new one. If the ID does not exist,
    the function returns None.

    Args:
        updated_veterinarian (list): The veterinarian record with updated values.
        array_veterinarians (list[list]): The list of veterinarians, where each
            veterinarian is represented as a list of values.
    """
    current_veterinarians_id = [veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")] for veterinarian in array_veterinarians]
    updated_veterinarian_id = updated_veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")]
    if(updated_veterinarian_id in current_veterinarians_id):
        updated_veterinarian_index = current_veterinarians_id.index(updated_veterinarian_id)
        array_veterinarians[updated_veterinarian_index] = updated_veterinarian
        return array_veterinarians[updated_veterinarian_index]
    return None

        
def delete_veterinarian_by_id(veterinarian_id, array_veterinarians):
    """Soft deletes a veterinarian by ID.

    Searches for a veterinarian by its unique ID in the list. If found,
    the veterinarian is marked as inactive (sets the 'active' field to False).
    This function does not remove the record from the list.

    Args:
        veterinarian_id (str): The ID of the veterinarian to be deleted.
        array_veterinarians (list[list]): The list of veterinarians, where each
            veterinarian is represented as a list of values.

    Returns:
        None: The list is modified in place.
    """
    current_veterinarians_id = [veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")] for veterinarian in array_veterinarians]
    if(veterinarian_id in current_veterinarians_id):
        deleted_veterinarian_index = current_veterinarians_id.index(veterinarian_id)
        array_veterinarians[deleted_veterinarian_index][HEADER_VETERINARIAN.index("active")] = False
    return None
    
def show_veterinarian(veterinarian): 
    """Displays a veterinarian's information in a formatted way.

    Uses the HEADER_VETERINARIAN as headers and prints the veterinarian's
    data in a structured format.

    Args:
        veterinarian (list): A list of values representing a veterinarian's record.

    Returns:
        None
    """
    print()
    print_array(HEADER_VETERINARIAN, veterinarian)

def get_veterinarian_by_dni(dni, array_veterinarians):
    """Retrieves a veterinarian record by its DNI.

    Iterates through the list of veterinarians and returns the first record
    that matches the provided DNI. If no match is found, returns None.

    Args:
        dni (str): The DNI of the veterinarian to search for.
        array_veterinarians (list[list]): The list of veterinarians, where each
            veterinarian is represented as a list of values.

    Returns:
        list | None: The veterinarian record if found, otherwise None.
    """
    for veterinarian in array_veterinarians:
        if veterinarian[HEADER_VETERINARIAN.index("dni")] == dni:
            return veterinarian
    return None

def update_veterinarian_data(current_veterinarian):
    """Updates an entity's data based on user input for each field.

    Iterates over the provided headers and prompts the user to input a new
    value for each field, except those listed in EXCLUDED_PRINT_HEADERS.
    Returns a new entity list with the updated values.

    Args:
        entity (list): The current entity record represented as a list of values.
        headers (list[str]): The headers corresponding to the entity's fields.

    Returns:
        list: A new list representing the updated entity.
    """
    updated_entity = current_veterinarian.copy()
    
    for header in HEADER_VETERINARIAN:
        if header in EXCLUDED_PRINT_HEADERS:
            continue
        elif header == "dni":
            valid_dni = False
            while not valid_dni:
                input_header = input(f'Ingresa un {header} válido: ')
                if is_valid_dni(input_header): #Agregar validacion de DNI
                    valid_dni = True
                    updated_entity[HEADER_VETERINARIAN.index(header)] = input_header
                print("El veterinario ya existe, ingrese otro DNI.")
        elif header == "matricula":
            valid_matricula = False
            while not valid_matricula:
                input_header = input(f'Ingresa una Matrícula válida: ')
                if is_valid_matricula(input_header):
                    valid_matricula = True
                    updated_entity[HEADER_VETERINARIAN.index(header)] = input_header
                print("El número de matrícula es inválido.")
        elif header == "email":
            valid_email = False
            while not valid_email:
                input_header = input(f'Ingresa un Email: ')
                if is_valid_email(input_header):
                    valid_email = True
                    updated_entity[HEADER_VETERINARIAN.index(header)] = input_header
                print("El formato del email es inválido.")
        elif header == "nombre":
            valid_name = False
            while not valid_name:
                input_header = input(f'Ingresa un Nombre: ')
                if is_valid_name(input_header):
                    valid_name = True
                    updated_entity[HEADER_VETERINARIAN.index(header)] = input_header
                print("El formato del nombre ingresado es inválido.")
        elif header == "apellido":
            valid_surname = False
            while not valid_surname:
                input_header = input(f'Ingresa un Apellido: ')
                if is_valid_name(input_header):
                    valid_surname = True
                    updated_entity[HEADER_VETERINARIAN.index(header)] = input_header
                print("El formato del apellido ingresado es inválido.")
        elif header == "telefono":        
            input_header = input(f'Ingresa un Telefono: ')
            updated_entity[HEADER_VETERINARIAN.index(header)] = input_header
            # valid_phone = False
            # while not valid_phone:
            #     input_header = input(f'Ingresa un Telefono: ')
                # if is_valid_phone(input_header):
                #     valid_phone = True
                #     new_veterinarian.append(input_header)
                # print("El formato del telefono ingresado es inválido.")
    return updated_entity