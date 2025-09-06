import random

from utils.constants import HEADER_APPOINTMENT, HEADER_OWNER, HEADER_PET, HEADER_VETERINARIAN
from utils.entitiesHelper import get_next_id
from utils.arrayHelper import print_array_bidimensional
from utils.arrayHelper import print_array

READABLE_HEADER = ["Mascota", "Fecha", "Hora", "Tratamiento", "Veterinario"]

# CREATE
def create_appointment(array_appointments, array_pets, array_veterinarians, array_owners):
    new_appointment = []
    
    for header in HEADER_APPOINTMENT:
        if header == "appointment_id":
            new_appointment.append(get_next_id(array_appointments))
        elif header == "active":
            new_appointment.append(True)
        elif header == "pet_id":
            # Search for the pet by it's name and owner's DNI
            owner_found = None
            pet_found = None
            while owner_found is None:
                # Search for the owner by it's DNI
                owner_dni = input("Ingrese el DNI del dueño: ")
                owner_found = find_owner_by_dni(array_owners, owner_dni)
                
                if not owner_found:
                    print("Error: No se encontró un dueño con ese DNI") # Proximamente esto llevara a la creacion de un dueño
                    break

            if owner_found:
                while pet_found is None:
                    # Search for the pet by it's name
                    pet_name = input("Ingrese el nombre de la mascota: ")
                    pet_found = find_pet_by_name_and_owner(array_pets, pet_name, owner_found[HEADER_OWNER.index("owner_id")])
                        
                    if pet_found:
                        new_appointment.append(pet_found[HEADER_PET.index("pet_id")]) 
                        print(f"Mascota encontrada: {pet_found[HEADER_PET.index('nombre')]} {pet_found[HEADER_PET.index('especie')]} {pet_found[HEADER_PET.index('raza')]}")
                        break
                    else:
                        print("Error: No se encontró una mascota activa con ese nombre para ese dueño") # Proximamente esto llevara a la creacion de la mascota

        elif header == "veterinarian_id":
            # Randomly assign a veterinarian
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
    for appointment in array_appointments:
        if (appointment[HEADER_APPOINTMENT.index("appointment_id")] == appointment_id and 
            appointment[HEADER_APPOINTMENT.index("active")]):
            return appointment
    return None

# UPDATE
def update_appointment(updated_appointment, array_appointments, array_pets, array_veterinarians):
    current_appointments_id = [appointment[HEADER_APPOINTMENT.index("appointment_id")] for appointment in array_appointments if appointment[HEADER_APPOINTMENT.index("active")]]
    
    if updated_appointment[HEADER_APPOINTMENT.index("appointment_id")] in current_appointments_id:
        updated_appointment_index = current_appointments_id.index(updated_appointment[HEADER_APPOINTMENT.index("appointment_id")])
        
        # pet_id_index = HEADER_APPOINTMENT.index("pet_id")
        # veterinarian_id_index = HEADER_APPOINTMENT.index("veterinarian_id")
        
        # if not any(pet[HEADER_PET.index("pet_id")] == updated_appointment[pet_id_index] for pet in array_pets):
        #     print(f"No existe una mascota con ese ID")
        # if not any(veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")] == updated_appointment[veterinarian_id_index] for veterinarian in array_veterinarians):
        #     print(f"No existe un veterinario con ese ID")
        
        for i in range(len(array_appointments[updated_appointment_index])):
            array_appointments[updated_appointment_index][i] = updated_appointment[i]
        
        return array_appointments[updated_appointment_index]
    return None

# DELETE
def delete_appointment_by_id(appointment_id, array_appointments):
    for appointment in array_appointments:
        if (appointment[HEADER_APPOINTMENT.index("appointment_id")] == appointment_id and appointment[HEADER_APPOINTMENT.index("active")]):  
            appointment[HEADER_APPOINTMENT.index("active")] = False  
          #  return appointment  
    #return None

# SHOW AN APPOINTMENT
def show_appointment(appointment, array_pets, array_veterinarians): 
    print("\n=== Detalles del Turno ===")
    readable_appointment = get_readable_appointment(appointment, array_pets, array_veterinarians)
    print_array(READABLE_HEADER, readable_appointment)
    print("==========================\n")

# ACTIONS
def add_appointment_action(array_appointments, array_pets, array_veterinarians, array_owners):
    print("\n--- Ingrese el nuevo Turno ---\n")
    new_appointment = create_appointment(array_appointments, array_pets, array_veterinarians, array_owners)
    print("\nTurno agregado correctamente.\n")
    show_appointment(new_appointment)
     
def modify_appointment_action(array_appointments, array_pets, array_veterinarians, array_owners):
    print("\n--- Modificación de Turno ---\n")
    appointment_to_update = find_appointment_by_user_input(array_appointments, array_pets, array_veterinarians, array_owners)
    if appointment_to_update:
        print("\nTurno encontrado:\n")
        show_appointment(appointment_to_update)
        updated_appointment = update_appointment_data(appointment_to_update)
        updated_appointment = update_appointment(updated_appointment, array_appointments, array_pets, array_veterinarians)
        if updated_appointment:
            print("\nTurno actualizado correctamente:\n")
            show_appointment(updated_appointment)
            return updated_appointment
    else:
        print("\nNo se pudo modificar el Turno.\n")
    return None

def show_all_appointments_action(array_appointments, array_pets, array_veterinarians): 
    print("\n--- Listado de Turnos Activos ---\n")
    active_appointments = list(filter(lambda v: v[HEADER_APPOINTMENT.index("active")] == True, array_appointments))

    readable_appointments = []
    for appointment in active_appointments:
        readable_appointment = get_readable_appointment(appointment, array_pets, array_veterinarians)
        readable_appointments.append(readable_appointment)

    print_array_bidimensional(READABLE_HEADER, readable_appointments)
    print("\n--- Fin del listado ---\n")
    
def delete_appointment_action(array_appointments, array_pets, array_veterinarians, array_owners):
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

def update_appointment_data(appointment):
    updated_appointment = appointment.copy()
    for header in HEADER_APPOINTMENT:
        if header in ["pet_id", "veterinarian_id", "active", "appointment_id"]:
            continue
        index = HEADER_APPOINTMENT.index(header)
        input_header = input(f'Ingresa {header}: ')
        updated_appointment[index] = input_header 
    return updated_appointment

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

