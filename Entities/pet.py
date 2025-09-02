from utils.arrayHelper import print_array_bidimensional
from utils.arrayHelper import print_array
from utils.entitiesHelper import get_next_id
from utils.constants import HEADER_PET

def create_pet(array_pets):
    new_pet = []
    for header in HEADER_PET:
        if header == "mascota_id":
            new_pet.append(get_next_id(array_pets))
        elif header == "activo":
            new_pet.append(True)
        else:
            input_header = input(f'Ingresa {header}: ')
            new_pet.append(input_header)
    array_pets.append(new_pet)
    return new_pet

def read_pet_by_id(pet_id, array_pets):
    for pet in array_pets:
        if (pet[0] == pet_id):
            return pet

def update_pet_by_id(pet_id, updated_pet, array_pets):
    current_pets_id = [pet[0] for pet in array_pets]
    if pet_id in current_pets_id:
        updated_pet_index = current_pets_id.index(pet_id)
        for i in range(len(array_pets[updated_pet_index])):
            array_pets[updated_pet_index][i] = updated_pet[i]
        return array_pets[updated_pet_index]

def delete_pet_by_id(pet_id, array_pets):
    current_pets_id = [pet[HEADER_PET.index("mascota_id")] for pet in array_pets]
    if pet_id in current_pets_id:
        deleted_pet_index = current_pets_id.index(pet_id)
        array_pets[deleted_pet_index][HEADER_PET.index("activo")] = False

def show_pet(pet):
    print()
    print("Mascota agregada/modificada correctamente.")
    print()
    print_array(HEADER_PET, pet)

def get_pet_by_id(pet_id, array_pets):
    for pet in array_pets:
        if pet[HEADER_PET.index("mascota_id")] == pet_id:
            return pet
    return None

def add_pet_action(pets):
    print("Ingrese los datos de la Mascota: \n")
    new_pet = create_pet(pets)
    show_pet(new_pet)

def modify_pet_action(pets):
    pet_id_input = input("Ingrese el ID de la Mascota que desea modificar: ")
    pet_to_update = get_pet_by_id(pet_id_input, pets)
    if pet_to_update:
        print(pet_to_update)
        show_pet(pet_to_update)
        updated_pet = create_pet(pets)
        return update_pet_by_id(updated_pet[HEADER_PET.index("mascota_id")], updated_pet, pets)
    else:
        print("Mascota no encontrada.")
        return None

def show_all_pets_action(array_pets):
    active_pets = list(filter(lambda p: p[HEADER_PET.index("activo")] == True, array_pets))
    print_array_bidimensional(HEADER_PET, active_pets)

def delete_pet_action(pets):
    pet_id_input = input("Ingrese el ID de la Mascota que desea dar de baja: ")
    pet_to_delete = get_pet_by_id(pet_id_input, pets)
    if pet_to_delete:
        print(pet_to_delete)
        show_pet(pet_to_delete)
        delete_pet_by_id(pet_to_delete[HEADER_PET.index("mascota_id")], pets)
    else:
        print("Mascota no encontrada.")
