import tkinter as tk

from entities.appointments.statistics import appointment_statistics
from utils.uiHelper import create_scrollable_container, load_info_table

def create_list_frame_statistics_appointments(root):
    font = ("Arial", 20)
    total_appointments_active_frame = tk.Frame(root, pady=10, padx=10, bg="#eee")
    total_appointments_active_frame.pack(fill="x")
    
    average_pet_age_frame = tk.Frame(root, pady=10, padx=10, bg="#eee")
    average_pet_age_frame.pack(fill="x")
    
    total_appointments_by_day_frame = tk.Frame(root, pady=10, padx=10, bg="#eee")
    total_appointments_by_day_frame.pack(side="left")
    
    total_appointments_by_vet_frame = tk.Frame(root, pady=10, padx=10, bg="#eee")
    total_appointments_by_vet_frame.pack(side="right")

    current_stadistics = appointment_statistics()
    
    total_appointments_active_variable = tk.StringVar()
    total_appointments_active_variable.set(len(current_stadistics["total_appointments_active"]))
    tk.Label(total_appointments_active_frame, text="Total de turnos activos:", bg="#eee", font = font).pack(fill="x", side="left")
    tk.Label(total_appointments_active_frame, textvariable=total_appointments_active_variable, bg="#eee", font = font).pack(side="left")
    
    average_pet_age_variable = tk.StringVar()
    average_pet_age_variable.set(current_stadistics["average_pet_age"])
    tk.Label(average_pet_age_frame, text="Promedio de edad de mascotas:", bg="#eee", font = font).pack(fill="x", side="left")
    tk.Label(average_pet_age_frame, textvariable=average_pet_age_variable, bg="#eee", font = font).pack(side="left")
    
    tk.Label(total_appointments_by_day_frame, text="Turnos por día", bg="#eee", font = font).pack(fill="x", side="top")
    list_apt_day = create_scrollable_container(total_appointments_by_day_frame)
    load_info_table(list_apt_day, current_stadistics["total_appointments_by_day"], ['Dia', 'Cantidad de turnos'])

    tk.Label(total_appointments_by_vet_frame, text="Turnos por veterinario", bg="#eee", font = font).pack(fill="x", side="top")
    list_vet = create_scrollable_container(total_appointments_by_vet_frame)
    load_info_table(list_vet, current_stadistics["total_appointments_by_vet"], ['Veterinario', 'Cantidad de turnos'])
    