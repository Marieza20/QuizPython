from colorama import init, Fore, Back, Style

salir = False
nombre = ["Santiago","Jorge","Luis","Carlos","Juan","Pedro","Pablo","Diego","Andres"]

def opciones(salir):
    while salir == False:
        opc = int(input("Menú Interactivo" + Fore.CYAN + "\n1. Mostrar Mensajes" + Fore.MAGENTA + "\n2. Mostrar Nombres" + Fore.RED + "\n3. Salir" + Fore.WHITE + "\nDigite la opción: "))
    
        if opc == 1:
            print("Los grandes logros de cualquier persona generalmente dependen de muchas manos, corazones y mentes.")
            print("-Walter Elias Disney")
        elif opc == 2:
            print(nombre)
        elif opc == 3:
            print("Saliendo...")
            salir = True
        else:
            print("Opción no válida, intente nuevamente.")
        print("----------------------------")
        
opciones(salir)