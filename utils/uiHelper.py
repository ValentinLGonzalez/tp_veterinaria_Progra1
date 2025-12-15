import tkinter as tk
from tkinter import SINGLE, ttk
from tkinter import messagebox

def on_mousewheel(event, parent):
    parent.yview_scroll(int(-1*(event.delta/120)), "units")
    
def create_scrollable_container(parent):
    container = tk.Frame(parent, padx=10, pady=10)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def on_canvas_configure(event):
        canvas.itemconfig(window_id, width=event.width)

    canvas.bind("<Configure>", on_canvas_configure)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    canvas.bind_all("<MouseWheel>", lambda e: on_mousewheel(e, canvas))

    return scrollable_frame

def add_scroll_to_widget(parent, widget_to_scroll):
    container = tk.Frame(parent)
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    
    window_id = canvas.create_window((0, 0), window=widget_to_scroll, anchor="nw")

    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    widget_to_scroll.bind("<Configure>", update_scrollregion)

    def fit_width(event):
        canvas.itemconfig(window_id, width=event.width)
    
    canvas.bind("<Configure>", fit_width)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    canvas.bind_all("<MouseWheel>", lambda e: on_mousewheel(e, canvas))

    return container

def on_focusOut_validation(event, validatorHandler):
    widget = event.widget
    isValid = validatorHandler(widget.get())
    if not isValid:
        widget.configure(bg="#ffcccc")
    else:
        widget.configure(bg="#ccffcc")

def show_radio_button(container, options, value_default=""):
    selected_option = tk.StringVar(value=value_default)
    radios = []
    for text, value in options:
        radios.append(ttk.Radiobutton(container, text=text, value=value, variable=selected_option).pack(fill="x", padx=10))
    return selected_option

def show_modal_selector(container, options, title, callback):
    modal_container = tk.Toplevel(container)
    modal_container.title(title)
    modal_container.geometry("200x400")
    listbox = tk.Listbox(modal_container)
    listbox.config(selectmode=SINGLE)
    for item in options:
        listbox.insert(tk.END, item)

    listbox.pack(pady=10)
    
    def on_confirm():
        index = listbox.curselection()
        if not index:
            messagebox.showwarning("Atención", "Por favor selecciona una opción")
            return
        selected_index = index[0]
        value_text = listbox.get(selected_index)
        if callback:
            callback(value_text)
        modal_container.destroy()
    
    listbox.bind("<<ListboxSelect>>",lambda e: on_confirm())
    tk.Button(modal_container, text="Cerrar", command=modal_container.destroy).pack(side="bottom", padx=5)
    add_scroll_to_widget(container, modal_container)

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
        
def load_info_table_set_individual(container, data, headers):
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
        tk.Label(row_frame, text=str(dic_row), width=40, anchor="w", font=font).pack(side='left', padx=5)
        
def load_info_table_set(container, data, headers):
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
        tk.Label(row_frame, text=str(dic_row), width="20", anchor="w", font=font).pack(side='left', padx=5)
        tk.Label(row_frame, text=str(data[dic_row]), width=20, anchor="w", font=font).pack(side='left', padx=5)
