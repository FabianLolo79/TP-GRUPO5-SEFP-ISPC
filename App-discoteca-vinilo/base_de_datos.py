import mysql.connector 

HOST = "localhost"
USER = "root"
PASSWORD = "45320145613LOko."
BD = "colecciondevinilos"

# Conectarse a la base de datos
cnx = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=BD
)

# Crear un cursor
cursor = cnx.cursor()

def cerrarConexion():
    cursor.close()
    cnx.close()
