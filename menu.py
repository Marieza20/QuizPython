salir = False

nombre = ["Santiago","Jorge","Luis","Carlos","Juan","Pedro","Pablo","Diego","Andres"]

while salir == False:
    opc = int(input("Menú Interactivo\n1. Mostrar Mensajes\n2. Mostrar Nombres\n3. Salir\nDigite la opción: "))
    
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