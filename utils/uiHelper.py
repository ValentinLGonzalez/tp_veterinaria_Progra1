import tkinter as tk
from tkinter import ttk

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
        canvas.itemconfig(window_id, width=event.width) # <--- CLAVE

    canvas.bind("<Configure>", on_canvas_configure)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    return scrollable_frame

def on_focusOut_validation(event, validatorHandler):
    widget = event.widget
    isValid = validatorHandler(widget.get())
    if not isValid:
        widget.configure(bg="#ffcccc")
    else:
        widget.configure(bg="#ccffcc")

def show_radio_button(container, options):
    selected_option = tk.StringVar()
    radios = []
    for text, value in options:
        radios.append(ttk.Radiobutton(container, text=text, value=value, variable=selected_option).pack(fill="x", padx=10))
    return selected_option