from utils.arrayHelper import print_array_bidimensional, print_array
from utils.constants import HEADER_OWNER
from utils.entitiesHelper import get_next_id

# CREATE
def create_owner(array_owners):
    new_owner = []
    for header in HEADER_OWNER:
        if header == "owner_id":
            new_owner.append(get_next_id(array_owners))
        elif header == "active":
            new_owner.append(True)
        else:
            input_header = input(f'Ingresa {header}: ')
            new_owner.append(input_header)
    array_owners.append(new_owner)
    return new_owner

# READ (por id)
def read_owner_by_id(owner_id, array_owners):
    for owner in array_owners:
        if (owner[HEADER_OWNER.index("owner_id")] == owner_id and
            owner[HEADER_OWNER.index("active")] == True):
            return owner
    return None

# READ (por DNI)
def get_owner_by_dni(dni, array_owners):
    for owner in array_owners:
        if (owner[HEADER_OWNER.index("dni")] == dni and
            owner[HEADER_OWNER.index("active")] == True):
            return owner
    return None

# UPDATE
def update_owner_by_id(owner_id, updated_owner, array_owners):
    current_owners_id = [owner[HEADER_OWNER.index("owner_id")] for owner in array_owners]
    if owner_id in current_owners_id:
        updated_owner_index = current_owners_id.index(owner_id)
        for i in range(len(array_owners[updated_owner_index])):
            array_owners[updated_owner_index][i] = updated_owner[i]
        return array_owners[updated_owner_index]
    return None

# DELETE (baja lógica)
def delete_owner_by_id(owner_id, array_owners):
    current_owners_id = [owner[HEADER_OWNER.index("owner_id")] for owner in array_owners]
    if owner_id in current_owners_id:
        deleted_owner_index = current_owners_id.index(owner_id)
        array_owners[deleted_owner_index][HEADER_OWNER.index("active")] = False

# SHOW (uno)
def show_owner(owner):
    print("\nDueño cargado/modificado correctamente.\n")
    print_array(HEADER_OWNER, owner)

# ACTIONS (flujo de uso con inputs)
def add_owner_action(owners):
    print("\n--- Ingrese los datos del Dueño ---\n")
    new_owner = create_owner(owners)
    show_owner(new_owner)

def modify_owner_action(owners):
    dni_input = input("Ingrese el DNI del Dueño que desea modificar: ")
    owner_to_update = get_owner_by_dni(dni_input, owners)
    if owner_to_update:
        print("\nDueño encontrado:\n")
        show_owner(owner_to_update)
        updated_owner = create_owner(owners)  # reusar carga estilo veterinario
        return update_owner_by_id(
            updated_owner[HEADER_OWNER.index("owner_id")],
            updated_owner,
            owners
        )
    else:
        print("\nNo se encontró un dueño activo con ese DNI.\n")
        return None

def show_all_owners_action(array_owners):
    print("\n--- Listado de Dueños Activos ---\n")
    active_owners = list(
        filter(lambda o: o[HEADER_OWNER.index("active")] == True, array_owners)
    )
    print_array_bidimensional(HEADER_OWNER, active_owners)
    print("\n--- Fin del listado ---\n")

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
