import random

from utils.constants import ENCAB_TURNOS
from utils.entitiesHelper import calculate_id

# CONSTANTS

# CREATE
def create_appointment(array_appointments, array_pets, array_veterinarians, array_owners):
    appointment = []
    
    for header in ENCAB_TURNOS:
        if header == "turno_id":
            appointment.append(calculate_id(array_appointments))
        elif header == "activo":
            appointment.append(True)
        elif header == "mascota_id":
            # Search for the pet by it's name and owner's DNI
            owner_found = None
            pet_found = None
            while owner_found is None:
                # Search for the owner by it's DNI
                owner_dni = input("Ingrese el DNI del dueño: ")
                for owner in array_owners:
                    if owner[1] == owner_dni and owner[6]:  
                        owner_found = owner
                        break
                
                if not owner_found:
                    print("Error: No se encontró un dueño con ese DNI") # Proximamente esto llevara a la creacion de un dueño
                    break

            if owner_found:
                while pet_found is None:
                    # Search for the pet by it's name
                    pet_name = input("Ingrese el nombre de la mascota: ")
                    pet_found = None
                    for pet in array_pets:
                        if (pet[1].lower() == pet_name.lower() and pet[5] == owner_found[0] and pet[8]): 
                            pet_found = pet
                            break
                        
                    if pet_found:
                        appointment.append(pet_found[0]) 
                        print(f"Mascota encontrada: {pet_found[1]} ({pet_found[2]} {pet_found[3]})")
                        break
                    else:
                        print("Error: No se encontró una mascota activa con ese nombre para ese dueño") # Proximamente esto llevara a la creacion de la mascota

        elif header == "veterinario_id":
            # Randomly assign a veterinarian
            active_veterinarians = [vet for vet in array_veterinarians if vet[6]] 
            random_veterianarian = random.choice(active_veterinarians)
            appointment.append(random_veterianarian[0])  
            
            print(f"Veterinario asignado: {random_veterianarian[1]} {random_veterianarian[2]} ({random_veterianarian[4]})")
        else:
            input_header = input(f'Ingresa {header}: ')
            appointment.append(input_header)
    
    array_appointments.append(appointment)
    return array_appointments

# READ
def read_appointment(appointment_id, array_appointments):
    for appointment in array_appointments:
        if appointment[0] == appointment_id:
            return appointment
    return None

# UPDATE
def update_appointment(updated_appointment, array_appointments, array_pets, array_veterinarians):
    current_appointments_id = [appointment[0] for appointment in array_appointments if appointment[6]]
    if updated_appointment[0] in current_appointments_id:
        updated_appointment_index = current_appointments_id.index(updated_appointment[0])
        
        mascota_id_index = ENCAB_TURNOS.index("mascota_id")
        veterinario_id_index = ENCAB_TURNOS.index("veterinario_id")
        
        if not any(mascota[0] == updated_appointment[mascota_id_index] for mascota in array_pets):
            print(f"No existe una mascota con ese ID")
        
        if not any(veterinarian[0] == updated_appointment[veterinario_id_index] for veterinarian in array_veterinarians):
            print(f"No existe un veterinario con ese ID")
        
        for i in range(len(array_appointments[updated_appointment_index])):
            array_appointments[updated_appointment_index][i] = updated_appointment[i]
        
        return array_appointments[updated_appointment_index]
    return None

# DELETE
def delete_appointment(appointment_id, array_appointments):
    for appointment in array_appointments:
        if appointment[0] == appointment_id and appointment[6]:  
            appointment[6] = False  
            return appointment  
    return None  


# Auxiliars 
#------ Testing Appointments ------------
#create_appointment(turnos, mascotas, veterinarios, duenos)
#imprimir_matriz(ENCAB_TURNOS, turnos)
# updated_appointment = [1, 3, "25-08-2025", "16:00", "Urgencia", 2, True]
# update_appointment(updated_appointment, turnos, mascotas, veterinarios)
# imprimir_matriz(ENCAB_TURNOS, turnos)  
# deleted_appointment= delete_appointment(2, turnos)
# imprimir_matriz(ENCAB_TURNOS, turnos)
# appointment = read_appointment(1, turnos)
# imprimir_matriz(ENCAB_TURNOS, [appointment])

