import mysql.connector

def obtener_medicos():

    conexion = mysql.connector.connect(
        host="localhost",
        user="examendamceac2026",
        password="CEACExamenDAM123$",
        database="examendamceac2627"
    )

    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM medicos")

    medicos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return medicos

