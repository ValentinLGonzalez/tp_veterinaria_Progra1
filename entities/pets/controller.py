from entities.owners.controller import show_all_owners_action
from entities.owners.entity import get_owner_by_dni
from entities.pets.entity import create_pet, delete_pet_by_id, get_pet_by_name_and_owner, show_pet
from utils.constants import HEADER_PET
from utils.arrayHelper import print_array_bidimensional
def add_pet_action(pets, owners):
    print("Ingrese los datos de la Mascota: \n")
    new_pet = create_pet(pets, owners)
    show_pet(new_pet)

def modify_pet_action(pets, array_owners):
    pet_name_input = input("Ingrese el nombre de la Mascota que desea modificar: ")
    show_all_owners_action()
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
