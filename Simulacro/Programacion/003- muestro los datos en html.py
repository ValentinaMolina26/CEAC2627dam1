
from flask import Flask, render_template
import mysql.connector

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

    # Consultar todas las publicaciones
    cursor.execute("SELECT * FROM publicaciones")
    publicaciones = cursor.fetchall()

    cursor.close()
    conexion.close()

    # Enviar los datos al HTML
    return render_template("index.html", publicaciones=publicaciones)


if __name__ == "__main__":
    app.run(debug=True)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
