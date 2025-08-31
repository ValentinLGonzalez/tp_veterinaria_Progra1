from utils.arrayHelper import print_array_bidimensional
from utils.arrayHelper import print_array
from utils.constants import ENCAB_VETERINARIOS
from utils.entitiesHelper import calculate_id

def create_veterinarian(array_veterinarians):
    new_veterinarian = []
    for header in ENCAB_VETERINARIOS:
        if header == "veterinario_id":
            new_veterinarian.append(calculate_id(array_veterinarians))
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
    current_veterinarians_id = [veterinarian[0] for veterinarian in array_veterinarians]
    if(current_veterinarians_id.count(veterinarian_id)):
        deleted_veterinarian_index = current_veterinarians_id.index(veterinarian_id)
        array_veterinarians.pop(deleted_veterinarian_index)
        
def show_all_veterinarians(array_veterinarians): 
    print_array_bidimensional(ENCAB_VETERINARIOS, array_veterinarians)
    
def show_veterinarian(veterinarian): 
    print()
    print("Veterinario agregado correctamente.")
    print()
    print_array(ENCAB_VETERINARIOS, veterinarian)

def add_veterinarian_action(veterinarians):
    print("Ingrese los datos del Veterinario: \n")
    new_veterinarian = create_veterinarian(veterinarians)
    show_veterinarian(new_veterinarian)
     