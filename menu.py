import agregar_vinilo
import modificar_vinilo

def menu():
    while True:
        print("=" * 27)    
        print("1. Agregar nuevo vinilo") 
        print("2. Modificar vinilo")
        print("3. Eliminar vinilo")
        print("4. Mostrar discografia")
        print("5. Buscar vinilo por titulo")
        print("6. Salir")
        print("=" * 27, "\n")

        opcion = input("Ingrese una opción: ")
        print("")

        if opcion == "1":
            print("=" * 27)
            print("Opción 1 elegida - agregar_vinilo")
            print("=" * 27, "\n")
            
            autor = input("ingrese el nombre del autor: ")
    
            titulo = input("ingrese el titulo del disco: ")

            anio = input("ingrese el año del disco: ")
            
            agregar_vinilo.agregar_vinilo(autor, titulo, anio)

        elif opcion == "2":
            print("Opción 2 elegida - modificar_vinilo \n")
            
            titulo =input("Ingresa el titulo del vinilo que desea modificar: ")
            
            modificar_vinilo.modificar_vinilo(titulo)
        
        elif opcion == "3":
            titulo = input("Ingrese el título del disco a eliminar: ")
            
        elif opcion == "4":
            if agregar_vinilo.discografia:
                print("discografia: ")
                print(agregar_vinilo.discografia)
            else:
                print("La discografia esta vacia")
            
        elif opcion == "5":
            buscar = input(print("Ingrese el titulo del disco que desea buscar: "))
            disco = agregar_vinilo.discografia[buscar]
            print("Datos del disco")
            print(disco)

        elif opcion == "6":
            print("¡Hasta luego! \n")
            break
        else:
            print("Opción incorrecta. Por favor, ingrese una opción válida. \n")