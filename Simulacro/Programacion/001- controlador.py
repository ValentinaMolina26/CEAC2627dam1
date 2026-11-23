import mysql.connector

# Conectar con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="simulacrosocialhub",
    password="Simulacrosocialhub1$",
    database="socialhub20261123"
)

# Crear cursor
cursor = conexion.cursor()

# Consultar todas las publicaciones
cursor.execute("SELECT * FROM publicaciones")

# Recuperar los resultados
publicaciones = cursor.fetchall()

# Mostrar los resultados por consola
for publicacion in publicaciones:
    print(publicacion)

# Cerrar cursor y conexión
cursor.close()
conexion.close()

