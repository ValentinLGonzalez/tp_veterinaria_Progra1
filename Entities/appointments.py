import random

from utils.constants import HEADER_APPOINTMENT, HEADER_OWNER, HEADER_PET, HEADER_VETERINARIAN
from utils.entitiesHelper import get_next_id, update_entity_data
from utils.arrayHelper import print_array_bidimensional
from utils.arrayHelper import print_array

READABLE_HEADER = ["Mascota", "Fecha", "Hora", "Tratamiento", "Veterinario"]
OPEN_WORK_HOUR = '08:00'
CLOSE_WORK_HOUR = '20:00'

horarios = {'08:00': True, '08:30': False}

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
                owner_found = find_owner_by_dni(array_owners, owner_dni)
                
                if not owner_found:
                    print("Error: No se encontró un dueño con ese DNI") 
                    break

            if owner_found:
                while pet_found is None:
                    pet_name = input("Ingrese el nombre de la mascota: ")
                    pet_found = find_pet_by_name_and_owner(array_pets, pet_name, owner_found[HEADER_OWNER.index("owner_id")])
                        
                    if pet_found:
                        new_appointment.append(pet_found[HEADER_PET.index("pet_id")]) 
                        print(f"Mascota encontrada: {pet_found[HEADER_PET.index('nombre')]} {pet_found[HEADER_PET.index('especie')]} {pet_found[HEADER_PET.index('raza')]}")
                        break
                    else:
                        print("Error: No se encontró una mascota activa con ese nombre para ese dueño") 

        elif header == "veterinarian_id":
            active_veterinarians = [vet for vet in array_veterinarians if vet[HEADER_VETERINARIAN.index("active")]] 
            random_veterinarian = random.choice(active_veterinarians)
            new_appointment.append(random_veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")])  
            
            print(f"Veterinario asignado: {random_veterinarian[HEADER_VETERINARIAN.index('nombre')]} {random_veterinarian[HEADER_VETERINARIAN.index('apellido')]} DNI({random_veterinarian[HEADER_VETERINARIAN.index('dni')]}) ({random_veterinarian[HEADER_VETERINARIAN.index('matricula')]})")
        else:
            input_header = input(f'Ingresa {header}: ')
            new_appointment.append(input_header)
    
    array_appointments.append(new_appointment)
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
        if (appointment[HEADER_APPOINTMENT.index("appointment_id")] == appointment_id and appointment[HEADER_APPOINTMENT.index("active")]):  
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
    print("\nTurno agregado correctamente.\n")
    show_appointment(new_appointment)
     
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
    appointment_to_update = find_appointment_by_user_input(array_appointments, array_pets, array_veterinarians, array_owners)
    if appointment_to_update:
        print("\nTurno encontrado:\n")
        show_appointment(appointment_to_update)
        updated_appointment = update_entity_data(appointment_to_update, HEADER_APPOINTMENT)
        updated_appointment = update_appointment(updated_appointment, array_appointments, array_pets, array_veterinarians)
        if updated_appointment:
            print("\nTurno actualizado correctamente:\n")
            show_appointment(updated_appointment)
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
    appointment_to_delete = find_appointment_by_user_input(array_appointments, array_pets, array_veterinarians, array_owners)
    if appointment_to_delete:
        print("\nTurno encontrado:\n")
        show_appointment(appointment_to_delete)
        delete_appointment_by_id(appointment_to_delete[HEADER_APPOINTMENT.index("appointment_id")], array_appointments)
        print("\nTurno dado de baja correctamente.\n")
    else:
        print("\nNo se pudo dar de baja el turno.\n")

# AUXILIARS
def find_appointment_by_user_input(array_appointments, array_pets, array_veterinarians, array_owners):
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
    owner = find_owner_by_dni(array_owners, owner_dni)
    if not owner:
        print("No se encontró un dueño activo con ese DNI")
        return None

    pet_name = input("Ingrese el nombre de la mascota: ")
    pet = find_pet_by_name_and_owner(array_pets, pet_name, owner[HEADER_OWNER.index("owner_id")])
    if not pet:
        print("No se encontró una mascota activa con ese nombre para ese dueño")
        return None

    vet_dni = input("Ingrese el DNI del veterinario: ")
    vet = find_veterinarian_by_dni(array_veterinarians, vet_dni)
    if not vet:
        print("No se encontró un veterinario activo con ese DNI")
        return None

    appointment = find_appointment_by_pet_and_vet(array_appointments, pet[HEADER_PET.index("pet_id")], vet[HEADER_VETERINARIAN.index("veterinarian_id")])
    if not appointment:
        print("No se encontró un turno para esa mascota y veterinario")
        return None

    return appointment

def find_appointment_by_pet_and_vet(array_appointments, pet_id, veterinarian_id):
    """Finds an active appointment by pet ID and veterinarian ID.

    Args:
        array_appointments (list[list]): The list of appointments.
        pet_id (str | int): The ID of the pet.
        veterinarian_id (str | int): The ID of the veterinarian.

    Returns:
        list | None: The appointment if found, otherwise None.
    """
    for appointment in array_appointments:
        if (appointment[HEADER_APPOINTMENT.index("pet_id")] == pet_id and appointment[HEADER_APPOINTMENT.index("veterinarian_id")] == veterinarian_id and appointment[HEADER_APPOINTMENT.index("active")]):
            return appointment
    return None

def find_owner_by_dni(array_owners, dni):
    for owner in array_owners:
        if (owner[HEADER_OWNER.index("dni")] == dni and owner[HEADER_OWNER.index("active")]):
            return owner
    return None

def find_pet_by_name_and_owner(array_pets, pet_name, owner_id):
    for pet in array_pets:
        if (pet[HEADER_PET.index("nombre")].lower() == pet_name.lower() and pet[HEADER_PET.index("owner_id")] == owner_id and pet[HEADER_PET.index("active")]):
            return pet
    return None

def find_veterinarian_by_dni(array_veterinarians, dni):
    for vet in array_veterinarians:
        if (vet[HEADER_VETERINARIAN.index("dni")] == dni and vet[HEADER_VETERINARIAN.index("active")]):
            return vet
    return None

def get_readable_appointment(appointment, array_pets, array_veterinarians):
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

