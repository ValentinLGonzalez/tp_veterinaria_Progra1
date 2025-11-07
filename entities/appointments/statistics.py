from entities.appointments.data import get_all_appointments_with
from entities.veterinarians.data import get_all_veterinarians_with
from utils.constants import HEADER_APPOINTMENT, HEADER_VETERINARIAN
from functools import reduce

# STATISTICS
def appointment_statistics():
    """Generates statistics about appointments.

    """
    print("\n--- Estadísticas de Turnos ---\n")
    appointments = get_all_appointments_with()
    veterinarians = get_all_veterinarians_with()

    active_appointments = list(filter(lambda apt: bool(apt[HEADER_APPOINTMENT.index("active")]) == True, appointments))
    print(f"Total de turnos activos: {len(active_appointments)}")

    appointments_by_date = {}
    for appointment in active_appointments:
        date = appointment[HEADER_APPOINTMENT.index("fecha")]
        appointments_by_date[date] = appointments_by_date.get(date, 0) + 1
        
    print("\nTurnos por día:")
    print_appointment_statistics(appointments_by_date)

    appointments_by_vet = {}
    for appointment in active_appointments:
        vet_id = appointment[HEADER_APPOINTMENT.index("veterinarian_id")]
        vet_name = None
        for vet in veterinarians:
            if (vet[HEADER_VETERINARIAN.index("veterinarian_id")] == vet_id and 
               bool(vet[HEADER_VETERINARIAN.index("active")])):
                vet_name = f"{vet[HEADER_VETERINARIAN.index('nombre')]} {vet[HEADER_VETERINARIAN.index('apellido')]} ({vet[HEADER_VETERINARIAN.index('dni')]})"
                break
        if (vet_name):
            appointments_by_vet[vet_name] = appointments_by_vet.get(vet_name, 0) + 1

    print("\nTurnos por veterinario:")
    print_appointment_statistics(appointments_by_vet)

    print("\n--- Fin de estadísticas ---\n")

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