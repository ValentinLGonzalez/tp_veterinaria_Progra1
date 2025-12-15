import tkinter as tk

from entities.appointments.statistics import appointment_statistics
from utils.uiHelper import create_scrollable_container

def create_list_frame_statistics(root):
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
    
def load_info_table(container, data, headers):
    font = ("Arial", 12)
    for widget in container.winfo_children():
        widget.destroy()

    header_frame = tk.Frame(container, bg="gray")
    header_frame.pack(fill="x", pady=2)
    
    for title in headers:
        tk.Label(header_frame, text=title.capitalize(), width=20, 
                 bg="gray", fg="white", anchor="w").pack(side='left', padx=5)
    for dic_row in data:
        row_frame = tk.Frame(container, pady=2, bd=1, relief="solid")
        row_frame.pack( pady=2)
        tk.Label(row_frame, text=str(dic_row), width=20, anchor="w", font=font).pack(side='left', padx=5)
        tk.Label(row_frame, text=str(data[dic_row]), width=20, anchor="w", font=font).pack(side='left', padx=5)