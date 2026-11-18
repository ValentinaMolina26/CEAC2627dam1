# Importo Flask para la web y connector para MySQL
from flask import Flask, render_template, request
import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='caminodeida',
        password='CEACcamino_ida123$',
        database='caminodeida'
    )

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/procesa", methods=["POST"])
def procesa():
  ######################### MYSQL
 	# Creo un cursor para poder pedir cosas
  cursor = connection.cursor()

  # Ejecuto una petición sobre el cursor
  cursor.execute("""
        INSERT INTO clientes (nombre, apellidos, email)
        VALUES (%s, %s, %s);
    """, (
        request.form["nombre"],
        request.form["apellidos"],
        request.form["email"]
    ))
  connection.commit()
  return "ok yo te voy a procesar el formulario: "

@aplicacion.route("/procesa2", methods=["POST"])
def procesa2():
  ######################### MYSQL
 	# Creo un cursor para poder pedir cosas
  cursor = connection.cursor()

  # Ejecuto una petición sobre el cursor
  cursor.execute("""
        INSERT INTO direccion (ciudad, pais, codigo_postal)
        VALUES (%s, %s, %s);
    """, (
        request.form["ciudad"],
        request.form["pais"],
        request.form["codigo_postal"]
    ))    

  connection.commit()
  # Ahora atrapo los parametros
 
  return "ok yo te voy a procesar el formulario: "
  
if __name__ == "__main__":
  aplicacion.run()
