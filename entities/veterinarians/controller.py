from entities.veterinarians.data import get_data_veterinarian_by_dni
from entities.veterinarians.entity import READABLE_HEADER, create_veterinarian, delete_veterinarian_by_id, show_all_veterinarians_active, show_veterinarian, update_veterinarian_data
from utils.arrayHelper import print_array_bidimensional
from utils.constants import HEADER_VETERINARIAN

def add_veterinarian_action():
    """Adds a new veterinarian to the list after collecting user input.

    Prompts the user to enter the data for a new veterinarian, creates
    the veterinarian record, appends it to the list, and displays it.

    Returns:
        list: The newly created veterinarian record.
    """
    try:
        print("\nIngrese los datos del Veterinario: \n")
        new_veterinarian = create_veterinarian()
        print("\nVeterinario agregado correctamente.\n")
        show_veterinarian(new_veterinarian)
    except Exception as e:
        print(f'[ERROR] Controller - add_veterinarian_action {e}')
     
def modify_veterinarian_action():
    """Modifies an existing veterinarian by searching with DNI.

    Continuously prompts the user to enter a veterinarian's DNI until a valid
    veterinarian is found. Once found, the veterinarian's details are displayed,
    updated with user input, and saved back into the list.

    Returns:
        list: The updated veterinarian record.
    """
    try:
        is_valid_dni = False
        while not is_valid_dni:
            dni_input = input("Ingrese el DNI del Veterinario que desea modificar: ")
            veterinarian_to_update = get_data_veterinarian_by_dni(dni_input)
            if veterinarian_to_update:
                is_valid_dni = True
                show_veterinarian(veterinarian_to_update)
            else:
                print("El DNI no corresponde a un veterinario existente.")
        return update_veterinarian_data(veterinarian_to_update)
    except Exception as e:
        print(f'[ERROR] Controller - modify_veterinarian_action {e}')

def show_all_veterinarians_action(): 
    """Displays all active veterinarians in a formatted table.

    Filters the list of veterinarians to include only those marked as active,
    then prints them using a bidimensional array format.

    Returns:
        None
    """
    try:
        readeable_veterinarians = show_all_veterinarians_active()
        print_array_bidimensional(READABLE_HEADER, readeable_veterinarians)
    except Exception as e:
        print(f'[ERROR] Controller - show_all_veterinarians_action {e}')
    
def delete_veterinarian_action():
    """Soft deletes a veterinarian by DNI after user confirmation.

    Continuously prompts the user to enter a veterinarian's DNI until a valid
    veterinarian is found. Once found, displays the veterinarian, deletes it
    by marking it as inactive, and confirms the deletion.

    Returns:
        None: The list is modified in place.
    """
    
    try:
        is_valid_dni = False
        while not is_valid_dni:
            dni_input = input("Ingrese el DNI del Veterinario que desea dar de baja: ")
            veterinarian_to_update = get_data_veterinarian_by_dni(dni_input)
            if veterinarian_to_update:
                is_valid_dni = True
                show_veterinarian(veterinarian_to_update)
            else:
                print("El DNI no corresponde a un veterinario existente.")
        veterinarian_to_delete = get_data_veterinarian_by_dni(dni_input)
        print("Veterinario dado de baja correctamente.\n")
        delete_veterinarian_by_id(veterinarian_to_delete[HEADER_VETERINARIAN.index("veterinarian_id")])
    except Exception as e:
        print(f'[ERROR] Controller - delete_veterinarian_action {e}')        
