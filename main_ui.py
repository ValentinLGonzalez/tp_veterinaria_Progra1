import tkinter as tk
from tkinter import ttk

from entities.appointments.view import create_list_frame_appointment
from entities.owners.view import create_list_frame_owner
from entities.pets.view import create_list_frame_pet
from entities.veterinarians.view import create_list_frame

root = tk.Tk()
root.title("Veterinaria")
root.geometry('1200x550')
font = ("Arial", 24)
def mostrar_vista(nombre_vista):
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    if nombre_vista == "appointment":
        titulo = tk.Label(content_frame, text=f"Turnos", font=font)
        titulo.pack(pady=20)
        create_list_frame_appointment(content_frame)
    elif nombre_vista == "veterinarian":
        titulo = tk.Label(content_frame, text=f"Veterinarios", font=font)
        titulo.pack(pady=20)
        create_list_frame(content_frame)
    elif nombre_vista == "pet":
        titulo = tk.Label(content_frame, text=f"Mascotas", font=font)
        titulo.pack(pady=20)
        create_list_frame_pet(content_frame)
    elif nombre_vista == "owner":
        titulo = tk.Label(content_frame, text=f"Dueños", font=font)
        titulo.pack(pady=20)
        create_list_frame_owner(content_frame)

side_menu_frame = tk.Frame(root, width=200, bg="lightgray")
side_menu_frame.pack(side="left", fill="y") 

content_frame = tk.Frame(root, bg="white")
content_frame.pack(side="right", expand=True, fill="both")

ttk.Button(side_menu_frame, text="Turnos", command=lambda: mostrar_vista("appointment")).pack(fill="x", pady=5)
ttk.Button(side_menu_frame, text="Veterinarios", command=lambda: mostrar_vista("veterinarian")).pack(fill="x", pady=5)
ttk.Button(side_menu_frame, text="Mascotas", command=lambda: mostrar_vista("pet")).pack(fill="x", pady=5)
ttk.Button(side_menu_frame, text="Dueños", command=lambda: mostrar_vista("owner")).pack(fill="x", pady=5)

mostrar_vista("Bienvenido")

root.mainloop()