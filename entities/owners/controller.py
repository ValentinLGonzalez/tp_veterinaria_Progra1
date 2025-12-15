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
    """Displays the data of an owner on the screen.

    Prints a success message and then displays a formatted table
    with the information of the provided owner.

    Parameters:
        owner (Owner): The owner object whose data is to be displayed.
    """
    print("\nDueño cargado/modificado correctamente.\n")
    print_array(READABLE_HEADER, get_readable_owner(owner))


def add_owner_action():
    """Manages the flow for adding a new owner.

    This function coordinates user interaction to register a new owner.
    First, it displays a message on the console to request the data. Then, it calls
    the `create_owner` function to capture user input and create the
    owner object. Finally, it uses `show_owner` to display the information
    of the newly added owner.
    """
    print("\n--- Ingrese los datos del Dueño ---\n")
    new_owner = create_owner()
    show_owner(new_owner)


def _get_owner_to_modify_recursively():
    """Recursively prompts for an owner's DNI until a valid one is found.

    The function asks the user to enter the DNI of the owner they wish to modify.
    It searches for the owner in the database. If found, it displays their data
    and returns the owner object. If not found, it informs the user
    and calls itself again to retry.

    Returns:
        dict: The dictionary representing the found owner.
    """
    dni_input = input("Ingrese el DNI del Dueño que desea modificar: ")
    owner_to_update = get_owner_by_dni(dni_input)
    if owner_to_update:
        print("\nDueño encontrado:\n")
        show_owner(owner_to_update)
        return owner_to_update
    else:
        print("\nNo se encontró un dueño activo con ese DNI. Intente nuevamente.\n")
        return _get_owner_to_modify_recursively()


def modify_owner_action():
    """Manages the user flow for modifying an existing owner.

    This function orchestrates the entire process of modifying an owner's data.
    It handles:
    1. Recursively asking the user to select the owner to modify until a valid one is entered.
    2. Prompting for the new data to update.
    3. Performing the update in the data source using the owner's ID.
    4. Displaying the updated owner's information in the console.
    """
    print("\n--- Modificar un Dueño ---\n")
    owner_to_update = _get_owner_to_modify_recursively()
    updated_data = update_owner_data(owner_to_update)
    updated_owner = update_owner_by_id(updated_data)
    show_owner(updated_owner)


def show_all_owners_action():
    """Displays a list of all active owners.

    This function gets the complete list of owners, filters it to include
    only those marked as "active", formats the data for better
    readability, and finally prints it to the console in a table format.
    """
    all_owners = get_all_owners()
    active_owners = list(
        filter(lambda o: o[HEADER_OWNER.index("active")] == "True", all_owners)
    )
    return [get_readable_owner(owner) for owner in active_owners]




def delete_owner_action():
    """Manages the action of deactivating an owner.

    This function prompts the user for the DNI of the owner they wish to deactivate.
    It searches for the owner in the system using the provided DNI. If an
    active owner is found, it displays their information for confirmation and
    then proceeds to perform a soft delete. It prints messages
    to the console to inform the user about the result of the operation
    (success or if the owner was not found).
    """
    dni_input = input("Ingrese el DNI del Dueño que desea dar de baja: ")
    owner_to_delete = get_owner_by_dni(dni_input)
    if owner_to_delete:
        print("\nDueño encontrado:\n")
        show_owner(owner_to_delete)
        delete_owner_by_id(owner_to_delete[HEADER_OWNER.index("owner_id")])
        print("\nDueño dado de baja correctamente.\n")
    else:
        print("\nNo se encontró un dueño activo con ese DNI.\n")
