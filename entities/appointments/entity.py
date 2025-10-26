import random
from entities.appointments.data import get_next_appointment_id, save_data_appointment
from entities.appointments.validations import is_valid_appointment_date, is_valid_appointment_time, is_valid_appointment_date
from entities.owner import get_owner_by_dni
from entities.pet import get_pet_by_name_and_owner
from entities.treatments import TREATMENTS, get_treatment_description_by_id, is_valid_treatment, show_all_treatments
from entities.veterinarians.entity import get_veterinarian_by_dni
from utils.constants import HEADER_APPOINTMENT, HEADER_OWNER, HEADER_PET, HEADER_VETERINARIAN
from utils.entitiesHelper import get_next_id

# CONSTANTS
READABLE_HEADER = ["Mascota", "Fecha", "Hora", "Tratamiento", "Veterinario"]

# CREATE
def create_appointment(array_appointments, array_pets, array_veterinarians, array_owners):
    """Creates a new appointment and appends it to the list.

    Iterates over the headers defined in HEADER_APPOINTMENT to build
    a new appointment record:
    - Generates a unique ID for "appointment_id".
    - Sets "active" to True.
    - Asks the user to input the owner's DNI and pet name, then validates them.
    - Randomly assigns an active veterinarian.

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
            new_appointment.append(get_next_appointment_id())
        elif header == "active":
            new_appointment.append(True)
        elif header == "treatment_id":
            appointment_treatment = None
            while appointment_treatment is None:
                show_all_treatments(TREATMENTS)
                treatment_id = int(input("Ingrese el id del tratamiento: "))
                if is_valid_treatment(treatment_id):
                    appointment_treatment = treatment_id
                else:
                    print("Ingrese un tratamiento válido.")
            new_appointment.append(appointment_treatment)
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
            valid_date = None
            while valid_date is None:
                input_date = input("Ingrese la fecha (DD.MM.YYYY): ")
                if is_valid_appointment_date(input_date):
                    valid_date = input_date
                    new_appointment.append(valid_date)
                else:
                    print("Error: La fecha es inválida.")
        elif header == "hora":
            valid_time = None
            while valid_time is None:
                input_time = input("Ingrese la hora (HH:MM): ")
                if is_valid_appointment_time(input_time):
                    valid_time = input_time
                    new_appointment.append(valid_time)
        elif header == "veterinarian_id":
            assigned_vet = assign_veterinarian(array_appointments, array_veterinarians, valid_date, valid_time)  
            if not assigned_vet:
                return None                 
            new_appointment.append(assigned_vet[HEADER_VETERINARIAN.index("veterinarian_id")])            
            print(f"Veterinario asignado: {assigned_vet[HEADER_VETERINARIAN.index('nombre')]} {assigned_vet[HEADER_VETERINARIAN.index('apellido')]} DNI({assigned_vet[HEADER_VETERINARIAN.index('dni')]}) ({assigned_vet[HEADER_VETERINARIAN.index('matricula')]})")
    save_data_appointment(new_appointment)
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
        array_appointments[updated_appointment_index] = updated_appointment
        return array_appointments[updated_appointment_index]
    return None

#AUXILIAR UPDATE
def update_appointment_data(appointment, array_appointments, array_veterinarians):
    """Updates appointment data by prompting the user for new values.

    If the appointment's date or time changes, automatically reassigns
    a veterinarian available
    
    Args:
        appointment (list): The appointment to update.
        
    Returns:
        list: The updated appointment.
    """

    try:
        updated_appointment = appointment.copy()
        old_date = appointment[HEADER_APPOINTMENT.index("fecha")]
        old_time = appointment[HEADER_APPOINTMENT.index("hora")]

        for header in HEADER_APPOINTMENT:
            if header in ["pet_id", "veterinarian_id", "active", "appointment_id"]:
                continue
            index = HEADER_APPOINTMENT.index(header)
            if header == "hora":
                valid_time = None
                while valid_time is None:
                    input_time = input("Ingrese la hora (HH:MM): ")
                    if is_valid_appointment_time(input_time):
                        valid_time = input_time
                    updated_appointment[index] = valid_time
            elif header == "fecha":
                valid_date = None
                while valid_date is None:
                    input_date = input("Ingrese la fecha (YYYY-MM-DD): ")
                    if is_valid_appointment_date(input_date):
                        valid_date = input_date
                        updated_appointment[index] = valid_date
                    else:
                        print("Error: La fecha es inválida.")
            elif header == "treatment_id":
                appointment_treatment = None
                while appointment_treatment is None:
                    show_all_treatments(TREATMENTS)
                    treatment_id = int(input("Ingrese el id del tratamiento: "))
                    if is_valid_treatment(treatment_id):
                        appointment_treatment = treatment_id
                    else:
                        print("Ingrese un tratamiento válido.")
                updated_appointment[index] = appointment_treatment

        new_date = updated_appointment[HEADER_APPOINTMENT.index("fecha")]
        new_time = updated_appointment[HEADER_APPOINTMENT.index("hora")]

        if new_date != old_date or new_time != old_time:
            print("\nReasignando veterinario...")
            new_vet = assign_veterinarian(array_appointments, array_veterinarians, new_date, new_time)
            if new_vet:
                updated_appointment[HEADER_APPOINTMENT.index("veterinarian_id")] = new_vet[HEADER_VETERINARIAN.index("veterinarian_id")]
                print(f"Nuevo veterinario: {new_vet[HEADER_VETERINARIAN.index('nombre')]} {new_vet[HEADER_VETERINARIAN.index('apellido')]}")
            else:
                print("No hay veterinarios disponibles. El turno será cancelado.")
                updated_appointment[HEADER_APPOINTMENT.index("active")] = False
        return updated_appointment
    except Exception as e:
        print(f"Error al modificar los datos del turno: {e}")
        return appointment

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
    treatment = get_treatment_description_by_id(appointment[HEADER_APPOINTMENT.index("treatment_id")])
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

    try:
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
    except Exception as e:
            print(f"Error al buscar turno: {e}")
            return None

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