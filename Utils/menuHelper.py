def mostrar_menu(titulo, opciones, acciones):
    """
    Muestra un menu por consola en base a las opciones y acciones que sele pas apor parametro
    
    Ejemplo:
    
        titulo = "Hola soy el titulo"
        
        opciones = ["Opcion 1","Opcion 2"]
        
        def accion_uno():
            print("Hola soy accion 1")
            
        def accion_dos():
            print("Hola soy accion 2")

        acciones = [accion_uno, accion_dos]

        mostrar_menu(titulo, opciones, acciones)
    """
    accion_elegida = -1
    while accion_elegida != 0:
        print(titulo)
        for i in range(len(opciones)):
            print(f'{i + 1} - {opciones[i]}')
        print("Ingrese 0 para terminarel programa.")
        accion_elegida = int(input("¿Qué acción desea realizar? : "))
        acciones[accion_elegida - 1]()