import tkinter as tk
from tkinter import messagebox
from entities.owners.controller import show_all_owners_action
from entities.owners.data import get_next_owner_id, save_data_owner
from entities.owners.entity import READABLE_HEADER, delete_owner_by_id, get_all_owners_active, get_readable_owner, read_owner_by_id, update_owner_by_id, update_owner_data, validate_owner_dni
from entities.veterinarians.validations import is_valid_name
from utils.constants import HEADER_OWNER
from utils.uiHelper import create_scrollable_container, on_focusOut_validation
from utils.validations import is_valid_email, is_valid_phone

def on_create_new_owner(root, container):
    modal_create = tk.Toplevel(root)
    modal_create.title(f"Crear nuevo dueño")
    modal_create.geometry("500x400")
    
    for prop in HEADER_OWNER:
        if prop == "dni":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_dni = tk.Entry(modal_create)
            input_dni.pack(fill="x", padx=10)
            input_dni.bind("<FocusOut>", lambda e: on_focusOut_validation(e, validate_owner_dni))
        elif prop == "nombre":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_name = tk.Entry(modal_create)
            input_name.pack(fill="x", padx=10)
            input_name.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "apellido":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_surname = tk.Entry(modal_create)
            input_surname.pack(fill="x", padx=10)
            input_surname.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "email":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_email = tk.Entry(modal_create)
            input_email.pack(fill="x", padx=10)
            input_email.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_email))
        elif prop == "telefono":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_telefono = tk.Entry(modal_create)
            input_telefono.pack(fill="x", padx=10)
            input_telefono.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_phone))
            
    def save_data():
        new_owner = []
        hasError = False

        if (not validate_owner_dni(input_dni.get()) or 
            not is_valid_name(input_name.get()) or 
            not is_valid_name(input_surname.get()) or 
            not is_valid_email(input_email.get()) or 
            not is_valid_phone(input_telefono.get())):
                hasError = True
                
        new_owner.append(get_next_owner_id())
        new_owner.append(input_dni.get())
        new_owner.append(input_name.get())
        new_owner.append(input_surname.get())
        new_owner.append(input_email.get())
        new_owner.append(input_telefono.get())
        new_owner.append('True')
        
        if not hasError:
            save_data_owner(new_owner)
            modal_create.destroy()
            load_dynamic_table(container, root)
        else:
            messagebox.showerror("Error", "Algunos datos son incorrectos.", parent=modal_create)
            return
    
    btn_frame = tk.Frame(modal_create, pady=20)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Cancelar", command=modal_create.destroy).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Guardar", bg="#4CAF50", fg="white", command=save_data).pack(side="left", padx=5)



def on_search_owner(input_search, list_frame, root):
    texto_busqueda = input_search.get().lower()
    
    entities = get_all_owners_active()
    string_array = [('|').join(list(e)) for e in entities]
    for entity in string_array:
        match = texto_busqueda.lower() in entity.lower()
        if match:
            entity_tuple = get_readable_owner(entity.split('|'))
            load_dynamic_table(list_frame, root, entity_tuple)

def modify_owner(id, root, list_container):
    modal_modify = tk.Toplevel(root)
    modal_modify.title(f"Editar Usuario ID: {id}")
    modal_modify.geometry("500x400")
    current_data = read_owner_by_id(id)
    print("current_data ", current_data)
    for prop in HEADER_OWNER:
        if prop == "dni":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_dni = tk.Entry(modal_modify)
            input_dni.pack(fill="x", padx=10)
            input_dni.insert(0, current_data[HEADER_OWNER.index(prop)])
            input_dni.bind("<FocusOut>", lambda e: on_focusOut_validation(e, validate_owner_dni))
        elif prop == "nombre":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_name = tk.Entry(modal_modify)
            input_name.pack(fill="x", padx=10)
            input_name.insert(0, current_data[HEADER_OWNER.index(prop)])
            input_name.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "apellido":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_surname = tk.Entry(modal_modify)
            input_surname.pack(fill="x", padx=10)
            input_surname.insert(0, current_data[HEADER_OWNER.index(prop)])
            input_surname.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "email":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_email = tk.Entry(modal_modify)
            input_email.pack(fill="x", padx=10)
            input_email.insert(0, current_data[HEADER_OWNER.index(prop)])
            input_email.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_email))
        elif prop == "telefono":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_telefono = tk.Entry(modal_modify)
            input_telefono.pack(fill="x", padx=10)
            input_telefono.insert(0, current_data[HEADER_OWNER.index(prop)])
            input_telefono.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_phone))
    def save_data():
        hasError = False
        updated_entity = current_data.copy()
        
        if (not validate_owner_dni(input_dni.get()) or 
            not is_valid_name(input_name.get()) or 
            not is_valid_name(input_surname.get()) or 
            not is_valid_email(input_email.get()) or 
            not is_valid_phone(input_telefono.get())):
                hasError = True
                
        updated_entity[HEADER_OWNER.index("dni")] = input_dni.get()
        updated_entity[HEADER_OWNER.index("nombre")] = input_name.get()
        updated_entity[HEADER_OWNER.index("apellido")] = input_surname.get()
        updated_entity[HEADER_OWNER.index("email")] = input_email.get()
        updated_entity[HEADER_OWNER.index("telefono")] = input_telefono.get()

        if not hasError:
            update_owner_by_id(updated_entity)
            modal_modify.destroy()
            load_dynamic_table(list_container, root)
        else:
            messagebox.showerror("Error", "Algunos datos son incorrectos.", parent=modal_modify)
            return    

    btn_frame = tk.Frame(modal_modify, pady=20)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Cancelar", command=modal_modify.destroy).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Guardar", bg="#4CAF50", fg="white", command=save_data).pack(side="left", padx=5)


def delete_owner(id, root, list_container):
    if messagebox.askyesno("Confirmar", f"¿Borrar ID {id}?"):
        delete_owner_by_id(id)
        load_dynamic_table(list_container, root)

def load_dynamic_table(container, root, filtered_data=[]):
    for widget in container.winfo_children():
        widget.destroy()

    try:
        index_to_show = [READABLE_HEADER.index(col) for col in READABLE_HEADER]
        index_id = HEADER_OWNER.index("owner_id")
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
        data = show_all_owners_action()    
         
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
                  command=lambda i=row_id: delete_owner(i, root, container)).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Editar", 
                  command=lambda i=row_id: modify_owner(i, root, container)).pack(side="left", padx=2)

def create_list_frame_owner(root):
    frame_controles = tk.Frame(root, pady=10, padx=10, bg="#eee")
    frame_controles.pack(fill="x")

    tk.Label(frame_controles, text="Buscar:", bg="#eee").pack(side="left")

    input_search = tk.Entry(frame_controles)
    input_search.pack(side="left", padx=5)

    btn_buscar = tk.Button(frame_controles, text="🔍", command=lambda: on_search_owner(input_search, list_frame, root))
    btn_buscar.pack(side="left")

    btn_nuevo = tk.Button(frame_controles, text="+ Nuevo Dueño", bg="#4CAF50", fg="white", command=lambda: on_create_new_owner(root, list_frame))
    btn_nuevo.pack(side="right")
    
    list_frame = create_scrollable_container(root)
    load_dynamic_table(list_frame, root)