from colorama import init, Fore, Back, Style

salir = False
datos = {
    "producto": "Nike Air Max 270",
    "talla": 42,
    "color": "Rojo",
    "precio": 150,
    "stock": 20,
}

def editar(datos):
    dato = input("Ingrese la clave del producto a editar: ")
    if dato in datos:
        nuevo_valor = input(f"Ingrese el nuevo valor para {dato}: ")
        datos[dato] = nuevo_valor
        print(f"El valor de {dato} ha sido actualizado a {nuevo_valor}.")
        print(datos)
    else:
        print(f"La clave {dato} no existe en los datos.")

print("----------------------------")

def eliminar(datos):
    datoEliminar = input("Ingrese la clave del producto a eliminar: ")
    if datoEliminar in datos:
        del datos[datoEliminar]
        print(f"El valor de {datoEliminar} ha sido eliminado.")
        print(datos)
    else:
        print(f"La clave {datoEliminar} no existe en los datos.")

def opciones(salir):
    while salir == False:
        opc = int(input("Menú Interactivo" + Fore.GREEN + "\n1. Editar" + Fore.RED + "\n2. Eliminar" + Fore.CYAN + "\n3. Salir" + Fore.WHITE + "\nDigite la opción: "))
        if opc == 1:
            editar(datos)
        elif opc == 2:
            eliminar(datos)
        elif opc == 3:
            print("Saliendo...")
            salir = True
        else:
            print("Opción no válida, intente nuevamente.")
        print("----------------------------")
        
opciones(salir)