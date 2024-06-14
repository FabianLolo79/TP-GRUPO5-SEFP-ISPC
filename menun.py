# Diccionario para almacenar la discografía

discografia = {}

def menu():
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

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_nuevo_disco()
        elif opcion == "2":
            modificar_disco()
        elif opcion == "3":
            eliminar_disco()
        elif opcion == "4":
            mostrar_discografia()
        elif opcion == "5":
            buscar_disco_por_titulo()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción incorrecta. Por favor, ingrese una opción válida.")

def agregar_nuevo_disco():
    
    print("=" * 27)
    print("Opción 1 elegida - Agregar nuevo disco")
    print("=" * 27, "\n")
    
    nombre_artista = input("Ingrese el nombre del artista: ").capitalize()
    apellido_artista = input("Ingrese el apellido del artista: ").capitalize()
    artista = f"{nombre_artista} {apellido_artista}"
    print(type(artista))

    titulo = input("Ingrese el título del disco: ").title()
    print(titulo)
    anio = input("Ingrese el año del disco: ")
    genero = input("Ingrese el género del disco (opcional): ")
    precio = input("Ingrese el precio del disco (opcional): ")
    if precio == '':
        precio = None

    imagen_cara = input("Ingrese el nombre del archivo de la imagen de la cara (ej. portada.jpg): ")
    imagen_contra_cara = input("Ingrese el nombre del archivo de la imagen de la contracara (ej. contraportada.jpg): ")
    imagen_portada = (imagen_cara, imagen_contra_cara)

    disco = [titulo, anio, artista, genero, precio, imagen_portada]

    while True:
        cancion_numero = input("Ingrese el número de la canción para el lado A (o 'fin' para terminar): ")
        if cancion_numero.lower() == 'fin':
            break
        cancion_nombre = input("Ingrese el nombre de la canción: ")
        disco.agregar_cancion_lado_a(cancion_numero, cancion_nombre)

    while True:
        cancion_numero = input("Ingrese el número de la canción para el lado B (o 'fin' para terminar): ")
        if cancion_numero.lower() == 'fin':
            break
        cancion_nombre = input("Ingrese el nombre de la canción: ")
        disco.agregar_cancion_lado_b(cancion_numero, cancion_nombre)

    discografia[titulo] = disco
    print("Disco agregado exitosamente")
    
def modificar_disco():
    print("=" * 27)
    print("Opción 2 elegida - Modificar disco")
    print("=" * 27, "\n")
    
    titulo_buscar = input("Ingrese el título del disco que desea modificar: ").casefold()
    
    for titulo, disco in discografia.items():
        if titulo_buscar == titulo.casefold():
            print("Datos actuales del disco:")
            print(disco)

            opcion_modificar = input("¿Desea cambiar los campos del disco? (s/n): ")
            if opcion_modificar.lower() == "s":
                nombre_artista = input("Ingrese el nuevo nombre del artista: ")
                apellido_artista = input("Ingrese el nuevo apellido del artista: ")
                artista = f"{nombre_artista} {apellido_artista}"
                disco[2] = artista

                titulo_nuevo = input("Ingrese el nuevo título del disco: ")
                disco[0] = titulo_nuevo

                anio_nuevo = input("Ingrese el nuevo año del disco: ")
                disco[1] = anio_nuevo

                genero_nuevo = input("Ingrese el nuevo género del disco (opcional): ")
                disco[3] = genero_nuevo

                precio_nuevo = input("Ingrese el nuevo precio del disco (opcional): ")
                if precio_nuevo == '':
                    precio_nuevo = None
                disco[4] = precio_nuevo

                imagen_cara_nueva = input("Ingrese el nuevo nombre del archivo de la imagen de la cara (ej. portada.jpg): ")
                imagen_contra_cara_nueva = input("Ingrese el nuevo nombre del archivo de la imagen de la contracara (ej. contraportada.jpg): ")
                imagen_portada_nueva = (imagen_cara_nueva, imagen_contra_cara_nueva)
                disco[5] = imagen_portada_nueva

                print("Disco modificado exitosamente.")
            else:
                print("No se realizó ninguna modificación.")
            return
    print("No se encontró ningún disco con ese título.")


def eliminar_disco():
    print("=" * 27)
    print("Opción 3 elegida - Eliminar disco")
    print("=" * 27, "\n")
    
    titulo_buscar = input("Ingrese el título del disco a eliminar: ").casefold()
    
    for titulo, disco in list(discografia.items()):
        if titulo_buscar == titulo.casefold():
            del discografia[titulo]
            print("Disco eliminado exitosamente.")
            return
    print("No se encontró ningún disco con ese título.")


def mostrar_discografia():
    
    print("=" * 27)
    print("Opción 4 elegida - Mostrar discografía")
    print("=" * 27, "\n")
    
    if discografia:
        for titulo, disco in discografia.items():
            print(f"** Disco: {titulo} **")
            print(f"Artista: {disco[2]}")
            print(f"Año: {disco[1]}")
            print(f"Género: {disco[3]}")
            print(f"Precio: {disco[4]}")
            print(f"Imagen de portada: {disco[5][0]} y {disco[5][1]}")
            print("")  # Salto de línea para separar los discos
        print("Fin de la discografía.")
    else:
        print("La discografía está vacía.")
    

    
def buscar_disco_por_titulo():
    print("=" * 27)
    print("Opción 5 elegida - Buscar disco por título")
    print("=" * 27, "\n")
    
    titulo_buscar = input("Ingrese el título del disco a buscar: ")
    
    for titulo, disco in discografia.items():
        if titulo_buscar.casefold() == titulo.casefold():
            print(f"** Disco: {titulo} **")
            print(f"Artista: {disco[2]}")
            print(f"Año: {disco[1]}")
            print(f"Género: {disco[3]}")
            print(f"Precio: {disco[4]}")
            print(f"Imagen de portada: {disco[5][0]} y {disco[5][1]}")
            return
    print("No se encontró ningún disco con ese título.")

