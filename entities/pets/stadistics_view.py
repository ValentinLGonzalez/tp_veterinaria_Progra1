import tkinter as tk

from entities.pets.statistics import pet_statistics
from utils.uiHelper import create_scrollable_container, load_info_table, load_info_table_set, load_info_table_set_individual

def create_list_frame_statistics_pets(root):
    font = ("Arial", 20)
    total_active_pets_frame = tk.Frame(root, pady=10, padx=10, bg="#eee")
    total_active_pets_frame.pack(fill="x")
    
    total_inactive_pets_frame = tk.Frame(root, pady=10, padx=10, bg="#eee")
    total_inactive_pets_frame.pack(fill="x")
    
    total_species_frame = tk.Frame(root, pady=10, padx=10, bg="#eee")
    total_species_frame.pack(side="left")
    
    breeds_by_species_frame = tk.Frame(root, pady=10, padx=10, bg="#eee")
    breeds_by_species_frame.pack(side="right")

    current_stadistics = pet_statistics()
    
    total_active_pets_variable = tk.StringVar()
    total_active_pets_variable.set(current_stadistics["total_active_pets"])
    tk.Label(total_active_pets_frame, text="Total de mascotas activas:", bg="#eee", font = font).pack(fill="x", side="left")
    tk.Label(total_active_pets_frame, textvariable=total_active_pets_variable, bg="#eee", font = font).pack(side="left")
    
    total_inactive_pets_variable = tk.StringVar()
    total_inactive_pets_variable.set(current_stadistics["total_inactive_pets"])
    tk.Label(total_inactive_pets_frame, text="Total de mascotas inactivas:", bg="#eee", font = font).pack(fill="x", side="left")
    tk.Label(total_inactive_pets_frame, textvariable=total_inactive_pets_variable, bg="#eee", font = font).pack(side="left")
    
    tk.Label(total_species_frame, text="Especies registradas", bg="#eee", font = font).pack(fill="x", side="top")
    list_species = create_scrollable_container(total_species_frame)
    load_info_table_set_individual(list_species, current_stadistics["total_species"], ['Especie'])

    tk.Label(breeds_by_species_frame, text="Cantidad de razas por especie", bg="#eee", font = font).pack(fill="x", side="top")
    list_breeds = create_scrollable_container(breeds_by_species_frame)
    load_info_table_set(list_breeds, current_stadistics["breeds_by_species"], ['Especie', 'Raza'])
    