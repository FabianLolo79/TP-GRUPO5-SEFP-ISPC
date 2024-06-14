# Diccionario para almacenar la discografía
import base_de_datos as bd
#discografia = {}

""" La función menu() muestra un menú con las opciones disponibles y pide al usuario que ingrese una opción.
    Luego, dependiendo de la opción seleccionada, llama a la función correspondiente
"""

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
            bd.cerrarConexion()
            break
        else:
            # Opción inválida
            print("Opción incorrecta. Por favor, ingrese una opción válida.")


""" La función agregar_nuevo_disco() pide al usuario que ingrese la información del disco, como el nombre del artista, el título del disco,
    el año, el género, el precio, la imagen de la cara y la contracara. Luego, agrega el disco a la base de datos y pide al usuario que ingrese 
    las canciones del lado A y B. Finalmente, agrega las canciones a la base de datos y confirma que el disco se agregó exitosamente.
"""
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

    canciones = []
    while True:
        cancion_nombre = input("Ingrese el nombre de la canción para el lado A (o 'fin' para terminar): ")
        if cancion_nombre.lower() == 'fin':
            break
        canciones.append([cancion_nombre, 'A'])
    
    while True:
        cancion_nombre = input("Ingrese el nombre de la canción para el lado B (o 'fin' para terminar): ")
        if cancion_nombre.lower() == 'fin':
            break
        canciones.append([cancion_nombre, 'B'])

    # Agregar el disco a la base de datos
    bd.cursor.execute("INSERT INTO imagen_portada (imagen_cara, imagen_contraCara) VALUES (%s, %s)", (imagen_cara, imagen_contra_cara))
    idImagen_portada = bd.cursor.lastrowid

    bd.cursor.execute("INSERT INTO artista (nombre, apellido) VALUES (%s, %s)", (nombre_artista, apellido_artista))
    idArtista = bd.cursor.lastrowid

    bd.cursor.execute("INSERT INTO discovinilo (titulo, genero, precio, anio, idArtista, idImagen_portada) VALUES (%s, %s, %s, %s, %s, %s)", (titulo, genero, precio, anio, idArtista, idImagen_portada))
    idDiscoVinilo = bd.cursor.lastrowid

    bd.cursor.executemany("INSERT INTO canciones (nombre, lado, idDiscoVinilo) VALUES (%s, %s, %s)", [(cancion[0], cancion[1], idDiscoVinilo) for cancion in canciones])

    bd.cnx.commit()

    print("Disco agregado exitosamente")


""" La función modificar_disco() pide al usuario que ingrese el título del disco que desea modificar.
    Luego, busca el disco en la base de datos y pide al usuario que ingrese los nuevos datos del disco.
    Finalmente, actualiza la información del disco en la base de datos y confirma que el disco se modificó exitosamente.
"""

def modificar_disco():
    # Modificar un disco existente en la discografía
    print("=" * 27)
    print("Opción 2 elegida - Modificar disco")
    print("=" * 27, "\n")

    # Pedir al usuario que ingrese el título del disco que desea modificar
    titulo_buscar = input("Ingrese el titulo del disco que desea buscar: \n")

    resultados = buscar_disco_por_titulo(titulo_buscar)

    cambiar = input("Desea modificar los cambios? s/n ").lower()
    if cambiar == "s":
        nuevo_titulo = input("Ingrese el nuevo título del disco o pulse enter si desea dejar el actual: ")
        if nuevo_titulo:
            titulo_actual = nuevo_titulo
        else:
            titulo_actual = resultados[0][0]

        nuevo_nombre = input("Ingrese el nuevo nombre de artista o pulse enter si desea dejar el actual: ")
        if nuevo_nombre:
            nombre_actual = nuevo_nombre
        else:
            nombre_actual = resultados[0][1]
            
        apellido_nuevo = input("Ingrese el nuevo nombre de artista o pulse enter si desea dejar el actual: ")
        if apellido_nuevo:
            apellido_actual = apellido_nuevo
        else:
            apellido_actual = resultados[0][1]

        nuevo_anio = input("Ingrese el nuevo año o pulse enter si desea dejar el actual: ")
        if nuevo_anio:
            anio_actual = nuevo_anio
        else:
            anio_actual = resultados[0][3]

        nuevo_genero = input("Ingrese el nuevo género o pulse enter si desea dejar el actual: ")
        if nuevo_genero:
            genero_actual = nuevo_genero
        else:
            genero_actual = resultados[0][4]

        nuevo_precio = input("Ingrese el nuevo precio o pulse enter si desea dejar el actual: ")
        if nuevo_precio:
            precio_actual = nuevo_precio
        else:
            precio_actual = resultados[0][5]

        nuevo_imagen_cara = input("Ingrese la nueva imagen de la cara o pulse enter si desea dejar la actual: ")
        if nuevo_imagen_cara:
            imagen_cara_actual = nuevo_imagen_cara
        else:
            imagen_cara_actual = resultados[0][6]

        nuevo_imagen_contraCara = input("Ingrese lanueva imagen de la contracara o pulse enter si desea dejar la actual: ")
        if nuevo_imagen_contraCara:
            imagen_contraCara_actual = nuevo_imagen_contraCara
        else:
            imagen_contraCara_actual = resultados[0][7]

        bd.cursor.execute("UPDATE imagen_portada SET imagen_cara = %s, imagen_contraCara = %s WHERE idImagen_portada = %s", (imagen_cara_actual, imagen_contraCara_actual, resultados[0][12]))
        bd.cursor.execute("UPDATE artista SET nombre = %s, apellido = %s WHERE idArtista = %s", (nombre_actual, apellido_actual, resultados[0][10]))
        bd.cursor.execute("UPDATE discovinilo SET titulo = %s, anio = %s, genero = %s, precio = %s WHERE idDiscoVinilo = %s", (titulo_actual, anio_actual, genero_actual, precio_actual, resultados[0][11]))
        bd.cnx.commit()

        print("Disco modificado exitosamente")

    else:
        print("Disco no encontrado")
        
        
""" La función eliminar_disco() pide al usuario que ingrese el título del disco que desea eliminar.
    Luego, busca el disco en la base de datos y pide al usuario que confirme si desea eliminar el disco.
    Si el usuario confirma, elimina el disco de la base de datos y confirma que el disco se eliminó exitosamente.
"""

def eliminar_disco():
    # Eliminar un disco de la discografía
    print("=" * 27)
    print("Opción 3 elegida - Eliminar disco")
    print("=" * 27, "\n")
    
    titulo_buscar = input("Ingrese el titulo del disco que desea buscar: \n")
    resultados = buscar_disco_por_titulo(titulo_buscar)

    cambiar = input("Desea eliminar este disco? s/n ").lower()
    if cambiar == "s":
        bd.cursor.execute("DELETE FROM canciones WHERE idDiscoVinilo = %s", (resultados[0][11],))
        bd.cursor.execute("DELETE FROM discovinilo WHERE idDiscoVinilo = %s", (resultados[0][11],))
        bd.cursor.execute("SELECT COUNT(*) FROM discovinilo WHERE idArtista = %s", (resultados[0][10],))
        count = bd.cursor.fetchone()[0]
        if count == 0:
            bd.cursor.execute("DELETE FROM artista WHERE idArtista = %s", (resultados[0][10],))
            bd.cnx.commit()
            print("Disco y artista eliminados correctamente")
        
        
    else:
        print("Volviendo al menu...")


""" La función mostrar_discografia() muestra la discografía completa, incluyendo el título, el artista, el año,
    el género, el precio, la imagen de la cara y la contracara, y las canciones del lado A y B de cada disco.
"""

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
            ip.imagen_contraCara,
            c.nombre as cancion, 
            c.lado,
            a.idArtista,
            dv.idDiscoVinilo
        FROM 
            discovinilo dv
        INNER JOIN 
            artista a ON dv.idArtista = a.idArtista
        INNER JOIN 
            imagen_portada ip ON dv.idImagen_portada = ip.idImagen_portada
        LEFT JOIN 
            canciones c ON dv.idDiscoVinilo = c.idDiscoVinilo
        WHERE 
            dv.idArtista IS NOT NULL AND 
            dv.idImagen_portada IS NOT NULL
        ORDER BY 
            dv.titulo, c.lado, c.nombre
        """)
    resultados = bd.cursor.fetchall()
    disco_actual = None
    canciones_lado_a = []
    canciones_lado_b = []
    for resultado in resultados:
        if resultado[0]!= disco_actual:
            if disco_actual is not None:
                print("Lado A:")
                for cancion in canciones_lado_a:
                    print(f"  {cancion}")
                print("Lado B:")
                for cancion in canciones_lado_b:
                    print(f"  {cancion}")
                print()
            print(f"** Disco: {resultado[0]} **")
            print(f"Artista: {resultado[1]} {resultado[2]}")
            print(f"Año: {resultado[3]}")
            print(f"Género: {resultado[4]}")
            print(f"Precio: {resultado[5]}")
            print(f"Imagen de la cara: {resultado[6]}")
            print(f"Imagen de la contracara: {resultado[7]}")
            disco_actual = resultado[0]
            canciones_lado_a = []
            canciones_lado_b = []
        if resultado[8] is not None:
            if resultado[9] == 'A':
                canciones_lado_a.append(resultado[8])
            else:
                canciones_lado_b.append(resultado[8])
    if disco_actual is not None:
        print("Lado A:")
        for cancion in canciones_lado_a:
            print(f"  {cancion}")
        print("Lado B:")
        for cancion in canciones_lado_b:
            print(f"  {cancion}")
        print()


""" La función buscar_disco_por_titulo() pide al usuario que ingrese el título del disco que desea buscar.
    Luego, busca el disco en la base de datos y muestra la información del disco, incluyendo el artista,
    el año, el género, el precio, la imagen de la cara y la contracara, y las canciones del lado A y B. 
"""

def buscar_disco_por_titulo(titulo):
    # Buscar un disco por título
    print("=" * 27)
    print("Opción 5 elegida - Buscar disco por título")
    print("=" * 27, "\n")

    # Pedir al usuario que ingrese el título del disco a buscar
        
    bd.cursor.execute("""
        SELECT 
            dv.titulo, 
            a.nombre, 
            a.apellido, 
            dv.anio, 
            dv.genero, 
            dv.precio, 
            ip.imagen_cara, 
            ip.imagen_contraCara,
            c.nombre as cancion, 
            c.lado,
            a.idArtista,
            dv.iddiscovinilo,
            ip.idImagen_portada
        FROM 
            discovinilo dv
        INNER JOIN 
            artista a ON dv.idArtista = a.idArtista
        INNER JOIN 
            imagen_portada ip ON dv.idImagen_portada = ip.idImagen_portada
        LEFT JOIN 
            canciones c ON dv.idDiscoVinilo = c.idDiscoVinilo
        WHERE 
            dv.titulo = %s AND 
            dv.idArtista IS NOT NULL AND 
            dv.idImagen_portada IS NOT NULL
        ORDER BY 
            dv.titulo, c.lado, c.nombre
        """, (titulo,))
    resultados = bd.cursor.fetchall()
    if resultados:
        disco_actual = resultados[0][0]
        canciones_lado_a = []
        canciones_lado_b = []
        for resultado in resultados:
            if resultado[8] is not None:
                if resultado[9] == 'A':
                    canciones_lado_a.append(resultado[8])
                else:
                    canciones_lado_b.append(resultado[8])
        print(f"** Disco: {disco_actual} **")
        print(f"Artista: {resultados[0][1]} {resultados[0][2]}")
        print(f"Año: {resultados[0][3]}")
        print(f"Género: {resultados[0][4]}")
        print(f"Precio: {resultados[0][5]}")
        print(f"Imagen de la cara: {resultados[0][6]}")
        print(f"Imagen de la contracara: {resultados[0][7]}")
        print("Lado A:")
        for cancion in canciones_lado_a:
            print(f"  {cancion}")
        print("Lado B:")
        for cancion in canciones_lado_b:
            print(f"  {cancion}")
        print()
        return resultados
    else:
        print("No se encontró el disco con ese título.")