from entities.owners.data import get_all_owners
from entities.owners.entity import (
    create_owner,
    delete_owner_by_id,
    get_owner_by_dni,
    get_readable_owner,
    update_owner_by_id,
    update_owner_data,
    READABLE_HEADER,
)
from utils.arrayHelper import print_array, print_array_bidimensional
from utils.constants import HEADER_OWNER


def show_owner(owner):
    print("\nDueño cargado/modificado correctamente.\n")
    print_array(READABLE_HEADER, get_readable_owner(owner))


def add_owner_action():
    print("\n--- Ingrese los datos del Dueño ---\n")
    new_owner = create_owner()
    show_owner(new_owner)


def modify_owner_action():
    is_valid_dni = False
    while not is_valid_dni:
        dni_input = input("Ingrese el DNI del Dueño que desea modificar: ")
        owner_to_update = get_owner_by_dni(dni_input)
        if owner_to_update:
            is_valid_dni = True
            show_owner(owner_to_update)
        else:
            print("El DNI no corresponde a un dueño existente.")
    updated_owner = update_owner_data(owner_to_update)
    update_owner_by_id(updated_owner)
    show_owner(updated_owner)


def show_all_owners_action():
    print("\n--- Listado de Dueños Activos ---\n")
    all_owners = get_all_owners()
    active_owners = list(
        filter(lambda o: o[HEADER_OWNER.index("active")] == "True", all_owners)
    )
    readable_owners = [get_readable_owner(owner) for owner in active_owners]
    print_array_bidimensional(READABLE_HEADER, readable_owners)
    print("\n--- Fin del listado ---\n")


def delete_owner_action():
    dni_input = input("Ingrese el DNI del Dueño que desea dar de baja: ")
    owner_to_delete = get_owner_by_dni(dni_input)
    if owner_to_delete:
        print("\nDueño encontrado:\n")
        show_owner(owner_to_delete)
        delete_owner_by_id(owner_to_delete[HEADER_OWNER.index("owner_id")])
        print("\nDueño dado de baja correctamente.\n")
    else:
        print("\nNo se encontró un dueño activo con ese DNI.\n")
