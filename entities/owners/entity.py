from entities.owners.data import get_data_owner_by_dni, get_next_owner_id, save_data_owner, get_all_owners, save_all_owners, get_data_owner_by_id
from entities.owners.validations import is_valid_name
from utils.arrayHelper import print_array_bidimensional, print_array
from utils.constants import EXCLUDED_PRINT_HEADERS, HEADER_OWNER
from utils.validations import is_valid_dni, is_valid_email, is_valid_phone

READABLE_HEADER = ["Dni", "Nombre", "Apellido", "Email", "Teléfono"]

def create_owner():
    new_owner = []
    for header in HEADER_OWNER:
        if header == "owner_id":
            new_owner.append(get_next_owner_id())
        elif header == "active":
            new_owner.append(True)
        elif header == "dni":
            valid_dni = False
            while not valid_dni:
                input_header = input(f'Ingresa un {header} válido: ')
                if not get_data_owner_by_dni(input_header) and is_valid_dni(input_header):
                    valid_dni = True
                    new_owner.append(input_header)
                else:
                    print("El dueño ya existe, ingrese otro DNI.")
        elif header == "email":
            valid_email = False
            while not valid_email:
                input_header = input(f'Ingresa un Email: ')
                if is_valid_email(input_header):
                    valid_email = True
                    new_owner.append(input_header)
                else:
                    print("El formato del email es inválido.")
        elif header == "nombre":
            valid_name = False
            while not valid_name:
                input_header = input(f'Ingresa un Nombre: ')
                if is_valid_name(input_header):
                    valid_name = True
                    new_owner.append(input_header)
                else:
                    print("El formato del nombre ingresado es inválido.")
        elif header == "apellido":
            valid_surname = False
            while not valid_surname:
                input_header = input(f'Ingresa un Apellido: ')
                if is_valid_name(input_header):
                    valid_surname = True
                    new_owner.append(input_header)
                else:
                    print("El formato del apellido ingresado es inválido.")
        elif header == "telefono":        
            valid_phone = False
            while not valid_phone:
                input_header = input(f'Ingresa un Telefono: ')
                if is_valid_phone(input_header):
                    valid_phone = True
                    new_owner.append(input_header)
                else:
                    print("El formato del telefono ingresado es inválido.")
    save_data_owner(new_owner)
    return new_owner


def read_owner_by_id(owner_id):
    return get_data_owner_by_id(owner_id)


def get_owner_by_dni(dni):
    return get_data_owner_by_dni(dni)


def update_owner_by_id(updated_owner):
    all_owners = get_all_owners()
    current_owners_id = [owner[HEADER_OWNER.index("owner_id")] for owner in all_owners]
    updated_owner_id = updated_owner[HEADER_OWNER.index("owner_id")]
    if(updated_owner_id in current_owners_id):
        updated_owner_index = current_owners_id.index(updated_owner_id)
        all_owners[updated_owner_index] = updated_owner
        save_all_owners(all_owners)
        return all_owners[updated_owner_index]
    return None

def update_owner_data(current_owner):
    updated_entity = current_owner.copy()
    
    for header in HEADER_OWNER:
        if header in EXCLUDED_PRINT_HEADERS:
            continue
        elif header == "dni":
            valid_dni = False
            while not valid_dni:
                input_header = input(f'Ingresa un {header} válido: ')
                if is_valid_dni(input_header):
                    valid_dni = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El dueño ya existe, ingrese otro DNI.")
        elif header == "email":
            valid_email = False
            while not valid_email:
                input_header = input(f'Ingresa un Email: ')
                if is_valid_email(input_header):
                    valid_email = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El formato del email es inválido.")
        elif header == "nombre":
            valid_name = False
            while not valid_name:
                input_header = input(f'Ingresa un Nombre: ')
                if is_valid_name(input_header):
                    valid_name = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El formato del nombre ingresado es inválido.")
        elif header == "apellido":
            valid_surname = False
            while not valid_surname:
                input_header = input(f'Ingresa un Apellido: ')
                if is_valid_name(input_header):
                    valid_surname = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El formato del apellido ingresado es inválido.")
        elif header == "telefono":        
            valid_phone = False
            while not valid_phone:
                input_header = input(f'Ingresa un Telefono: ')
                if is_valid_phone(input_header):
                    valid_phone = True
                    updated_entity[HEADER_OWNER.index(header)] = input_header
                else:
                    print("El formato del telefono ingresado es inválido.")
    return updated_entity

def delete_owner_by_id(owner_id):
    all_owners = get_all_owners()
    current_owners_id = [owner[HEADER_OWNER.index("owner_id")] for owner in all_owners]
    if owner_id in current_owners_id:
        deleted_owner_index = current_owners_id.index(owner_id)
        all_owners[deleted_owner_index][HEADER_OWNER.index("active")] = False
        save_all_owners(all_owners)

def get_readable_owner(owner):
    
    dni = owner[HEADER_OWNER.index("dni")]
    name = owner[HEADER_OWNER.index("nombre")]
    surname = owner[HEADER_OWNER.index("apellido")]
    email = owner[HEADER_OWNER.index("email")]
    phone = owner[HEADER_OWNER.index("telefono")]

    return (dni, name, surname, email, phone)

