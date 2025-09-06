from utils.entitiesHelper import create_arrays
from entities.veterinarians import add_veterinarian_action, delete_veterinarian_action, modify_veterinarian_action, show_all_veterinarians_action
from entities.appointments import add_appointment_action, delete_appointment_action, modify_appointment_action, show_all_appointments_action

def main():
    #-------------------------------------------------
    # Inicialización de variables
    #---------------------------------------------------------------- ------------------------------
    owners, pets, appointments, veterinarians = create_arrays()


    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de Veterinarios")
            print("[2] Gestion de Turnos")
            print("[3] Opción 3")
            print("[4] Opción 4")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":   # Opción 1
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE VETERINARIOS")
                    print("---------------------------")
                    print("[1] Agregar Veterinario")
                    print("[2] Modificar un Veterinario por DNI")
                    print("[3] Mostrar todos los Veterinarios")
                    print("[4] Eliminar Veterinario por DNI")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0": # Opción salir del submenú
                    break # No salimos del programa, volvemos al menú anterior
                elif opcion == "1":   # Opción 1
                    add_veterinarian_action(veterinarians)
                elif opcion == "2":   # Opción 2
                    modify_veterinarian_action(veterinarians)
                elif opcion == "3":   # Opción 3
                    show_all_veterinarians_action(veterinarians)
                elif opcion == "4":   # Opción 4
                    delete_veterinarian_action(veterinarians)

        elif opcion == "2":   # Opción 2
             while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE TURNOS")
                    print("---------------------------")
                    print("[1] Sacar Turno")
                    print("[2] Modificar Turno")
                    print("[3] Mostrar todos los Turnos")
                    print("[4] Eliminar un Turno")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcion = input("Seleccione una opción: ")
                    if opcion in [str(i) for i in range(0, opciones + 1)]: 
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcion == "0": # Opción salir del submenú
                    break # No salimos del programa, volvemos al menú anterior
                elif opcion == "1":   # Opción 1
                    add_appointment_action(appointments, pets, veterinarians, owners)
                elif opcion == "2":   # Opción 2
                    modify_appointment_action(appointments, pets, veterinarians, owners)
                elif opcion == "3":   # Opción 3
                    show_all_appointments_action(appointments, pets, veterinarians)
                elif opcion == "4":   # Opción 4
                    delete_appointment_action(appointments, pets, veterinarians, owners)

        # elif opcion == "3":   # Opción 3
        #     ...
        # elif opcion == "4":   # Opción 4
        #     ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()
