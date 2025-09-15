from entities.veterinarians import get_veterinarian_by_dni, is_valid_name
from utils.arrayHelper import print_array_bidimensional, print_array
from utils.constants import EXCLUDED_PRINT_HEADERS, HEADER_OWNER
from utils.entitiesHelper import get_next_id
from utils.validations import is_valid_dni, is_valid_email, is_valid_phone

READABLE_HEADER = ["Dni", "Nombre", "Apellido", "Email", "Teléfono"]

def create_owner(array_owners):
    new_owner = []
    for header in HEADER_OWNER:
        if header == "owner_id":
            new_owner.append(get_next_id(array_owners))
        elif header == "active":
            new_owner.append(True)
        elif header == "dni":
            valid_dni = False
            while not valid_dni:
                input_header = input(f'Ingresa un {header} válido: ')
                if not get_veterinarian_by_dni(input_header, array_owners) and is_valid_dni(input_header):
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
    array_owners.append(new_owner)
    return new_owner


def read_owner_by_id(owner_id, array_owners):
    for owner in array_owners:
        if (owner[HEADER_OWNER.index("owner_id")] == owner_id and
            owner[HEADER_OWNER.index("active")] == True):
            return owner
    return None


def get_owner_by_dni(dni, array_owners):
    for owner in array_owners:
        if (owner[HEADER_OWNER.index("dni")] == dni and
            owner[HEADER_OWNER.index("active")] == True):
            return owner
    return None


def update_owner_by_id(updated_owner, array_owners):
    current_owners_id = [owner[HEADER_OWNER.index("owner_id")] for owner in array_owners]
    updated_owner_id = updated_owner[HEADER_OWNER.index("owner_id")]
    if(updated_owner_id in current_owners_id):
        updated_owner_index = current_owners_id.index(updated_owner_id)
        array_owners[updated_owner_index] = updated_owner
        return array_owners[updated_owner_index]
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

def delete_owner_by_id(owner_id, array_owners):
    current_owners_id = [owner[HEADER_OWNER.index("owner_id")] for owner in array_owners]
    if owner_id in current_owners_id:
        deleted_owner_index = current_owners_id.index(owner_id)
        array_owners[deleted_owner_index][HEADER_OWNER.index("active")] = False

def show_owner(owner):
    print("\nDueño cargado/modificado correctamente.\n")
    print_array(READABLE_HEADER, get_readable_owner(owner))

def add_owner_action(owners):
    print("\n--- Ingrese los datos del Dueño ---\n")
    new_owner = create_owner(owners)
    show_owner(new_owner)

def modify_owner_action(owners):
    is_valid_dni = False
    while not is_valid_dni:
        dni_input = input("Ingrese el DNI del Dueño que desea modificar: ")
        owner_to_update = get_owner_by_dni(dni_input, owners)
        if owner_to_update:
            is_valid_dni = True
            show_owner(owner_to_update)
        else:
            print("El DNI no corresponde a un dueño existente.")
    updated_veterinarian = update_owner_data(owner_to_update)
    return update_owner_by_id(updated_veterinarian, owners)

def show_all_owners_action(array_owners):
    print("\n--- Listado de Dueños Activos ---\n")
    active_owners = list(
        filter(lambda o: o[HEADER_OWNER.index("active")] == True, array_owners)
    )
    readable_owners = [get_readable_owner(owner) for owner in active_owners]
    print_array_bidimensional(READABLE_HEADER, readable_owners)
    print("\n--- Fin del listado ---\n")
    
def get_readable_owner(owner):
    
    dni = owner[HEADER_OWNER.index("dni")]
    name = owner[HEADER_OWNER.index("nombre")]
    surname = owner[HEADER_OWNER.index("apellido")]
    email = owner[HEADER_OWNER.index("email")]
    phone = owner[HEADER_OWNER.index("telefono")]

    return (dni, name, surname, email, phone)

def delete_owner_action(owners):
    dni_input = input("Ingrese el DNI del Dueño que desea dar de baja: ")
    owner_to_delete = get_owner_by_dni(dni_input, owners)
    if owner_to_delete:
        print("\nDueño encontrado:\n")
        show_owner(owner_to_delete)
        delete_owner_by_id(owner_to_delete[HEADER_OWNER.index("owner_id")], owners)
        print("\nDueño dado de baja correctamente.\n")
    else:
        print("\nNo se encontró un dueño activo con ese DNI.\n")

