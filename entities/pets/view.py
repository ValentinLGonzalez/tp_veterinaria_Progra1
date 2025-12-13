import tkinter as tk
from tkinter import messagebox
from entities.pets.controller import show_all_pets_action
from entities.pets.entity import READABLE_HEADER
from utils.constants import HEADER_PET

def modify_pet(id):
    print(f"Editando ID: {id}")

def delete_pet(id):
    if messagebox.askyesno("Confirmar", f"¿Borrar ID {id}?"):
        print(f"Eliminando ID: {id}")

def load_dynamic_table(container):
    for widget in container.winfo_children():
        widget.destroy()

    try:
        index_to_show = [READABLE_HEADER.index(col) for col in READABLE_HEADER]
        index_id = HEADER_PET.index("pet_id")
    except ValueError as e:
        tk.Label(container, text=f"Error de configuración: {e}", fg="red").pack()
        return

    header_frame = tk.Frame(container, bg="gray")
    header_frame.pack(fill="x", pady=2)
    
    for title in READABLE_HEADER:
        tk.Label(header_frame, text=title.capitalize(), width=15, 
                 bg="gray", fg="white", anchor="w").pack(side="left", padx=5)
    
    tk.Label(header_frame, text="Acciones", bg="gray", fg="white").pack(side="right", padx=30)

    data = show_all_pets_action() 
    for tuple_row in data:
        row_frame = tk.Frame(container, pady=2, bd=1, relief="solid")
        row_frame.pack(fill="x", pady=2)

        row_id = tuple_row[index_id]

        for index in index_to_show:
            value = tuple_row[index+1]
            tk.Label(row_frame, text=str(value), width=15, anchor="w").pack(side="left", padx=5)

        btn_frame = tk.Frame(row_frame)
        btn_frame.pack(side="right", padx=5)
        
        tk.Button(btn_frame, text="Eliminar", bg="#ffcccc", 
                  command=lambda i=row_id: delete_pet(i)).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Editar", 
                  command=lambda i=row_id: modify_pet(i)).pack(side="left", padx=2)

def create_list_frame_pet(root):
    list_frame = tk.Frame(root, padx=10, pady=10)
    list_frame.pack(fill="both", expand=True)
    load_dynamic_table(list_frame)