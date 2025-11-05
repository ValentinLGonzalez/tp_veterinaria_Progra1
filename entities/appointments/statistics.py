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
    total_active_appointments = reduce(lambda total, apt: total + (1 if apt[HEADER_APPOINTMENT.index("active")] else 0), appointments, 0)
    print(f"Total de turnos activos: {total_active_appointments}")
    active_appointments = list(filter(lambda apt: apt[HEADER_APPOINTMENT.index("active")], appointments))

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
        for vet in veterinarians:
            if (vet[HEADER_VETERINARIAN.index("veterinarian_id")] == vet_id and 
               bool(vet[HEADER_VETERINARIAN.index("active")])):
                vet_name = f"{vet[HEADER_VETERINARIAN.index('nombre')]} {vet[HEADER_VETERINARIAN.index('apellido')]} ({vet[HEADER_VETERINARIAN.index('dni')]})"
                break
        if (vet_name):
            appointments_by_vet[vet_name] = appointments_by_vet.get(vet_name, 0) + 1

    print("\nTurnos por veterinario:")
    for vet, count in appointments_by_vet.items():
        print(f"  {vet}: {count} turno(s)")

    print("\n--- Fin de estadísticas ---\n")