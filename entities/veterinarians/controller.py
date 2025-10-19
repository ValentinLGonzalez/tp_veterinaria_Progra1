from entities.veterinarians.entity import READABLE_HEADER, create_veterinarian, delete_veterinarian_by_id, get_readable_veterinarian, get_veterinarian_by_dni, show_veterinarian, update_veterinarian_by_id, update_veterinarian_data
from utils.arrayHelper import print_array_bidimensional
from utils.constants import HEADER_VETERINARIAN

def add_veterinarian_action(veterinarians):
    """Adds a new veterinarian to the list after collecting user input.

    Prompts the user to enter the data for a new veterinarian, creates
    the veterinarian record, appends it to the list, and displays it.

    Args:
        veterinarians (list[list]): The list of veterinarians, where each
            veterinarian is represented as a list of values.

    Returns:
        list: The newly created veterinarian record.
    """
    print("\nIngrese los datos del Veterinario: \n")
    new_veterinarian = create_veterinarian(veterinarians)
    print("\nVeterinario agregado correctamente.\n")
    show_veterinarian(new_veterinarian)
     
def modify_veterinarian_action(veterinarians):
    """Modifies an existing veterinarian by searching with DNI.

    Continuously prompts the user to enter a veterinarian's DNI until a valid
    veterinarian is found. Once found, the veterinarian's details are displayed,
    updated with user input, and saved back into the list.

    Args:
        veterinarians (list[list]): The list of veterinarians, where each
            veterinarian is represented as a list of values.

    Returns:
        list: The updated veterinarian record.
    """
    is_valid_dni = False
    while not is_valid_dni:
        dni_input = input("Ingrese el DNI del Veterinario que desea modificar: ")
        veterinarian_to_update = get_veterinarian_by_dni(dni_input, veterinarians)
        if veterinarian_to_update:
            is_valid_dni = True
            show_veterinarian(veterinarian_to_update)
        else:
            print("El DNI no corresponde a un veterinario existente.")
    updated_veterinarian = update_veterinarian_data(veterinarian_to_update)
    return update_veterinarian_by_id(updated_veterinarian, veterinarians)

def show_all_veterinarians_action(array_veterinarians): 
    """Displays all active veterinarians in a formatted table.

    Filters the list of veterinarians to include only those marked as active,
    then prints them using a bidimensional array format.

    Args:
        array_veterinarians (list[list]): The list of veterinarians, where each
            veterinarian is represented as a list of values.

    Returns:
        None
    """
    active_veterinarians = list(filter(lambda v: v[HEADER_VETERINARIAN.index("active")] == True, array_veterinarians))
    readeable_veterinarians = [get_readable_veterinarian(veterinarian) for veterinarian in active_veterinarians]
    print_array_bidimensional(READABLE_HEADER, readeable_veterinarians)
    
def delete_veterinarian_action(veterinarians):
    """Soft deletes a veterinarian by DNI after user confirmation.

    Continuously prompts the user to enter a veterinarian's DNI until a valid
    veterinarian is found. Once found, displays the veterinarian, deletes it
    by marking it as inactive, and confirms the deletion.

    Args:
        veterinarians (list[list]): The list of veterinarians, where each
            veterinarian is represented as a list of values.

    Returns:
        None: The list is modified in place.
    """
    is_valid_dni = False
    while not is_valid_dni:
        dni_input = input("Ingrese el DNI del Veterinario que desea dar de baja: ")
        veterinarian_to_update = get_veterinarian_by_dni(dni_input, veterinarians)
        if veterinarian_to_update:
            is_valid_dni = True
            show_veterinarian(veterinarian_to_update)
        else:
            print("El DNI no corresponde a un veterinario existente.")
    veterinarian_to_delete = get_veterinarian_by_dni(dni_input, veterinarians)
    print("\Veterinario dado de baja correctamente.\n")
    delete_veterinarian_by_id(veterinarian_to_delete[HEADER_VETERINARIAN.index("veterinarian_id")], veterinarians)
