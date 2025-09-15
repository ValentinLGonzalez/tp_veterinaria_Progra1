import random

from utils.constants import HEADER_APPOINTMENT, HEADER_OWNER, HEADER_PET, HEADER_VETERINARIAN
from utils.entitiesHelper import get_next_id
from utils.arrayHelper import print_array_bidimensional, print_array
from entities.owner import get_owner_by_dni
from entities.pet import get_pet_by_name_and_owner
from entities.veterinarians import get_veterinarian_by_dni

READABLE_HEADER = ["Mascota", "Fecha", "Hora", "Tratamiento", "Veterinario"]
OPEN_WORK_HOUR = '08:00'
CLOSE_WORK_HOUR = '20:00'

# CREATE
def create_appointment(array_appointments, array_pets, array_veterinarians, array_owners):
    """Creates a new appointment and appends it to the list.

    Iterates over the headers defined in HEADER_APPOINTMENT to build
    a new appointment record:
    - Generates a unique ID for "appointment_id".
    - Sets "active" to True.
    - Asks the user to input the owner's DNI and pet name, then validates them.
    - Randomly assigns an active veterinarian.
    - Prompts the user for the remaining values.

    Args:
        array_appointments (list[list]): The list of existing appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
        array_owners (list[list]): The list of owners.

    Returns:
        list: The newly created appointment as a list of values.
    """
    new_appointment = []
    
    
    for header in HEADER_APPOINTMENT:
        if header == "appointment_id":
            new_appointment.append(get_next_id(array_appointments))
        elif header == "active":
            new_appointment.append(True)
        elif header == "pet_id":
            owner_found = None
            pet_found = None
            while owner_found is None:
                owner_dni = input("Ingrese el DNI del dueño: ")
                owner_found = get_owner_by_dni(array_owners, owner_dni)
                
                if not owner_found:
                    print("Error: No se encontró un dueño con ese DNI") 
                    return None
            if owner_found:
                while pet_found is None:
                    pet_name = input("Ingrese el nombre de la mascota: ")
                    pet_found = get_pet_by_name_and_owner(array_pets, pet_name, owner_found[HEADER_OWNER.index("owner_id")])
                        
                    if pet_found:
                        new_appointment.append(pet_found[HEADER_PET.index("pet_id")]) 
                        print(f"Mascota encontrada: {pet_found[HEADER_PET.index('nombre')]} {pet_found[HEADER_PET.index('especie')]} {pet_found[HEADER_PET.index('raza')]}")
                        break
                    else:
                        print("Error: No se encontró una mascota activa con ese nombre para ese dueño") 
                        return None
        elif header == "fecha":
            appointment_date = input(f'Ingresa {header} (YYYY-MM-DD): ')
            new_appointment.append(appointment_date)
        elif header == "hora":
            valid_time = None
            while valid_time is None:
                input_time = input("Ingrese la hora (HH:MM): ")
                if validate_appointment_time(input_time):
                    valid_time = input_time
                new_appointment.append(valid_time)
        elif header == "veterinarian_id":
            assigned_vet = assign_veterinarian(array_appointments, array_veterinarians, appointment_date, valid_time)  
            if not assigned_vet:
                return None                 
            new_appointment.append(assigned_vet[HEADER_VETERINARIAN.index("veterinarian_id")])            
            print(f"Veterinario asignado: {assigned_vet[HEADER_VETERINARIAN.index('nombre')]} {assigned_vet[HEADER_VETERINARIAN.index('apellido')]} DNI({assigned_vet[HEADER_VETERINARIAN.index('dni')]}) ({assigned_vet[HEADER_VETERINARIAN.index('matricula')]})")
    return new_appointment

# GET
def get_appointment_by_id(appointment_id, array_appointments):
    """Retrieves an active appointment by its ID.

    Args:
        appointment_id (str | int): The ID of the appointment to retrieve.
        array_appointments (list[list]): The list of appointments.

    Returns:
        list | None: The appointment if found and active, otherwise None.
    """
    for appointment in array_appointments:
        if (appointment[HEADER_APPOINTMENT.index("appointment_id")] == appointment_id and 
            appointment[HEADER_APPOINTMENT.index("active")]):
            return appointment
    return None

# UPDATE
def update_appointment(updated_appointment, array_appointments):
    """Updates an existing appointment by its ID.

    Finds the appointment in the original array,
    replaces its contents with `updated_appointment` and returns the updated record.

    Args:
        updated_appointment (list): The appointment with updated values.
        array_appointments (list[list]): The list of appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.

    Returns:
        list | None: The updated appointment if successful, otherwise None.
    """
    current_appointments_id = [appointment[HEADER_APPOINTMENT.index("appointment_id")] for appointment in array_appointments if appointment[HEADER_APPOINTMENT.index("active")]]
    
    if updated_appointment[HEADER_APPOINTMENT.index("appointment_id")] in current_appointments_id:
        updated_appointment_index = current_appointments_id.index(updated_appointment[HEADER_APPOINTMENT.index("appointment_id")])
        
        for i in range(len(array_appointments[updated_appointment_index])):
            array_appointments[updated_appointment_index][i] = updated_appointment[i]
        
        return array_appointments[updated_appointment_index]
    return None

# DELETE
def delete_appointment_by_id(appointment_id, array_appointments):
    """Soft deletes an appointment by ID.

    Marks the appointment as inactive by setting its "active" field to False.

    Args:
        appointment_id (str | int): The ID of the appointment to delete.
        array_appointments (list[list]): The list of appointments.

    Returns:
        list | None: The deactivated appointment if found, otherwise None.
    """
    for appointment in array_appointments:
        if (appointment[HEADER_APPOINTMENT.index("appointment_id")] == appointment_id and 
            appointment[HEADER_APPOINTMENT.index("active")]):  
            appointment[HEADER_APPOINTMENT.index("active")] = False  
            return appointment  

# SHOW AN APPOINTMENT
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

# STATISTICS
def appointment_statistics(array_appointments, array_veterinarians):
    """Generates statistics about appointments.

    Args:
        array_appointments (list[list]): The list of appointments.
        array_veterinarians (list[list]): The list of veterinarians.
    """
    print("\n--- Estadísticas de Turnos ---\n")

    active_appointments = [a for a in array_appointments if a[HEADER_APPOINTMENT.index("active")]]
    print(f"Total de turnos activos: {len(active_appointments)}")

    appointments_by_date = {}
    for appointment in active_appointments:
        date = appointment[HEADER_APPOINTMENT.index("fecha")]
        appointments_by_date[date] = appointments_by_date.get(date, 0) + 1
    print("\nTurnos por día:")
    for date, count in appointments_by_date.items():
        print(f"  {date}: {count} turno(s)")

    appointments_by_vet = {}
    for appointment in active_appointments:
        vet_id = appointment[HEADER_APPOINTMENT.index("veterinarian_id")]
        vet_name = None
        for vet in array_veterinarians:
            if (vet[HEADER_VETERINARIAN.index("veterinarian_id")] == vet_id and 
               vet[HEADER_VETERINARIAN.index("active")]):
                vet_name = f"{vet[HEADER_VETERINARIAN.index('nombre')]} {vet[HEADER_VETERINARIAN.index('apellido')]} ({vet[HEADER_VETERINARIAN.index('dni')]})"
                break
        if (vet_name):
            appointments_by_vet[vet_name] = appointments_by_vet.get(vet_name, 0) + 1
    print("\nTurnos por veterinario:")
    for vet, count in appointments_by_vet.items():
        print(f"  {vet}: {count} turno(s)")

    print("\n--- Fin de estadísticas ---\n")

# ACTIONS
def add_appointment_action(array_appointments, array_pets, array_veterinarians, array_owners):
    """Adds a new appointment by prompting the user for input.

    Calls `create_appointment`, appends it to the list, displays the new appointment,
    and returns it.

    Args:
        array_appointments (list[list]): The list of appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
        array_owners (list[list]): The list of owners.
    """
    print("\n--- Ingrese el nuevo Turno ---\n")
    new_appointment = create_appointment(array_appointments, array_pets, array_veterinarians, array_owners)
    if new_appointment:
        print("\nTurno agregado correctamente.\n")
        show_appointment(new_appointment, array_pets, array_veterinarians)
    else:
        print("\nError: No se pudo crear el turno.\n")
     
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
        updated_appointment = update_appointment_data(appointment_to_update)
        updated_appointment = update_appointment(updated_appointment, array_appointments)
        if updated_appointment:
            print("\nTurno actualizado correctamente:\n")
            show_appointment(updated_appointment, array_pets, array_veterinarians)
            return updated_appointment
    else:
        print("\nNo se pudo modificar el Turno.\n")
    return None

def show_all_appointments_action(array_appointments, array_pets, array_veterinarians): 
    """Displays all active appointments in a formatted table.

    Filters active appointments and prints them in a human-readable format.

    Args:
        array_appointments (list[list]): The list of appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
    """
    print("\n--- Listado de Turnos Activos ---\n")
    active_appointments = list(filter(lambda v: v[HEADER_APPOINTMENT.index("active")] == True, array_appointments))

    readable_appointments = []
    for appointment in active_appointments:
        readable_appointment = get_readable_appointment(appointment, array_pets, array_veterinarians)
        readable_appointments.append(readable_appointment)

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

# GETTERS
def get_appointment_by_user_input(array_appointments, array_pets, array_veterinarians, array_owners):
    """Finds an appointment by asking the user for owner DNI, pet name, and veterinarian DNI.

    Args:
        array_appointments (list[list]): The list of appointments.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
        array_owners (list[list]): The list of owners.

    Returns:
        list | None: The appointment if found, otherwise None.
    """
    owner_dni = input("Ingrese el DNI del dueño: ")
    owner = get_owner_by_dni(array_owners, owner_dni)
    if not owner:
        print("No se encontró un dueño activo con ese DNI")
        return None

    pet_name = input("Ingrese el nombre de la mascota: ")
    pet = get_pet_by_name_and_owner(array_pets, pet_name, owner[HEADER_OWNER.index("owner_id")])
    if not pet:
        print("No se encontró una mascota activa con ese nombre para ese dueño")
        return None

    vet_dni = input("Ingrese el DNI del veterinario: ")
    vet = get_veterinarian_by_dni(vet_dni, array_veterinarians)
    if not vet:
        print("No se encontró un veterinario activo con ese DNI")
        return None

    appointment = get_appointment_by_pet_and_vet(array_appointments, pet[HEADER_PET.index("pet_id")], vet[HEADER_VETERINARIAN.index("veterinarian_id")])
    if not appointment:
        print("No se encontró un turno para esa mascota y veterinario")
        return None

    return appointment

def get_appointment_by_pet_and_vet(array_appointments, pet_id, veterinarian_id):
    """Finds an active appointment by pet ID and veterinarian ID.

    Args:
        array_appointments (list[list]): The list of appointments.
        pet_id (str | int): The ID of the pet.
        veterinarian_id (str | int): The ID of the veterinarian.

    Returns:
        list | None: The appointment if found, otherwise None.
    """
    for appointment in array_appointments:
        if (appointment[HEADER_APPOINTMENT.index("pet_id")] == pet_id and 
            appointment[HEADER_APPOINTMENT.index("veterinarian_id")] == veterinarian_id and 
            appointment[HEADER_APPOINTMENT.index("active")]):
            return appointment
    return None

#AUXILIAR UPDATE
def update_appointment_data(appointment):
    """Updates appointment data by prompting the user for new values.
    
    Args:
        appointment (list): The appointment to update.
        
    Returns:
        list: The updated appointment.
    """
    updated_appointment = appointment.copy()
    for header in HEADER_APPOINTMENT:
        if header in ["pet_id", "veterinarian_id", "active", "appointment_id"]:
            continue
        index = HEADER_APPOINTMENT.index(header)
        if header == "hora":
            valid_time = None
            while valid_time is None:
                input_time = input("Ingrese la hora (HH:MM): ")
                if validate_appointment_time(input_time):
                    valid_time = input_time
                updated_appointment[index] = valid_time
        else:
            input_header = input(f'Ingresa {header}: ')
            updated_appointment[index] = input_header 
    return updated_appointment


#FUNCTIONS FOR READABLE SHOWING
def get_readable_appointment(appointment, array_pets, array_veterinarians):
    """Converts an appointment to a readable format with pet and vet names.
    
    Args:
        appointment (list): The appointment to convert.
        array_pets (list[list]): The list of pets.
        array_veterinarians (list[list]): The list of veterinarians.
        
    Returns:
        list: The readable appointment format.
    """
    pet_id = appointment[HEADER_APPOINTMENT.index("pet_id")]
    date = appointment[HEADER_APPOINTMENT.index("fecha")]
    time = appointment[HEADER_APPOINTMENT.index("hora")]
    treatment = appointment[HEADER_APPOINTMENT.index("tratamiento")]
    veterinarian_id = appointment[HEADER_APPOINTMENT.index("veterinarian_id")]
    
    pet_name = None
    for pet in array_pets:
        if (pet[HEADER_PET.index("pet_id")] == pet_id):
            pet_name = pet[HEADER_PET.index("nombre")]
            break
    
    vet_name = None
    for vet in array_veterinarians:
        if (vet[HEADER_VETERINARIAN.index("veterinarian_id")] == veterinarian_id):
            vet_name = f"{vet[HEADER_VETERINARIAN.index('nombre')]} {vet[HEADER_VETERINARIAN.index('apellido')]}"
            break
    
    readable_appointment = [pet_name, date, time, treatment, vet_name]
    return readable_appointment

#VALID VETERINARIANS ASSIGNMENT
def assign_veterinarian(array_appointments, array_veterinarians, date, time):
    """Assigns an available veterinarian for a specific date and time.
    
    Args:
        array_appointments (list[list]): List of existing appointments.
        array_veterinarians (list[list]): List of veterinarians.
        date (str): Appointment date (YYYY-MM-DD).
        time (str): Appointment time (HH:MM).
        
    Returns:
        list | None: The assigned veterinarian if available, None otherwise.
    """
    active_veterinarians = [vet for vet in array_veterinarians if vet[HEADER_VETERINARIAN.index("active")]]

    available_veterinarians = []
    for vet in active_veterinarians:
        if not has_appointment_conflict(array_appointments, vet[HEADER_VETERINARIAN.index("veterinarian_id")], date, time):
            available_veterinarians.append(vet)
    
    if not available_veterinarians:
        print("Error: No hay veterinarios disponibles en esa fecha y hora")
        return None
        
    random_veterinarian = random.choice(available_veterinarians)
    return random_veterinarian

#VALIDATIONS
def validate_appointment_time(time_str):
    """Validates if a given time string is in HH:MM format, within work hours,
    and optionally available.

    Args:
        time_str (str): The input time string (expected format 'HH:MM').

    Returns:
        bool: True if valid, False otherwise.
    """
    if len(time_str) != 5 or time_str[2] != ":":
        print("Error: el formato de hora debe ser HH:MM.")
        return False
    
    hh, mm = time_str.split(":")

    if not (hh.isdigit() and mm.isdigit()):
        print("Error: la hora y minutos deben ser números.")
        return False

    hour, minute = int(hh), int(mm)

    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        print("Error: hora o minutos fuera de rango.")
        return False

    open_hour, open_minute = map(int, OPEN_WORK_HOUR.split(":"))
    close_hour, close_minute = map(int, CLOSE_WORK_HOUR.split(":"))

    if not ((hour > open_hour or (hour == open_hour and minute >= open_minute)) and
            (hour < close_hour or (hour == close_hour and minute <= close_minute))):
        print(f"Error: el horario debe estar entre {OPEN_WORK_HOUR} y {CLOSE_WORK_HOUR}.")
        return False

    return True

def has_appointment_conflict(array_appointments, veterinarian_id, date, time):
    """Checks if a veterinarian already has an appointment at the given date and time.
    
    Args:
        array_appointments (list[list]): The list of appointments.
        veterinarian_id (str | int): The ID of the veterinarian to check.
        date (str): The appointment date (YYYY-MM-DD).
        time (str): The appointment time (HH:MM).
        
    Returns:
        bool: True if there's a conflict, False otherwise.
    """
    for appointment in array_appointments:
        if (appointment[HEADER_APPOINTMENT.index("veterinarian_id")] == veterinarian_id and
            appointment[HEADER_APPOINTMENT.index("fecha")] == date and
            appointment[HEADER_APPOINTMENT.index("hora")] == time and
            appointment[HEADER_APPOINTMENT.index("active")]):
            return True
    return False