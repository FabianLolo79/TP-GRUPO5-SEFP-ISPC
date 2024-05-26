ALGORITMO ColeccionVinilos
    DEFINIR titulo, artista, año COMO CADENA
	DIMENSION collecion_vinilos[100]
	
    i <- 1
    REPETIR
        ESCRIBIR "Ingrese el título del disco:"
        LEER titulo
		
        ESCRIBIR "Ingrese el nombre del artista:"
        LEER artista
		
        ESCRIBIR "Ingrese el año de lanzamiento:"
        LEER año
		
        collecion_vinilos[i] <- "Título: " + titulo + ", Artista: " + artista + ", Año: " + año
        i <- i + 1
		
        ESCRIBIR "¿Desea agregar otro disco? (S/N):"
        LEER respuesta
    HASTA QUE respuesta = "N" O respuesta = "n"
	
    PARA j DESDE 1 HASTA i - 1
        ESCRIBIR collecion_vinilos[j]
    FIN PARA
	
FIN ALGORITMO