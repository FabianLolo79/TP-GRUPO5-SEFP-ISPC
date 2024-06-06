import  agregar_vinilo
import modificar_vinilo
import eliminar_vinilo
import mostrar_discografia
import buscar

def menu():
    while True:
        print("=" * 27)    
        print("1. Agregar nuevo vinilo") 
        print("2. Modificar vinilo")
        print("3. Eliminar vinilo")
        print("4. Mostrar discografia")
        print("5. Buscar vinilo por titulo")
        print("6. Salir")
        print("=" * 27)

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_vinilo.agregar_vinilo()

        elif opcion == "2":
            modificar_vinilo.modificar_vinilo()
            
        elif opcion == "3":
            eliminar_vinilo.eliminar_vinilo()
            
        elif opcion == "4":
            mostrar_discografia.mostrar_discografia()
            
        elif opcion == "5":
            buscar.buscar()

        elif opcion == "6":
            print("¡Hasta luego! \n")
            break
        else:
            print("Opción incorrecta. Por favor, ingrese una opción válida. \n")