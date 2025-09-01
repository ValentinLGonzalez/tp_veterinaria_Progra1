from utils.arrayHelper import print_array_bidimensional
from utils.arrayHelper import print_array
from utils.constants import ENCAB_VETERINARIOS
from utils.entitiesHelper import get_next_id

def create_veterinarian(array_veterinarians):
    new_veterinarian = []
    for header in ENCAB_VETERINARIOS:
        if header == "veterinario_id":
            new_veterinarian.append(get_next_id(array_veterinarians))
        elif header == "activo":
            new_veterinarian.append(True)
        else :
            input_header = input(f'Ingresa {header}: ')
            new_veterinarian.append(input_header)
    array_veterinarians.append(new_veterinarian)
    return new_veterinarian

def read_veterinarian_by_id(veterinarian_id, array_veterinarians):
    for veterinarian in array_veterinarians:
        if(veterinarian[0] == veterinarian_id):
            return veterinarian
                  
def update_veterinarian_by_id(veterinarian_id, updated_veterinarian, array_veterinarians):
    current_veterinarians_id = [veterinarian[0] for veterinarian in array_veterinarians]
    if(current_veterinarians_id.count(veterinarian_id)):
        updated_veterinarian_index = current_veterinarians_id.index(veterinarian_id)
        for i in range(len(array_veterinarians[updated_veterinarian_index])):
            array_veterinarians[updated_veterinarian_index][i] = updated_veterinarian[i]
    return array_veterinarians[updated_veterinarian_index]

        
def delete_veterinarian_by_id(veterinarian_id, array_veterinarians):
    current_veterinarians_id = [veterinarian[ENCAB_VETERINARIOS.index("veterinario_id")] for veterinarian in array_veterinarians]
    if(current_veterinarians_id.count(veterinarian_id)):
        deleted_veterinarian_index = current_veterinarians_id.index(veterinarian_id)
        array_veterinarians[deleted_veterinarian_index][ENCAB_VETERINARIOS.index("activo")] = False
    
def show_veterinarian(veterinarian): 
    print()
    print("Veterinario agregado correctamente.")
    print()
    print_array(ENCAB_VETERINARIOS, veterinarian)

def get_veterinarian_by_dni(dni, array_veterinarians):
    for veterinarian in array_veterinarians:
        if veterinarian[ENCAB_VETERINARIOS.index("dni")] == dni:
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
    return update_veterinarian_by_id(updated_veterinarian[ENCAB_VETERINARIOS.index("veterinario_id")], updated_veterinarian, veterinarians)

def show_all_veterinarians_action(array_veterinarians): 
    active_veterinarians = list(filter(lambda v: v[ENCAB_VETERINARIOS.index("activo")] == True, array_veterinarians))
    print_array_bidimensional(ENCAB_VETERINARIOS, active_veterinarians)
    
def delete_veterinarian_action(veterinarians):
    dni_input = input("Ingrese el DNI del Veterinario que desea dar de baja: ")
    veterinarian_to_delete = get_veterinarian_by_dni(dni_input, veterinarians)
    print(veterinarian_to_delete)
    show_veterinarian(veterinarian_to_delete)
    delete_veterinarian_by_id(veterinarian_to_delete[ENCAB_VETERINARIOS.index("veterinario_id")], veterinarians)