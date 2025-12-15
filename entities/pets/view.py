import tkinter as tk
from tkinter import messagebox
from entities.owners.data import get_data_owner_by_id
from entities.owners.entity import get_all_owners_active
from entities.pets.controller import show_all_pets_action
from entities.pets.data import get_all_pets, get_data_pet_by_id, get_next_pet_id, save_data_pet, update_data_pets
from entities.pets.entity import READABLE_HEADER, delete_pet_by_id,get_readable_pet
from entities.pets.validations import is_valid_gender, is_valid_pet_age, is_valid_pet_weigth
from entities.veterinarians.validations import is_valid_name
from utils.constants import HEADER_OWNER, HEADER_PET
from utils.uiHelper import create_scrollable_container, on_focusOut_validation, show_modal_selector, show_radio_button

def on_create_new_pet(root, container):
    modal_create = tk.Toplevel(root)
    modal_create.title(f"Crear nueva Mascota")
    modal_create.geometry("500x500")
    
    for prop in HEADER_PET:
        if prop == "owner_id":
            owner_frame = tk.Frame(modal_create)
            owner_frame.pack(anchor="w")
            tk.Label(owner_frame, text=f"Dueño:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_owner_id = {"id": None}
            owners = list(map(lambda o: [o[HEADER_OWNER.index("owner_id")], o[HEADER_OWNER.index("nombre")], o[HEADER_OWNER.index("apellido")]], get_all_owners_active()))
            owner_label_variable = tk.StringVar()
            tk.Label(owner_frame, textvariable=owner_label_variable).pack(anchor="w", padx=10, pady=(10, 0))
            def on_owner_selected(owner):
                id, nombre, apellido = owner
                completed_name = f"{nombre} {apellido}"
                owner_label_variable.set(completed_name)
                selected_owner_id["id"] = id
            tk.Button(owner_frame, text="Elegir", command=lambda:show_modal_selector(modal_create, owners, f"Seleccione un Dueño", on_owner_selected)).pack(side="right", padx=5)
                
        elif prop == "nombre":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_name = tk.Entry(modal_create)
            input_name.pack(fill="x", padx=10)
            input_name.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "edad":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_age = tk.Entry(modal_create)
            input_age.pack(fill="x", padx=10)
            input_age.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_pet_age))
        elif prop == "peso":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_weight = tk.Entry(modal_create)
            input_weight.pack(fill="x", padx=10)
            input_weight.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_pet_weigth))
        elif prop == "especie":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_especie = tk.Entry(modal_create)
            input_especie.pack(fill="x", padx=10)
        elif prop == "raza":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_raza = tk.Entry(modal_create)
            input_raza.pack(fill="x", padx=10)
        elif prop == "sexo":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_gender_option = show_radio_button(modal_create,[('Macho','macho'),('Hembra','hembra')])
            
    def save_data():
        new_pet = []
        hasError = False

        if (not selected_owner_id['id'] or 
            not is_valid_name(input_name.get()) or 
            not is_valid_pet_age(input_age.get()) or 
            not is_valid_pet_weigth(input_weight.get()) or 
            not input_especie.get() or 
            not input_raza.get() or
            not is_valid_gender(selected_gender_option.get())):
                hasError = True
                
        new_pet.append(get_next_pet_id())
        new_pet.append(input_name.get())
        new_pet.append(input_especie.get())
        new_pet.append(input_raza.get())
        new_pet.append(input_age.get())
        new_pet.append(selected_owner_id['id'])
        new_pet.append(input_weight.get())
        new_pet.append(selected_gender_option.get())
        new_pet.append(True)
        
        if not hasError:
            save_data_pet(new_pet)
            modal_create.destroy()
            load_dynamic_table(container, root)
        else:
            messagebox.showerror("Error", "Algunos datos son incorrectos.", parent=modal_create)
            return
    
    btn_frame = tk.Frame(modal_create, pady=20)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Cancelar", command=modal_create.destroy).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Guardar", bg="#4CAF50", fg="white", command=save_data).pack(side="left", padx=5)


def on_search_pet(input_search, list_frame, root):
    texto_busqueda = input_search.get().lower()
    
    entities = get_all_pets()
    string_array = [('|').join(list(e)) for e in entities]
    for entity in string_array:
        match = texto_busqueda.lower() in entity.lower()
        if match:
            entity_tuple = get_readable_pet(entity.split('|'))
            load_dynamic_table(list_frame, root, entity_tuple)

def modify_pet(id, root, container):
    modal_modify = tk.Toplevel(root)
    modal_modify.title(f"Editar Mascota ID: {id}")
    modal_modify.geometry("500x500")

    current_data = get_data_pet_by_id(id)
    for prop in HEADER_PET:
        if prop == "owner_id":
            owner_frame = tk.Frame(modal_modify)
            owner_frame.pack(anchor="w")
            tk.Label(owner_frame, text=f"Dueño:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_owner_id = {"id": current_data[HEADER_PET.index(prop)]}
            owners = list(map(lambda o: [o[HEADER_OWNER.index("owner_id")], o[HEADER_OWNER.index("nombre")], o[HEADER_OWNER.index("apellido")]], get_all_owners_active()))
            current_owner = get_data_owner_by_id(selected_owner_id["id"])
            owner_label_variable = tk.StringVar(value=f"{current_owner[HEADER_OWNER.index("nombre")]} {current_owner[HEADER_OWNER.index("apellido")]}")
            tk.Label(owner_frame, textvariable=owner_label_variable).pack(anchor="w", padx=10, pady=(10, 0))
            def on_owner_selected(owner):
                id, nombre, apellido = owner
                completed_name = f"{nombre} {apellido}"
                owner_label_variable.set(completed_name)
                selected_owner_id["id"] = id
            tk.Button(owner_frame, text="Elegir", command=lambda:show_modal_selector(modal_modify, owners, f"Seleccione un Dueño", on_owner_selected)).pack(side="right", padx=5)
        elif prop == "nombre":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_name = tk.Entry(modal_modify)
            input_name.pack(fill="x", padx=10)
            input_name.insert(0, current_data[HEADER_PET.index(prop)])
            input_name.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_name))
        elif prop == "edad":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_age = tk.Entry(modal_modify)
            input_age.pack(fill="x", padx=10)
            input_age.insert(0, current_data[HEADER_PET.index(prop)])
            input_age.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_pet_age))
        elif prop == "peso":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_weight = tk.Entry(modal_modify)
            input_weight.pack(fill="x", padx=10)
            input_weight.insert(0, float(current_data[HEADER_PET.index(prop)]))
            input_weight.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_pet_weigth))
        elif prop == "especie":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_especie = tk.Entry(modal_modify)
            input_especie.pack(fill="x", padx=10)
            input_especie.insert(0, current_data[HEADER_PET.index(prop)])
        elif prop == "raza":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_raza = tk.Entry(modal_modify)
            input_raza.pack(fill="x", padx=10)
            input_raza.insert(0, current_data[HEADER_PET.index(prop)])
        elif prop == "sexo":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_gender_option = show_radio_button(modal_modify,[('Macho','Macho'),('Hembra','Hembra')], current_data[HEADER_PET.index(prop)]) 
    def save_data():
        updated_pet = current_data.copy()
        hasError = False
        if (not selected_owner_id['id'] or 
            not is_valid_name(input_name.get()) or 
            not is_valid_pet_age(input_age.get()) or 
            not is_valid_pet_weigth(input_weight.get()) or 
            not input_especie.get() or 
            not input_raza.get() or
            not is_valid_gender(selected_gender_option.get())):
                hasError = True
                
        updated_pet[HEADER_PET.index('nombre')] = input_name.get()
        updated_pet[HEADER_PET.index('especie')] = input_especie.get()
        updated_pet[HEADER_PET.index('raza')] = input_raza.get()
        updated_pet[HEADER_PET.index('edad')] = input_age.get()
        updated_pet[HEADER_PET.index('owner_id')] = selected_owner_id['id']
        updated_pet[HEADER_PET.index('peso')] = input_weight.get()
        updated_pet[HEADER_PET.index('sexo')] = selected_gender_option.get()
        
        if not hasError:
            update_data_pets(updated_pet)
            modal_modify.destroy()
            load_dynamic_table(container, root)
        else:
            messagebox.showerror("Error", "Algunos datos son incorrectos.", parent=modal_modify)
            return
    
    btn_frame = tk.Frame(modal_modify, pady=20)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Cancelar", command=modal_modify.destroy).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Guardar", bg="#4CAF50", fg="white", command=save_data).pack(side="left", padx=5)

def delete_pet(id, root, list_container):
    if messagebox.askyesno("Confirmar", f"¿Borrar ID {id}?"):
        delete_pet_by_id(id)
        load_dynamic_table(list_container, root)

def load_dynamic_table(container, root, filtered_data=[]):
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
    
    data = []
    if filtered_data:
        data.append(filtered_data)
    else:
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
                  command=lambda i=row_id: delete_pet(i, root, container)).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Editar", 
                  command=lambda i=row_id: modify_pet(i, root, container)).pack(side="left", padx=2)

def create_list_frame_pet(root):
    
    frame_controles = tk.Frame(root, pady=10, padx=10, bg="#eee")
    frame_controles.pack(fill="x")

    tk.Label(frame_controles, text="Buscar:", bg="#eee").pack(side="left")

    input_search = tk.Entry(frame_controles)
    input_search.pack(side="left", padx=5)

    btn_buscar = tk.Button(frame_controles, text="🔍", command=lambda: on_search_pet(input_search, list_frame, root))
    btn_buscar.pack(side="left")

    btn_nuevo = tk.Button(frame_controles, text="+ Nueva Mascota", bg="#4CAF50", fg="white", command=lambda: on_create_new_pet(root, list_frame))
    btn_nuevo.pack(side="right")
    
    list_frame = create_scrollable_container(root)
    load_dynamic_table(list_frame, root)