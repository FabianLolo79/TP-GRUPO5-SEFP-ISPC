# Diccionario para almacenar la discografía
import base_de_datos as bd
discografia = {}

def menu():
    # Loop infinito para mostrar el menú y procesar las opciones
    while True:
        # Pedir al usuario que ingrese una opción
        print("=" * 27)   
        print("MEMÚ DE OPCIONES: \n") 
        print("1. Agregar nuevo vinilo") 
        print("2. Modificar vinilo")
        print("3. Eliminar vinilo")
        print("4. Mostrar discografia")
        print("5. Buscar vinilo por titulo")
        print("6. Salir \n")
        print("=" * 27)

        opcion = input("Ingrese una opción: \n")

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
        cancion_nombre = input("Ingrese el nombre de la canción para el lado A (o 'fin' para terminar): ")
        if cancion_nombre.lower() == 'fin':
            break
        disco[6].append(cancion_nombre)

    # Pedir al usuario que ingrese las canciones del lado B
    while True:
        #cancion_numero = input("Ingrese el número de la canción para el lado B (o 'fin' para terminar): ")
        cancion_nombre = input("Ingrese el nombre de la canción para el lado B (o 'fin' para terminar): ")
        if cancion_nombre.lower() == 'fin':
            break
        disco[7].append(cancion_nombre)

    # Agregar el disco a la base de datos
    bd.cursor.execute("INSERT INTO imagen_portada (imagen_cara, imagen_contraCara) VALUES (%s, %s)", (imagen_cara, imagen_contra_cara))
    idImagen_portada = bd.cursor.lastrowid

    bd.cursor.execute("INSERT INTO artista (nombre, apellido) VALUES (%s, %s)", (nombre_artista, apellido_artista))
    idArtista = bd.cursor.lastrowid

    bd.cursor.execute("INSERT INTO discovinilo (titulo, genero, precio, anio, idArtista, idImagen_portada) VALUES (%s, %s, %s, %s, %s, %s)", (titulo, genero, precio, anio, idArtista, idImagen_portada))
    idDiscoVinilo = bd.cursor.lastrowid

    for cancion in disco[6]:
        bd.cursor.execute("INSERT INTO canciones (nombre, lado, idDiscoVinilo) VALUES (%s, 'A', %s)", (cancion, idDiscoVinilo))

    for cancion in disco[7]:
        bd.cursor.execute("INSERT INTO canciones (nombre, lado, idDiscoVinilo) VALUES (%s, 'B', %s)", (cancion, idDiscoVinilo))

    bd.cnx.commit()
    bd.cerrarConexion

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

                # Modificar los campos del disco
                bd.cursor.execute("UPDATE discovinilo SET titulo = %s, anio = %s, artista = %s, genero = %s, precio = %s WHERE titulo = %s", (titulo_nuevo, anio_nuevo, artista, genero_nuevo, precio_nuevo, titulo_buscar))
                bd.cnx.commit()
                print("Disco modificado exitosamente")
                
            else:
                print("No se realizaron cambios en el disco")
            break
    else:
        print("No se encontró ningún disco con ese título.")
        

def eliminar_disco():
    # Eliminar un disco de la discografía
    print("=" * 27)
    print("Opción 3 elegida - Eliminar disco")
    print("=" * 27, "\n")
    
    # Pedir al usuario que ingrese el título del disco a eliminar
    titulo_buscar = input("Ingrese el título del disco que desea eliminar: ").casefold()
    
    # Buscar el disco en la discografía
    for titulo, disco in discografia.items():
        if titulo_buscar == titulo.casefold():
            # Eliminar el disco de la discografía
            del discografia[titulo]
            
           # Eliminar el disco de la base de datos
            bd.cursor.execute("DELETE FROM discovinilo WHERE titulo = %s", (titulo_buscar,))
            bd.cnx.commit()
            print("Disco eliminado exitosamente")
            
            break
    else:
        print("No se encontró ningún disco con ese título.")


def mostrar_discografia():
    # Mostrar la discografía completa
    print("=" * 27)
    print("Opción 4 elegida - Mostrar discografía")
    print("=" * 27, "\n")

    # Mostrar la discografía completa
    bd.cursor.execute("""
        SELECT 
            dv.titulo, 
            a.nombre, 
            a.apellido, 
            dv.anio, 
            dv.genero, 
            dv.precio, 
            ip.imagen_cara, 
            ip.imagen_contraCara
        FROM 
            discovinilo dv
        INNER JOIN 
            artista a ON dv.idArtista = a.idArtista
        INNER JOIN 
            imagen_portada ip ON dv.idImagen_portada = ip.idImagen_portada
        WHERE 
            dv.idArtista IS NOT NULL AND 
            dv.idImagen_portada IS NOT NULL
        """)
    resultados = bd.cursor.fetchall()
    for resultado in resultados:
        print(f"** Disco: {resultado[0]} **")
        print(f"Artista: {resultado[1]} {resultado[2]}")
        print(f"Año: {resultado[3]}")
        print(f"Género: {resultado[4]}")
        print(f"Precio: {resultado[5]}")
        print(f"Imagen de la cara: {resultado[6]}")
        print(f"Imagen de la contracara: {resultado[7]}")
        print()


def buscar_disco_por_titulo():
    # Buscar un disco por título
    print("=" * 27)
    print("Opción 5 elegida - Buscar disco por título")
    print("=" * 27, "\n")

    # Pedir al usuario que ingrese el título del disco a buscar
    titulo_buscar = input("Ingrese el título del disco a buscar: ").casefold()

    # Buscar el disco en la base de datos
    bd.cursor.execute("""
        SELECT 
            dv.titulo, 
            a.nombre, 
            a.apellido, 
            dv.anio, 
            dv.genero, 
            dv.precio, 
            ip.imagen_cara, 
            ip.imagen_contraCara
        FROM 
            discovinilo dv
        INNER JOIN 
            artista a ON dv.idArtista = a.idArtista
        INNER JOIN 
            imagen_portada ip ON dv.idImagen_portada = ip.idImagen_portada
        WHERE 
            dv.titulo = %s AND 
            dv.idArtista IS NOT NULL AND 
            dv.idImagen_portada IS NOT NULL
    """, (titulo_buscar,))
    resultado = bd.cursor.fetchone()
    if resultado:
        print(f"** Disco: {resultado[0]} **")
        print(f"Artista: {resultado[1]} {resultado[2]}")
        print(f"Año: {resultado[3]}")
        print(f"Género: {resultado[4]}")
        print(f"Precio: {resultado[5]}")
        print(f"Imagen de la cara: {resultado[6]}")
        print(f"Imagen de la contracara: {resultado[7]}")
    else:
        print("No se encontró ningún disco con ese título.")