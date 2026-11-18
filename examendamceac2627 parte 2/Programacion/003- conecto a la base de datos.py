from flask import Flask, render_template
import mysql.connector

aplicacion = Flask(__name__)

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


@aplicacion.route("/")
def inicio():

    medicos = obtener_medicos()

    return render_template("simulacro.html", medicos=medicos)


if __name__ == "__main__":
    aplicacion.run(debug=True)

