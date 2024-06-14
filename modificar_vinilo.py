import agregar_vinilo

def modificar_vinilo(tit):
    print("Opción 2 elegida - modificar_vinilo \n")
    while True:
        if tit.title() in agregar_vinilo.discografia:
            disco = agregar_vinilo.discografia[tit.title()]
            print("Datos actuales del disco")
            print(disco)
            break
        else:
            print("No se encuentra el titulo que ingresó. Intente nuevamente")
            continue
        
        
    opcion_modificar = input("¿Desea cambiar los campos del disco? (s/n): ")
        
    if opcion_modificar.lower() == "s":
        autor = input("ingrese el nuevo nombre del autor: ")

        titulo = input("ingrese el nuevo nombre del titulo: ")

        anio = input("ingrese el nuevo año del disco: ")
    
        agregar_vinilo.discografia["autor"] = agregar_vinilo.discografia[tit]
        
        agregar_vinilo.discografia["titulo"] = agregar_vinilo.titulo
        
        agregar_vinilo.discografia["año"] = agregar_vinilo.anio
        
        print("Disco modificado exitosamente.")
    else:
        print("No se encontró ningún disco con ese título.")