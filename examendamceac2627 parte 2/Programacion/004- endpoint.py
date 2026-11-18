from flask import Flask, render_template, request, redirect
import mysql.connector

aplicacion = Flask(__name__)


# FUNCIÓN PARA OBTENER LOS MÉDICOS
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


# CAMINO DE VUELTA: MOSTRAR LOS MÉDICOS
@aplicacion.route("/")
def inicio():

    medicos = obtener_medicos()

    return render_template("simulacro.html", medicos=medicos)


# MOSTRAR EL FORMULARIO
@aplicacion.route("/formulario")
def formulario():

    return render_template("formulario.html")


# CAMINO DE IDA: INSERTAR UN MÉDICO
@aplicacion.route("/insertar", methods=["POST"])
def insertar():

    nombre = request.form["nombre"]
    apellidos = request.form["apellidos"]
    email = request.form["email"]
    especialidad = request.form["especialidad"]
    numero_de_colegiado = request.form["numero_de_colegiado"]
    activo = request.form["activo"]

    conexion = mysql.connector.connect(
        host="localhost",
        user="examendamceac2026",
        password="CEACExamenDAM123$",
        database="examendamceac2627"
    )

    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO medicos
        (nombre, apellidos, email, especialidad, numero_de_colegiado, activo)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, apellidos, email, especialidad,
          numero_de_colegiado, activo))

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect("/")


if __name__ == "__main__":
    aplicacion.run(debug=True)

