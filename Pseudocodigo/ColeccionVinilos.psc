ALGORITMO ColeccionVinilos
    DEFINIR titulo, artista, a�o COMO CADENA
	DIMENSION collecion_vinilos[100]
	
    i <- 1
    REPETIR
        ESCRIBIR "Ingrese el t�tulo del disco:"
        LEER titulo
		
        ESCRIBIR "Ingrese el nombre del artista:"
        LEER artista
		
        ESCRIBIR "Ingrese el a�o de lanzamiento:"
        LEER a�o
		
        collecion_vinilos[i] <- "T�tulo: " + titulo + ", Artista: " + artista + ", A�o: " + a�o
        i <- i + 1
		
        ESCRIBIR "�Desea agregar otro disco? (S/N):"
        LEER respuesta
    HASTA QUE respuesta = "N" O respuesta = "n"
	
    PARA j DESDE 1 HASTA i - 1
        ESCRIBIR collecion_vinilos[j]
    FIN PARA
	
FIN ALGORITMO