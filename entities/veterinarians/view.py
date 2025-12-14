import tkinter as tk
from tkinter import messagebox
from entities.veterinarians.controller import show_all_veterinarians_action
from entities.veterinarians.data import get_next_veterinarian_id, save_data_veterinarian, update_data_veterinarian
from entities.veterinarians.entity import READABLE_HEADER, delete_veterinarian_by_id, get_readable_veterinarian, get_veterinarian_by_id, validate_dni
from entities.veterinarians.validations import is_valid_matricula, is_valid_name
from utils.constants import HEADER_VETERINARIAN
from utils.validations import is_valid_email, is_valid_phone

def on_focusOut_validation(event, validatorHandler):
    widget = event.widget
    isValid = validatorHandler(widget.get())
    if not isValid:
        widget.configure(bg="#ffcccc")
    else:
        widget.configure(bg="#ccffcc")
        
def on_create_new_veterinarian(root, container):
    modal_modify = tk.Toplevel(root)
    modal_modify.title(f"Crear nuevo veterinario")
    modal_modify.geometry("500x400")
    
    for prop in HEADER_VETERINARIAN:
        if prop == "dni":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_dni = tk.Entry(modal_modify)
            input_dni.pack(fill="x", padx=10)
            input_dni.bind("<FocusOut>", lambda e: on_focusOut_validation(e, validate_dni))
        elif prop == "nombre":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_name = tk.Entry(modal_modify)
            input_name.pack(fill="x", padx=10)
            input_name.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "apellido":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_surname = tk.Entry(modal_modify)
            input_surname.pack(fill="x", padx=10)
            input_surname.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "matricula":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_matricula = tk.Entry(modal_modify)
            input_matricula.pack(fill="x", padx=10)
            input_matricula.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_matricula))
        elif prop == "email":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_email = tk.Entry(modal_modify)
            input_email.pack(fill="x", padx=10)
            input_email.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_email))
        elif prop == "telefono":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_telefono = tk.Entry(modal_modify)
            input_telefono.pack(fill="x", padx=10)
            input_telefono.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_phone))
            
    def save_data():
        new_veterinarian = []
        hasError = False

        if (not validate_dni(input_dni.get()) or 
            not is_valid_name(input_name.get()) or 
            not is_valid_name(input_surname.get()) or 
            not is_valid_matricula(input_matricula.get()) or 
            not is_valid_email(input_email.get()) or 
            not is_valid_phone(input_telefono.get())):
                hasError = True
                
        new_veterinarian.append(get_next_veterinarian_id())
        new_veterinarian.append(input_dni.get())
        new_veterinarian.append(input_name.get())
        new_veterinarian.append(input_surname.get())
        new_veterinarian.append(input_matricula.get())
        new_veterinarian.append(input_email.get())
        new_veterinarian.append(input_telefono.get())
        new_veterinarian.append(True)
        print(new_veterinarian)
        if not hasError:
            save_data_veterinarian(new_veterinarian)
            modal_modify.destroy()
            load_dynamic_table(container, root)
        else:
            messagebox.showerror("Error", "Algunos datos son incorrectos.", parent=modal_modify)
            return
    
    btn_frame = tk.Frame(modal_modify, pady=20)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Cancelar", command=modal_modify.destroy).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Guardar", bg="#4CAF50", fg="white", command=save_data).pack(side="left", padx=5)

def on_search_veterinarian(input_search, list_frame):
    texto_busqueda = input_search.get().lower()
    
    entities = show_all_veterinarians_action()
    string_array = [('|').join(list(e)) for e in entities]
    for entity in string_array:
        match = texto_busqueda.lower() in entity.lower()
        if match:
            entity_tuple = get_readable_veterinarian(entity.split('|'))
            load_dynamic_table(list_frame, entity_tuple)
            
    
    
def modify_veterinarian(id, root, container):
    modal_modify = tk.Toplevel(root)
    modal_modify.title(f"Editar Usuario ID: {id}")
    modal_modify.geometry("500x400")

    current_data = get_veterinarian_by_id(id)

    for prop in HEADER_VETERINARIAN:
        if prop == "dni":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_dni = tk.Entry(modal_modify)
            input_dni.pack(fill="x", padx=10)
            input_dni.insert(0, current_data[HEADER_VETERINARIAN.index(prop)])
            input_dni.bind("<FocusOut>", lambda e: on_focusOut_validation(e, validate_dni))
        elif prop == "nombre":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_name = tk.Entry(modal_modify)
            input_name.pack(fill="x", padx=10)
            input_name.insert(0, current_data[HEADER_VETERINARIAN.index(prop)])
            input_dni.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "apellido":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_surname = tk.Entry(modal_modify)
            input_surname.pack(fill="x", padx=10)
            input_surname.insert(0, current_data[HEADER_VETERINARIAN.index(prop)])
            input_dni.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "matricula":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_matricula = tk.Entry(modal_modify)
            input_matricula.pack(fill="x", padx=10)
            input_matricula.insert(0, current_data[HEADER_VETERINARIAN.index(prop)])
            input_dni.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_matricula))
        elif prop == "email":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_email = tk.Entry(modal_modify)
            input_email.pack(fill="x", padx=10)
            input_email.insert(0, current_data[HEADER_VETERINARIAN.index(prop)])
            input_dni.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_email))
        elif prop == "telefono":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_telefono = tk.Entry(modal_modify)
            input_telefono.pack(fill="x", padx=10)
            input_telefono.insert(0, current_data[HEADER_VETERINARIAN.index(prop)])
            input_dni.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_phone))
    def save_data():
        updated_entity = current_data.copy()
        updated_entity[HEADER_VETERINARIAN.index("dni")] = input_dni.get()
        updated_entity[HEADER_VETERINARIAN.index("nombre")] = input_name.get()
        updated_entity[HEADER_VETERINARIAN.index("apellido")] = input_surname.get()
        updated_entity[HEADER_VETERINARIAN.index("matricula")] = input_matricula.get()
        updated_entity[HEADER_VETERINARIAN.index("email")] = input_email.get()
        updated_entity[HEADER_VETERINARIAN.index("telefono")] = input_telefono.get()
        update_data_veterinarian(updated_entity)
        modal_modify.destroy()
        load_dynamic_table(container, root)

    btn_frame = tk.Frame(modal_modify, pady=20)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Cancelar", command=modal_modify.destroy).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Guardar", bg="#4CAF50", fg="white", command=save_data).pack(side="left", padx=5)

def delete_veterinarian(id, root, list_container):
    if messagebox.askyesno("Confirmar", f"¿Borrar ID {id}?"):
        delete_veterinarian_by_id(id)
        load_dynamic_table(list_container, root)

def load_dynamic_table(container, root, filtered_data=[]):
    for widget in container.winfo_children():
        widget.destroy()

    try:
        index_to_show = [HEADER_VETERINARIAN.index(col) for col in READABLE_HEADER]
        index_id = HEADER_VETERINARIAN.index("veterinarian_id")
    except ValueError as e:
        tk.Label(container, text=f"Error de configuración: {e}", fg="red").pack()
        return

    header_frame = tk.Frame(container, bg="gray")
    header_frame.pack(fill="x", pady=2)
    
    for title in READABLE_HEADER:
        tk.Label(header_frame, text=title.capitalize(), width=20, 
                 bg="gray", fg="white", anchor="w").pack(side="left", padx=5)
    
    tk.Label(header_frame, text="Acciones", bg="gray", fg="white").pack(side="right", padx=30)
    
    data = []
    if filtered_data:
        data.append(filtered_data)
    else:
        data = show_all_veterinarians_action() 
        
    for tuple_row in data:
        row_frame = tk.Frame(container, pady=2, bd=1, relief="solid")
        row_frame.pack(fill="x", pady=2)

        row_id = tuple_row[index_id]

        for index in index_to_show:
            value = tuple_row[index]
            tk.Label(row_frame, text=str(value), width=20, anchor="w").pack(side="left", padx=5)

        btn_frame = tk.Frame(row_frame)
        btn_frame.pack(side="right", padx=5)
        
        tk.Button(btn_frame, text="Eliminar", bg="#ffcccc", 
                  command=lambda i=row_id: delete_veterinarian(i, root, container)).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Editar", 
                  command=lambda i=row_id: modify_veterinarian(i, root, container)).pack(side="left", padx=2)

def create_list_frame(root):
    list_frame = tk.Frame(root, padx=10, pady=10)
    
    frame_controles = tk.Frame(root, pady=10, padx=10, bg="#eee")
    frame_controles.pack(fill="x")

    tk.Label(frame_controles, text="Buscar:", bg="#eee").pack(side="left")

    input_search = tk.Entry(frame_controles)
    input_search.pack(side="left", padx=5)

    btn_buscar = tk.Button(frame_controles, text="🔍", command=lambda: on_search_veterinarian(input_search, list_frame))
    btn_buscar.pack(side="left")

    btn_nuevo = tk.Button(frame_controles, text="+ Nuevo Usuario", bg="#4CAF50", fg="white", command=lambda: on_create_new_veterinarian(root, list_frame))
    btn_nuevo.pack(side="right")
    
    list_frame.pack(fill="both", expand=True)
    load_dynamic_table(list_frame, root=root)