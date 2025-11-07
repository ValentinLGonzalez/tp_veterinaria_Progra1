# SHOW AN APPOINTMENT
from entities.appointments.entity import READABLE_HEADER, create_appointment, delete_appointment_by_id, get_appointment_by_user_input, get_readable_appointment, show_all_appointments_active, update_appointment, update_appointment
from utils.arrayHelper import print_array, print_array_bidimensional
from utils.constants import HEADER_APPOINTMENT

# ACTIONS
def add_appointment_action():
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
        new_appointment = create_appointment()
        if new_appointment:
            print("\nTurno agregado correctamente.\n")
            show_appointment(new_appointment)
        else:
            print("\nError: No se pudo crear el turno.\n")
    except Exception as e:
        raise Exception(f"\nError al crear el turno: {e}\n")
      
def modify_appointment_action():
    """Modifies an existing appointment.

    Prompts the user to search for an appointment using owner DNI, pet name,
    and veterinarian DNI. If found, displays the appointment, collects new data,
    updates the appointment in the file, and returns the updated record.

    Args:
        array_appointments (list[list]): The list of appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
        array_owners (list[list]): The list of owners.

    Returns:
        list | None: The updated appointment if successful, otherwise None.
    """
    print("\n--- Modificación de Turno ---\n")
    try:
        appointment_to_update = get_appointment_by_user_input()
        if appointment_to_update:
            print("\nTurno encontrado:\n")
            show_appointment(appointment_to_update)
            updated_appointment = update_appointment(appointment_to_update)
            if updated_appointment:
                print("\nTurno actualizado correctamente:\n")
                show_appointment(updated_appointment)
                return updated_appointment
        else:
            print("\nNo se pudo modificar el Turno.\n")
        return None
    except Exception as e:
        raise Exception(f"\nError al modificar el turno: {e}\n")

def show_appointment(appointment):
    """Displays the details of an appointment in a readable format.

    Converts the raw appointment data into a readable form
    (pet name, date, time, treatment, veterinarian) and prints it.

    Args:
        appointment (list): The appointment to display.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
    """
    try:
        print("\n=== Detalles del Turno ===")
        readable_appointment = get_readable_appointment(appointment)
        print_array(READABLE_HEADER, readable_appointment)
        print("==========================\n")
    except Exception as e:
        print(f"Error al mostrar el turno: {e}")

def show_all_appointments_action(): 
    """Displays all active appointments in a formatted table.

    Filters active appointments and prints them in a readable format.
    """
    try:
        print("\n--- Listado de Turnos Activos ---\n")
        readable_appointments = show_all_appointments_active()
        print_array_bidimensional(READABLE_HEADER, readable_appointments)
        print("\n--- Fin del listado ---\n")
    except Exception as e:
        raise Exception(f"Error al mostrar todos los turnos: {e}")
    
def delete_appointment_action():
    """Soft deletes an appointment after user confirmation.

    Prompts the user to search for an appointment using DNI and names,
    then marks it as inactive if found and returns the deleted appointment.
    
    Returns:
        list | None: The deactivated appointment if successful, otherwise None.
    """
    try:
        print("\n--- Baja de Turno ---\n")
        appointment_to_delete = get_appointment_by_user_input()
        if appointment_to_delete:
            print("\nTurno encontrado:\n")
            show_appointment(appointment_to_delete)
            delete_appointment_by_id(appointment_to_delete[HEADER_APPOINTMENT.index("appointment_id")])
            print("\nTurno dado de baja correctamente.\n")
        else:
            print("\nNo se pudo dar de baja el turno.\n")
    except Exception as e:
        raise Exception(f"\nError al eliminar el turno: {e}\n")

