# Diccionario para almacenar la discografía
discografia = {}

def menu():
    # Loop infinito para mostrar el menú y procesar las opciones
    while True:
        print("\n******")
        print("Bienvenido a la discografía del grupo 5")
        print("******")
        print("1. Agregar nuevo disco") 
        print("2. Modificar disco")
        print("3. Eliminar disco")
        print("4. Mostrar discografía")
        print("5. Buscar disco por título")
        print("6. Salir")
        print("******\n")

        # Pedir al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")

        # Procesar la opción seleccionada
        if opcion == "1":
            # Agregar un nuevo disco
            agregar_nuevo_disco()
        elif opcion == "2":
            # Modificar un disco existente
            modificar_disco()
        elif opcion == "3":
            # Eliminar un disco
            eliminar_disco()
        elif opcion == "4":
            # Mostrar la discografía completa
            mostrar_discografia()
        elif opcion == "5":
            # Buscar un disco por título
            buscar_disco_por_titulo()
        elif opcion == "6":
            # Salir del programa
            print("¡Hasta luego!")
            break
        else:
            # Opción inválida
            print("Opción incorrecta. Por favor, ingrese una opción válida.")

def agregar_nuevo_disco():
    # Agregar un nuevo disco a la discografía
    print("=" * 27)
    print("Opción 1 elegida - Agregar nuevo disco")
    print("=" * 27, "\n")
    
    # Pedir al usuario que ingrese la información del disco
    nombre_artista = input("Ingrese el nombre del artista: ").capitalize()
    apellido_artista = input("Ingrese el apellido del artista: ").capitalize()
    artista = f"{nombre_artista} {apellido_artista}"
    
    titulo = input("Ingrese el título del disco: ").title()
    anio = input("Ingrese el año del disco: ")
    genero = input("Ingrese el género del disco (opcional): ")
    precio = input("Ingrese el precio del disco (opcional): ")
    if precio == '':
        precio = None

    imagen_cara = input("Ingrese el nombre del archivo de la imagen de la cara (ej. portada.jpg): ")
    imagen_contra_cara = input("Ingrese el nombre del archivo de la imagen de la contracara (ej. contraportada.jpg): ")
    imagen_portada = (imagen_cara, imagen_contra_cara)

    # Crear una lista para almacenar las canciones del disco
    disco = [titulo, anio, artista, genero, precio, imagen_portada, [], []]

    # Pedir al usuario que ingrese las canciones del lado A
    while True:
        cancion_numero = input("Ingrese el número de la canción para el lado A (o 'fin' para terminar): ")
        if cancion_numero.lower() == 'fin':
            break
        cancion_nombre = input("Ingrese el nombre de la canción: ")
        disco[6].append((cancion_numero, cancion_nombre))

    # Pedir al usuario que ingrese las canciones del lado B
    while True:
        cancion_numero = input("Ingrese el número de la canción para el lado B (o 'fin' para terminar): ")
        if cancion_numero.lower() == 'fin':
            break
        cancion_nombre = input("Ingrese el nombre de la canción: ")
        disco[7].append((cancion_numero, cancion_nombre))

    # Agregar el disco a la discografía
    discografia[titulo] = disco
    print("Disco agregado exitosamente")
    
def modificar_disco():
    # Modificar un disco existente
    print("=" * 27)
    print("Opción 2 elegida - Modificar disco")
    print("=" * 27, "\n")
    
    # Pedir al usuario que ingrese el título del disco a modificar
    titulo_buscar = input("Ingrese el título del disco que desea modificar: ").casefold()
    
    # Buscar el disco en la discografía
    for titulo, disco in discografia.items():
        if titulo_buscar == titulo.casefold():
            # Mostrar los datos actuales del disco
            print("Datos actuales del disco:")
            print(disco)

            # Pedir al usuario que confirme si desea modificar los campos del disco
            opcion_modificar = input("¿Desea cambiar los campos del disco? (s/n): ")
            if opcion_modificar.lower() == "s":
                # Modificar los campos del disco
                nombre_artista = input("Ingrese el nuevo nombre del artista: ").capitalize()
                apellido_artista = input("Ingrese el nuevo apellido del artista: ").capitalize()
                artista = f"{nombre_artista} {apellido_artista}"
                disco.pop(2)
                disco.insert(2, artista)

                titulo_nuevo = input("Ingrese el nuevo título del disco: ")
                disco.pop(0)
                disco.insert(0, titulo_nuevo)

                anio_nuevo = input("Ingrese el nuevo año del disco: ")
                disco.pop(1)
                disco.insert(1, anio_nuevo)

                genero_nuevo = input("Ingrese el nuevo género del disco (opcional): ")
                disco.pop(3)
                disco.insert(3, genero_nuevo)

                precio_nuevo = input("Ingrese el nuevo precio del disco (opcional): ")
                if precio_nuevo == '':
                    precio_nuevo = None
                disco.pop(4)
                disco.insert(4, precio_nuevo)

                imagen_cara_nueva = input("Ingrese el nuevo nombre del archivo de la imagen de la cara (ej. portada.jpg): ")
                imagen_contra_cara_nueva = input("Ingrese el nuevo nombre del archivo de la imagen de la contracara (ej. contraportada.jpg): ")
                imagen_portada_nueva = (imagen_cara_nueva, imagen_contra_cara_nueva)
                disco.pop(5)
                disco.insert(5, imagen_portada_nueva)

                disco[6].clear()
                while True:
                    cancion_numero = input("Ingrese el número de la canción para el lado A (o 'fin' para terminar): ")
                    if cancion_numero.lower() == 'fin':
                        break
                    cancion_nombre = input("Ingrese el nombre de la canción: ")
                    disco[6].append((cancion_numero, cancion_nombre))

                disco[7].clear()
                while True:
                    cancion_numero = input("Ingrese el número de la canción para el lado B (o 'fin' para terminar): ")
                    if cancion_numero.lower() == 'fin':
                        break
                    cancion_nombre = input("Ingrese el nombre de la canción: ")
                    disco[7].append((cancion_numero, cancion_nombre))

                print("Disco modificado exitosamente")
            else:
                print("No se realizaron cambios en el disco")
            break
    else:
        print("No se encontró ningún disco con ese título.")