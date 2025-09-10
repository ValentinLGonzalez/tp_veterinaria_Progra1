from utils.arrayHelper import print_array_bidimensional
from utils.arrayHelper import print_array
from utils.constants import HEADER_VETERINARIAN
from utils.entitiesHelper import get_next_id

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
            is_valid_dni = False
            while not is_valid_dni:
                input_header = input(f'Ingresa un {header} válido: ')
                if not get_veterinarian_by_dni(input_header, array_veterinarians):
                    is_valid_dni = True
                    new_veterinarian.append(input_header)
                print("El veterinario ya existe, ingrese otro DNI.")
        else :
            input_header = input(f'Ingresa {header}: ')
            new_veterinarian.append(input_header)
    array_veterinarians.append(new_veterinarian)
    return new_veterinarian

def read_veterinarian_by_id(veterinarian_id, array_veterinarians):
    for veterinarian in array_veterinarians:
        if(veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")] == veterinarian_id and veterinarian[HEADER_VETERINARIAN.index("active") == True]):
            return veterinarian
                  
def update_veterinarian_by_id(veterinarian_id, updated_veterinarian, array_veterinarians):
    current_veterinarians_id = [veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")] for veterinarian in array_veterinarians]
    if(current_veterinarians_id.count(veterinarian_id)):
        updated_veterinarian_index = current_veterinarians_id.index(veterinarian_id)
        for i in range(len(array_veterinarians[updated_veterinarian_index])):
            array_veterinarians[updated_veterinarian_index][i] = updated_veterinarian[i]
    return array_veterinarians[updated_veterinarian_index]

        
def delete_veterinarian_by_id(veterinarian_id, array_veterinarians):
    current_veterinarians_id = [veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")] for veterinarian in array_veterinarians]
    if(current_veterinarians_id.count(veterinarian_id)):
        deleted_veterinarian_index = current_veterinarians_id.index(veterinarian_id)
        array_veterinarians[deleted_veterinarian_index][HEADER_VETERINARIAN.index("active")] = False
    
def show_veterinarian(veterinarian): 
    print()
    print("Veterinario agregado correctamente.")
    print()
    print_array(HEADER_VETERINARIAN, veterinarian)

def get_veterinarian_by_dni(dni, array_veterinarians):
    for veterinarian in array_veterinarians:
        if veterinarian[HEADER_VETERINARIAN.index("dni")] == dni:
            return veterinarian
    return None

# Actions
def add_veterinarian_action(veterinarians):
    print("Ingrese los datos del Veterinario: \n")
    new_veterinarian = create_veterinarian(veterinarians)
    show_veterinarian(new_veterinarian)
     
def modify_veterinarian_action(veterinarians):
    dni_input = input("Ingrese el DNI del Veterinario que desea modificar: ")
    veterinarian_to_update = get_veterinarian_by_dni(dni_input, veterinarians)
    print(veterinarian_to_update)
    show_veterinarian(veterinarian_to_update)
    updated_veterinarian = create_veterinarian(veterinarians)
    return update_veterinarian_by_id(updated_veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")], updated_veterinarian, veterinarians)

def show_all_veterinarians_action(array_veterinarians): 
    active_veterinarians = list(filter(lambda v: v[HEADER_VETERINARIAN.index("active")] == True, array_veterinarians))
    print_array_bidimensional(HEADER_VETERINARIAN, active_veterinarians)
    
def delete_veterinarian_action(veterinarians):
    dni_input = input("Ingrese el DNI del Veterinario que desea dar de baja: ")
    veterinarian_to_delete = get_veterinarian_by_dni(dni_input, veterinarians)
    print(veterinarian_to_delete)
    show_veterinarian(veterinarian_to_delete)
    delete_veterinarian_by_id(veterinarian_to_delete[HEADER_VETERINARIAN.index("veterinarian_id")], veterinarians)