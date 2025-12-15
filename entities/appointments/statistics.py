from entities.appointments.data import get_all_appointments_with
from entities.pets.data import get_all_pets
from entities.veterinarians.data import get_all_veterinarians_with
from utils.constants import HEADER_APPOINTMENT, HEADER_PET, HEADER_VETERINARIAN
from functools import reduce

# STATISTICS
def appointment_statistics():
    """Generates statistics about appointments.

    """
    staditics = {"total_appointments_active": 0, "total_appointments_by_day": {}, "total_appointments_by_vet": {}, "average_pet_age": 0}
    print("\n--- Estadísticas de Turnos ---\n")
    appointments = get_all_appointments_with()
    veterinarians = get_all_veterinarians_with()

    active_appointments = list(filter(lambda apt: bool(apt[HEADER_APPOINTMENT.index("active")]) == True, appointments))
    print(f"Total de turnos activos: {len(active_appointments)}")
    staditics["total_appointments_active"] = active_appointments
    
    appointments_by_date = {}
    for appointment in active_appointments:
        date = appointment[HEADER_APPOINTMENT.index("fecha")]
        appointments_by_date[date] = appointments_by_date.get(date, 0) + 1
        
    print("\nTurnos por día:")
    print_appointment_statistics(appointments_by_date)
    staditics["total_appointments_by_day"] = appointments_by_date

    appointments_by_vet = {}
    for appointment in active_appointments:
        vet_id = appointment[HEADER_APPOINTMENT.index("veterinarian_id")]
        vet_name = None
        for vet in veterinarians:
            if (vet[HEADER_VETERINARIAN.index("veterinarian_id")] == vet_id and 
               bool(vet[HEADER_VETERINARIAN.index("active")])):
                vet_name = f"{vet[HEADER_VETERINARIAN.index('nombre')]} {vet[HEADER_VETERINARIAN.index('apellido')]}"
                break
        if (vet_name):
            appointments_by_vet[vet_name] = appointments_by_vet.get(vet_name, 0) + 1

    print("\nTurnos por veterinario:")
    print_appointment_statistics(appointments_by_vet)
    staditics["total_appointments_by_vet"] = appointments_by_vet
    
    # Pets stadistics
    pets_ages = [p[HEADER_PET.index('edad')] for p in get_all_pets()]
    total_pet_ages = reduce(lambda acc, pet_age:acc + int(pet_age), pets_ages, 0)
    average_pet_ages = round(total_pet_ages / len(pets_ages))
    staditics["average_pet_age"] = average_pet_ages
    print("\n--- Fin de estadísticas ---\n")
    
    return staditics

def print_appointment_statistics(dict, keys=None, index=0):
    """Recursively prints key-value pairs from a dictionary.

    Base case: Stops when index reaches the lenght of keys.

    Recursive case:  Prints current key and value, then calls itself with index + 1.

    """
    if keys is None:
        keys = list(dict.keys())
    if index == len(keys):
        return 0
    key = keys[index]
    print(f"  {key}: {dict[key]} turno(s)")
    print_appointment_statistics(dict, keys, index + 1) 