from utils.arrayHelper import print_array_bidimensional
from utils.arrayHelper import print_array
from utils.entitiesHelper import get_next_id
from utils.constants import HEADER_PET
from entities.owner import get_owner_by_dni, show_all_owners_action

def create_pet(array_pets, array_owners):
    new_pet = []
    for header in HEADER_PET:
        if header == "pet_id":
            new_pet.append(get_next_id(array_pets))
        elif header == "active":
            new_pet.append(True)
        elif header == "owner_id":
            show_all_owners_action(array_owners)
            input_header = input(f'Ingresa DNI del Dueño: ')
            new_pet.append(get_owner_by_dni(array_owners,input_header)[0])
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
    current_pets_id = [pet[HEADER_PET.index("pet_id")] for pet in array_pets]
    if pet_id in current_pets_id:
        deleted_pet_index = current_pets_id.index(pet_id)
        array_pets[deleted_pet_index][HEADER_PET.index("active")] = False

def show_pet(pet):
    print()
    print("Mascota agregada/modificada correctamente.")
    print()
    print_array(HEADER_PET, pet)


def add_pet_action(pets, owners):
    print("Ingrese los datos de la Mascota: \n")
    new_pet = create_pet(pets, owners)
    show_pet(new_pet)

def modify_pet_action(pets, array_owners):
    pet_name_input = input("Ingrese el nombre de la Mascota que desea modificar: ")
    show_all_owners_action(array_owners)
    owner_dni_input = input("Ingrese el DNI del dueño de la mascota: ")

    owner = get_owner_by_dni(array_owners, owner_dni_input)
    if not owner:
        print("Dueño no encontrado.")
        return None

    owner_id = owner[0]
    pet_to_update = get_pet_by_name_and_owner(pets, pet_name_input, owner_id)

    if not pet_to_update:
        print("Mascota no encontrada.")
        return None

    print("\nMascota encontrada:")
    show_pet(pet_to_update)

    print("\nIngrese los nuevos datos (presione Enter para dejar el valor actual):")

    editable_fields = ["nombre", "especie", "raza", "edad", "peso", "género"]

    for field in editable_fields:
        index = HEADER_PET.index(field)
        current_value = pet_to_update[index]
        new_value = input(f"{field.capitalize()} [{current_value}]: ")
        if new_value.strip():
            pet_to_update[index] = new_value

    print("\nMascota modificada correctamente:")
    show_pet(pet_to_update)

    return pet_to_update


def show_all_pets_action(array_pets):
    active_pets = list(filter(lambda p: p[HEADER_PET.index("active")] == True, array_pets))
    print_array_bidimensional(HEADER_PET, active_pets)

def delete_pet_action(pets, array_owners):
    pet_name_input = input("Ingrese el nombre de la Mascota que desea dar de baja: ")
    show_all_owners_action(array_owners)
    owner_dni_input = input("Ingrese el dni del dueño de la mascota que desea dar de baja: ")
    owner_id = get_owner_by_dni(array_owners,owner_dni_input)[0]
    pet_to_delete = get_pet_by_name_and_owner(pets,pet_name_input,owner_id)
    if pet_to_delete:
        print(pet_to_delete)
        show_pet(pet_to_delete)
        delete_pet_by_id(pet_to_delete[HEADER_PET.index("pet_id")], pets)
    else:
        print("Mascota no encontrada.")


def get_pet_by_name_and_owner(array_pets, pet_name, owner_id):
    index_name = HEADER_PET.index("nombre")
    index_owner = HEADER_PET.index("owner_id")
    index_active = HEADER_PET.index("active")

    for pet in array_pets:
        if (pet[index_name].lower() == pet_name.lower() and
            pet[index_owner] == owner_id and
            pet[index_active]):
            return pet
    return None

