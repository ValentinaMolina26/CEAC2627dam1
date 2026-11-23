from flask import Flask, render_template, request, redirect
import mysql.connector
import requests

app = Flask(__name__)

# Funcion para conectar con MySQL
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="simulacrosocialhub",
        password="Simulacrosocialhub1$",
        database="socialhub20261123"
    )
    return conexion


# Ruta principal
@app.route("/")
def inicio():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM publicaciones")
    publicaciones = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("index.html", publicaciones=publicaciones)


# Ruta para mostrar el formulario
@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


# Ruta para insertar una nueva publicacion
@app.route("/formulario", methods=["POST"])
def insertar():

    nombre = request.form["nombre"]
    plataforma = request.form["plataforma"]
    tipo_contenido = request.form["tipo_contenido"]
    descripcion = request.form["descripcion"]
    fecha_publicacion = request.form["fecha_publicacion"]
    estado = request.form["estado"]
    presupuesto = request.form["presupuesto"]
    enlace = request.form["enlace"]

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """INSERT INTO publicaciones
    (nombre, plataforma, tipo_contenido, descripcion,
    fecha_publicacion, estado, presupuesto, enlace)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    valores = (nombre, plataforma, tipo_contenido,
               descripcion, fecha_publicacion,
               estado, presupuesto, enlace)

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect("/")


# Tercera ruta: consultar con IA Ollama
@app.route("/peticion", methods=["GET", "POST"])
def consulta_ia():

    if request.method == "POST":

        pregunta = request.form["pregunta"]

        prompt = f"""
        Convierte esta pregunta en una consulta SQL de MySQL.
        La tabla se llama publicaciones.
        Sus campos son id, nombre, plataforma, tipo_contenido,
        descripcion, fecha_publicacion, estado, presupuesto y enlace.
        Devuelve solamente el SELECT.

        Pregunta: {pregunta}
        """

        respuesta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:7b",
                "prompt": prompt,
                "stream": False
            }
        )

        sql = respuesta.json()["response"].strip()
        sql = sql.replace("```sql", "").replace("```", "").strip()

        if not sql.upper().startswith("SELECT"):
            return "La IA no ha generado una consulta SELECT valida."

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(sql)
        resultados = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template(
            "peticion.html",
            resultados=resultados
        )

    return render_template("peticion.html")


if __name__ == "__main__":
    app.run(debug=True)

