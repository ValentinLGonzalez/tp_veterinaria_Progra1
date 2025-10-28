# SHOW AN APPOINTMENT
from entities.appointments.entity import READABLE_HEADER, create_appointment, delete_appointment_by_id, get_appointment_by_user_input, get_readable_appointment, update_appointment, update_appointment_data
from utils.arrayHelper import print_array, print_array_bidimensional
from utils.constants import HEADER_APPOINTMENT

# ACTIONS
def add_appointment_action(array_appointments, array_pets, array_veterinarians, array_owners):
    """Adds a new appointment by prompting the user for input.

    Calls `create_appointment` and displays the new appointment,
    and returns it.

    Args:
        array_appointments (list[list]): The list of appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
        array_owners (list[list]): The list of owners.
    """
    print("\n--- Ingrese el nuevo Turno ---\n")
    try:
        new_appointment = create_appointment(array_appointments, array_pets, array_veterinarians, array_owners)
        if new_appointment:
            print("\nTurno agregado correctamente.\n")
            show_appointment(new_appointment, array_pets, array_veterinarians)
        else:
            print("\nError: No se pudo crear el turno.\n")
    except Exception as e:
        print(f"\nError al crear el turno: {e}\n")
      
def modify_appointment_action(array_appointments, array_pets, array_veterinarians, array_owners):
    """Modifies an existing appointment.

    Prompts the user to search for an appointment using owner DNI, pet name,
    and veterinarian DNI. If found, displays the appointment, collects new data,
    updates the appointment in the array, and returns the updated record.

    Args:
        array_appointments (list[list]): The list of appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
        array_owners (list[list]): The list of owners.

    Returns:
        list | None: The updated appointment if successful, otherwise None.
    """
    print("\n--- Modificación de Turno ---\n")
    appointment_to_update = get_appointment_by_user_input(array_appointments, array_pets, array_veterinarians, array_owners)
    if appointment_to_update:
        print("\nTurno encontrado:\n")
        show_appointment(appointment_to_update, array_pets, array_veterinarians)
        updated_appointment = update_appointment_data(appointment_to_update, array_appointments, array_veterinarians)
        updated_appointment = update_appointment(updated_appointment, array_appointments)
        if updated_appointment:
            print("\nTurno actualizado correctamente:\n")
            show_appointment(updated_appointment, array_pets, array_veterinarians)
            return updated_appointment
    else:
        print("\nNo se pudo modificar el Turno.\n")
    return None

def show_appointment(appointment, array_pets, array_veterinarians):
    """Displays the details of an appointment in a readable format.

    Converts the raw appointment data into a human-readable form
    (pet name, date, time, treatment, veterinarian) and prints it.

    Args:
        appointment (list): The appointment to display.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
    """
    print("\n=== Detalles del Turno ===")
    readable_appointment = get_readable_appointment(appointment, array_pets, array_veterinarians)
    print_array(READABLE_HEADER, readable_appointment)
    print("==========================\n")

def show_all_appointments_action(array_appointments, array_pets, array_veterinarians): 
    """Displays all active appointments in a formatted table.

    Filters active appointments and prints them in a human-readable format.

    Args:
        array_appointments (list[list]): The list of appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
    """
    print("\n--- Listado de Turnos Activos ---\n")
    active_appointments = list(filter(lambda apt: apt[HEADER_APPOINTMENT.index("active")] == True, array_appointments))

    readable_appointments = list(map(
        lambda apt: get_readable_appointment(apt, array_pets, array_veterinarians),
        active_appointments
    ))

    print_array_bidimensional(READABLE_HEADER, readable_appointments)
    print("\n--- Fin del listado ---\n")
    
def delete_appointment_action(array_appointments, array_pets, array_veterinarians, array_owners):
    """Soft deletes an appointment after user confirmation.

    Prompts the user to search for an appointment using DNI and names,
    then marks it as inactive if found and returns the deleted appointment.

    Args:
        array_appointments (list[list]): The list of appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
        array_owners (list[list]): The list of owners.

    Returns:
        list | None: The deactivated appointment if successful, otherwise None.
    """
    print("\n--- Baja de Turno ---\n")
    appointment_to_delete = get_appointment_by_user_input(array_appointments, array_pets, array_veterinarians, array_owners)
    if appointment_to_delete:
        print("\nTurno encontrado:\n")
        show_appointment(appointment_to_delete, array_pets, array_veterinarians)
        delete_appointment_by_id(appointment_to_delete[HEADER_APPOINTMENT.index("appointment_id")], array_appointments)
        print("\nTurno dado de baja correctamente.\n")
    else:
        print("\nNo se pudo dar de baja el turno.\n")

