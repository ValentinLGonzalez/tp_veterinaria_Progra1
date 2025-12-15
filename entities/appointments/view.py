import tkinter as tk
from tkinter import messagebox
from entities.appointments.data import get_next_appointment_id, save_data_appointment, update_data_appointment
from entities.appointments.entity import READABLE_HEADER,delete_appointment_by_id, get_appointment_by_id, get_readable_appointment, show_all_appointments_active
from entities.appointments.validations import is_valid_appointment_date, is_valid_appointment_time
from entities.pets.data import get_all_pets, get_data_pet_by_id
from entities.treatments.data import get_all_treatments
from entities.treatments.entity import get_treatment_by_id
from entities.veterinarians.controller import show_all_veterinarians_action
from entities.veterinarians.entity import get_veterinarian_by_id
from utils.constants import HEADER_APPOINTMENT, HEADER_PET, HEADER_VETERINARIAN
from utils.uiHelper import create_scrollable_container, on_focusOut_validation, show_modal_selector

def on_create_new_appointment(root, container):
    modal_create = tk.Toplevel(root)
    modal_create.title(f"Crear nuevo turno")
    modal_create.geometry("500x500")
    
    for prop in HEADER_APPOINTMENT:
        if prop == "veterinarian_id":
            veterinarian_frame = tk.Frame(modal_create)
            veterinarian_frame.pack(anchor="w")
            tk.Label(veterinarian_frame, text=f"Veterinario:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_veterinarian_id = {"id": None}
            veterinarians = list(map(lambda o: [o[HEADER_VETERINARIAN.index("veterinarian_id")], o[HEADER_VETERINARIAN.index("nombre")], o[HEADER_VETERINARIAN.index("apellido")]], show_all_veterinarians_action()))
            veterinarian_label_variable = tk.StringVar()
            tk.Label(veterinarian_frame, textvariable=veterinarian_label_variable).pack(anchor="w", padx=10, pady=(10, 0))
            def on_veterinarian_selected(veterinarian):
                id, nombre, apellido = veterinarian
                veterinarian_label_variable.set(f"{nombre} {apellido}")
                selected_veterinarian_id["id"] = id
            tk.Button(veterinarian_frame, text="Elegir", command=lambda:show_modal_selector(modal_create, veterinarians, f"Seleccione un Veterinario", on_veterinarian_selected)).pack(padx=5)  
        elif prop == "pet_id":
            pet_frame = tk.Frame(modal_create)
            pet_frame.pack(anchor="w")
            tk.Label(pet_frame, text=f"Mascota:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_pet_id = {"id": None}
            pet = list(map(lambda p: [p[HEADER_PET.index("pet_id")], p[HEADER_PET.index("nombre")]], get_all_pets()))
            pet_label_variable = tk.StringVar()
            tk.Label(pet_frame, textvariable=pet_label_variable).pack(anchor="w", padx=10, pady=(10, 0))
            def on_pet_selected(pet):
                id, nombre = pet
                pet_label_variable.set(f"{nombre}")
                selected_pet_id["id"] = id
            tk.Button(pet_frame, text="Elegir", command=lambda:show_modal_selector(modal_create, pet, f"Seleccione una Mascota", on_pet_selected)).pack(padx=5)  
        elif prop == "fecha":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_date = tk.Entry(modal_create)
            input_date.pack(fill="x", padx=10)
            input_date.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_appointment_date))
        elif prop == "hora":
            tk.Label(modal_create, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_time = tk.Entry(modal_create)
            input_time.pack(fill="x", padx=10)
            input_time.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_appointment_time))
        elif prop == "treatment_id":
            treatment_frame = tk.Frame(modal_create)
            treatment_frame.pack(anchor="w")
            tk.Label(treatment_frame, text=f"Tratamiento:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_treatment_id = {"id": None}
            treatment = list(map(lambda t: [t['id'], t['description']], get_all_treatments()))
            treatment_label_variable = tk.StringVar()
            tk.Label(treatment_frame, textvariable=treatment_label_variable).pack(anchor="w", padx=10, pady=(10, 0))
            def on_treatment_selected(treatment):
                id, description = treatment
                treatment_label_variable.set(f"{description}")
                selected_treatment_id["id"] = id
            tk.Button(treatment_frame, text="Elegir", command=lambda:show_modal_selector(modal_create, treatment, f"Seleccione una Tratamiento", on_treatment_selected)).pack(padx=5)

            
    def save_data():
        new_appointment = []
        hasError = False

        if (not selected_pet_id['id'] or 
            not is_valid_appointment_date(input_date.get()) or 
            not is_valid_appointment_time(input_time.get()) or 
            not selected_treatment_id['id'] or
            not selected_veterinarian_id['id']):
                hasError = True
                
        new_appointment.append(get_next_appointment_id())
        new_appointment.append(selected_pet_id['id'])
        new_appointment.append(input_date.get())
        new_appointment.append(input_time.get())
        new_appointment.append(selected_treatment_id['id'])
        new_appointment.append(selected_veterinarian_id['id'])
        new_appointment.append(True)
        
        if not hasError:
            save_data_appointment(new_appointment)
            modal_create.destroy()
            load_dynamic_table(container, root)
        else:
            messagebox.showerror("Error", "Algunos datos son incorrectos.", parent=modal_create)
            return
    
    btn_frame = tk.Frame(modal_create, pady=20)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Cancelar", command=modal_create.destroy).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Guardar", bg="#4CAF50", fg="white", command=save_data).pack(side="left", padx=5)


def on_search_appointment(input_search, list_frame, root):
    texto_busqueda = input_search.get().lower()
    
    entities = show_all_appointments_active()
    string_array = [('|').join(list(e)) for e in entities]
    for entity in string_array:
        match = texto_busqueda.lower() in entity.lower()
        if match:
            entity_tuple = get_readable_appointment(get_appointment_by_id(entity[HEADER_APPOINTMENT.index('appointment_id')]))
            load_dynamic_table(list_frame, root, entity_tuple)

def modify_appointment(id, root, container):
    modal_modify = tk.Toplevel(root)
    modal_modify.title(f"Editar Mascota ID: {id}")
    modal_modify.geometry("500x500")

    current_data = get_appointment_by_id(id)
    for prop in HEADER_APPOINTMENT:
        if prop == "veterinarian_id":
            veterinarian_frame = tk.Frame(modal_modify)
            veterinarian_frame.pack(anchor="w")
            tk.Label(veterinarian_frame, text=f"Veterinario:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_veterinarian_id = {"id": current_data[HEADER_APPOINTMENT.index(prop)]}
            veterinarians = list(map(lambda o: [o[HEADER_VETERINARIAN.index("veterinarian_id")], o[HEADER_VETERINARIAN.index("nombre")], o[HEADER_VETERINARIAN.index("apellido")]], show_all_veterinarians_action()))
            current_veterinarian = get_veterinarian_by_id(selected_veterinarian_id["id"])
            veterinarian_label_variable = tk.StringVar(value=f"{current_veterinarian[HEADER_VETERINARIAN.index("nombre")]} {current_veterinarian[HEADER_VETERINARIAN.index("apellido")]}")
            tk.Label(veterinarian_frame, textvariable=veterinarian_label_variable).pack(anchor="w", padx=10, pady=(10, 0))
            def on_veterinarian_selected(veterinarian):
                id, nombre, apellido = veterinarian
                veterinarian_label_variable.set(f"{nombre} {apellido}")
                selected_veterinarian_id["id"] = id
            tk.Button(veterinarian_frame, text="Elegir", command=lambda:show_modal_selector(modal_modify, veterinarians, f"Seleccione un Veterinario", on_veterinarian_selected)).pack(side="right", padx=5)  
        elif prop == "pet_id":
            pet_frame = tk.Frame(modal_modify)
            pet_frame.pack(anchor="w")
            tk.Label(pet_frame, text=f"Mascota:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_pet_id = {"id": current_data[HEADER_APPOINTMENT.index(prop)]}
            pet = list(map(lambda p: [p[HEADER_PET.index("pet_id")], p[HEADER_PET.index("nombre")]], get_all_pets()))
            current_pet = get_data_pet_by_id(selected_pet_id["id"])
            print(current_pet)
            pet_label_variable = tk.StringVar(value=f'{current_pet[HEADER_PET.index('nombre')]}')
            tk.Label(pet_frame, textvariable=pet_label_variable).pack(anchor="w", padx=10, pady=(10, 0))
            def on_pet_selected(pet):
                id, nombre = pet
                pet_label_variable.set(f"{nombre}")
                selected_pet_id["id"] = id
            tk.Button(pet_frame, text="Elegir", command=lambda:show_modal_selector(modal_modify, pet, f"Seleccione una Mascota", on_pet_selected)).pack(side="right", padx=5)  
        elif prop == "fecha":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_date = tk.Entry(modal_modify)
            input_date.pack(fill="x", padx=10)
            input_date.insert(0, current_data[HEADER_APPOINTMENT.index(prop)])
            input_date.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_appointment_date))
        elif prop == "hora":
            tk.Label(modal_modify, text=f"{prop.capitalize()}:").pack(anchor="w", padx=10, pady=(10, 0))
            input_time = tk.Entry(modal_modify)
            input_time.pack(fill="x", padx=10)
            input_time.insert(0, current_data[HEADER_APPOINTMENT.index(prop)])
            input_time.bind("<FocusOut>", lambda e: on_focusOut_validation(e, is_valid_appointment_time))
        elif prop == "treatment_id":
            treatment_frame = tk.Frame(modal_modify)
            treatment_frame.pack(anchor="w")
            tk.Label(treatment_frame, text=f"Tratamiento:").pack(anchor="w", padx=10, pady=(10, 0))
            selected_treatment_id = {"id": current_data[HEADER_APPOINTMENT.index(prop)]}
            treatment = list(map(lambda t: [t['id'], t['description']], get_all_treatments()))
            current_treatment = get_treatment_by_id(selected_treatment_id["id"])
            treatment_label_variable = tk.StringVar(value=f'{current_treatment['description']}')
            tk.Label(treatment_frame, textvariable=treatment_label_variable).pack(anchor="w", padx=10, pady=(10, 0))
            def on_treatment_selected(treatment):
                id, description = treatment
                treatment_label_variable.set(f"{description}")
                selected_treatment_id["id"] = id
            tk.Button(treatment_frame, text="Elegir", command=lambda:show_modal_selector(modal_modify, treatment, f"Seleccione una Tratamiento", on_treatment_selected)).pack(side="right", padx=5)

    def save_data():
        updated_appointment = current_data.copy()
        hasError = False
        if (not selected_pet_id['id'] or 
            not is_valid_appointment_date(input_date.get()) or 
            not is_valid_appointment_time(input_time.get()) or 
            not selected_treatment_id['id'] or
            not selected_veterinarian_id['id']):
                hasError = True
          
        updated_appointment[HEADER_APPOINTMENT.index('pet_id')] = selected_pet_id['id']
        updated_appointment[HEADER_APPOINTMENT.index('fecha')] = input_date.get()
        updated_appointment[HEADER_APPOINTMENT.index('hora')] = input_time.get()
        updated_appointment[HEADER_APPOINTMENT.index('treatment_id')] = selected_treatment_id['id']
        updated_appointment[HEADER_APPOINTMENT.index('veterinarian_id')] = selected_veterinarian_id['id']
        
        if not hasError:
            update_data_appointment(updated_appointment)
            modal_modify.destroy()
            load_dynamic_table(container, root)
        else:
            messagebox.showerror("Error", "Algunos datos son incorrectos.", parent=modal_modify)
            return
    
    btn_frame = tk.Frame(modal_modify, pady=20)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Cancelar", command=modal_modify.destroy).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Guardar", bg="#4CAF50", fg="white", command=save_data).pack(side="left", padx=5)

def delete_appointment(id, root, list_container):
    if messagebox.askyesno("Confirmar", f"¿Borrar ID {id}?"):
        delete_appointment_by_id(id)
        load_dynamic_table(list_container, root)

def load_dynamic_table(container, root, filtered_data=[]):
    for widget in container.winfo_children():
        widget.destroy()

    try:
        index_to_show = [READABLE_HEADER.index(col) for col in READABLE_HEADER]
        index_id = HEADER_APPOINTMENT.index("appointment_id")
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
        data = show_all_appointments_active() 
        
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
                  command=lambda i=row_id: delete_appointment(i, root, container)).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Editar", 
                  command=lambda i=row_id: modify_appointment(i, root, container)).pack(side="left", padx=2)

def create_list_frame_appointment(root):
    
    frame_controles = tk.Frame(root, pady=10, padx=10, bg="#eee")
    frame_controles.pack(fill="x")

    tk.Label(frame_controles, text="Buscar:", bg="#eee").pack(side="left")

    input_search = tk.Entry(frame_controles)
    input_search.pack(side="left", padx=5)

    btn_buscar = tk.Button(frame_controles, text="🔍", command=lambda: on_search_appointment(input_search, list_frame, root))
    btn_buscar.pack(side="left")

    btn_nuevo = tk.Button(frame_controles, text="+ Nuevo Turno", bg="#4CAF50", fg="white", command=lambda: on_create_new_appointment(root, list_frame))
    btn_nuevo.pack(side="right")
    
    list_frame = create_scrollable_container(root)
    load_dynamic_table(list_frame, root)