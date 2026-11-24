from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


# conexion a msql
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="videoteca20261124",
        password="CEAC2627DAm123$$",
        database="videoteca20261124"
    )
    return conexion


# primer endpoint
@app.route("/")
def inicio():

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    # consultar todas las peliculas
    cursor.execute("SELECT * FROM peliculas")
    peliculas = cursor.fetchall()

    cursor.close()
    conexion.close()

    # enviar los datos al HTML
    return render_template("videoteca.html", peliculas=peliculas)


if __name__ == "__main__":
    app.run(debug=True)
