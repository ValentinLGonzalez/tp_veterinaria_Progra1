from entities.owners.data import get_data_owner_by_id
from entities.pets.data import delete_data_pets, get_data_pet_by_id, get_data_pet_by_name, get_data_pet_by_owner_id_and_pet_name, get_next_pet_id, save_data_pet
from entities.owners.controller import show_all_owners_action
from entities.owners.entity import get_owner_by_dni
from entities.pets.validations import is_valid_pet_age, is_valid_pet_weigth
from entities.veterinarians.validations import is_valid_name
from utils.constants import HEADER_PET, EXCLUDED_PRINT_HEADERS, HEADER_OWNER
from utils.arrayHelper import print_array

READABLE_HEADER = ["nombre", "raza", "edad", "dueño", "peso", "sexo"]

def create_pet():
    new_pet = []    
    for header in HEADER_PET:
        if header == "pet_id":
            new_pet.append(get_next_pet_id())
        elif header == "active":
            new_pet.append(True)
        elif header == "owner_id":
            show_all_owners_action()
            valid_owner = False
            while not valid_owner:
                input_dni = input("Ingresa el DNI del dueño: ")
                owner = get_owner_by_dni(input_dni)
                if owner:
                    valid_owner = True
                    new_pet.append(owner[HEADER_OWNER.index('owner_id')])
                else:
                    print("No se encontró un dueño con ese DNI.")
        elif header == "nombre":
            valid_name = False
            while not valid_name:
                input_name = input("Ingresa el nombre de la mascota: ")
                if is_valid_name(input_name):
                    valid_name = True
                    new_pet.append(input_name)
                else:
                    print("El nombre de la mascota es inválido.")
        elif header == "edad":
            valid_age = False
            while not valid_age:
                input_age = input("Ingresa la edad de la mascota: ")
                if is_valid_pet_age(input_age):
                    valid_age = True
                    new_pet.append(int(input_age))
                else:
                    print("La edad ingresada no es válida.")
        elif header == "peso":
            valid_weight = False
            while not valid_weight:
                input_weight = input("Ingresa el peso de la mascota: ")
                if is_valid_pet_weigth(input_weight):
                    valid_weight = True
                    new_pet.append(float(input_weight))
                else:
                    print("El peso ingresado no es válido.")
        else:
            input_header = input(f'Ingresa {header}: ')
            new_pet.append(input_header)
    save_data_pet(new_pet)
    return new_pet


def read_pet_by_id(pet_id):
    try:
        return get_data_pet_by_id(pet_id)
    except:
        raise Exception("Ocurrió un problema al intentar buscar la mascota.")


def update_pet_by_id(updated_pet, array_pets):
    current_pets_id = [pet[HEADER_PET.index("pet_id")] for pet in array_pets]
    updated_pet_id = updated_pet[HEADER_PET.index("pet_id")]
    if updated_pet_id in current_pets_id:
        updated_pet_index = current_pets_id.index(updated_pet_id)
        array_pets[updated_pet_index] = updated_pet
        return array_pets[updated_pet_index]
    return None


def delete_pet_by_id(id):
    pet_to_delete = get_data_pet_by_id(id)
    pet_to_delete[HEADER_PET.index('active')] = 'False'
    delete_data_pets(pet_to_delete)


def show_pet(pet):
    print()
    readable_pet = get_readable_pet(pet)
    print_array(READABLE_HEADER, readable_pet)


def get_pet_by_name_and_owner(pet_name, owner_id):
    pet_found = get_data_pet_by_owner_id_and_pet_name(owner_id, pet_name)
    return pet_found


def update_pet_data(current_pet):
    updated_entity = current_pet.copy()
    
    for header in HEADER_PET:
        if header in EXCLUDED_PRINT_HEADERS:
            continue
        elif header == "nombre":
            valid_name = False
            while not valid_name:
                input_name = input("Ingresa un nuevo nombre: ")
                if is_valid_name(input_name):
                    valid_name = True
                    updated_entity[HEADER_PET.index(header)] = input_name
                else:
                    print("Nombre inválido.")
        elif header == "edad":
            valid_age = False
            while not valid_age:
                input_age = input("Ingresa una nueva edad: ")
                if is_valid_pet_age(input_age):
                    valid_age = True
                    updated_entity[HEADER_PET.index(header)] = int(input_age)
                else:
                    print("Edad inválida.")
        elif header == "peso":
            valid_weight = False
            while not valid_weight:
                input_weight = input("Ingresa un nuevo peso: ")
                if is_valid_pet_weigth(input_weight):
                    valid_weight = True
                    updated_entity[HEADER_PET.index(header)] = float(input_weight)
                else:
                    print("Peso inválido.")
        elif header == "owner_id":
            print("Actualiza el dueño de la mascota:")
            show_all_owners_action([])
            input_dni = input("Ingresa el DNI del nuevo dueño: ")
            owner = get_owner_by_dni([], input_dni)
            if owner:
                updated_entity[HEADER_PET.index("owner_id")] = owner[0]
            else:
                print("Dueño no encontrado.")
        else:
            input_header = input(f'Ingresa un nuevo {header}: ')
            updated_entity[HEADER_PET.index(header)] = input_header
    return updated_entity


def get_readable_pet(pet):
    owner = get_data_owner_by_id(pet[HEADER_PET.index("owner_id")])
    id = pet[HEADER_PET.index("pet_id")]
    nombre = pet[HEADER_PET.index("nombre")]
    raza = pet[HEADER_PET.index("raza")]
    edad = pet[HEADER_PET.index("edad")]
    duenio = owner[HEADER_OWNER.index("nombre")]
    peso = pet[HEADER_PET.index("peso")]
    sexo = pet[HEADER_PET.index("sexo")]

    return (id, nombre, raza, edad, duenio, peso, sexo)
