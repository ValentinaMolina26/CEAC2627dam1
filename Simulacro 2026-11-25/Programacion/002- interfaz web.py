from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

#conexion a mysql
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="videojuegos20261125",
        password="CEAC2627dam123$",
        database="videojuegos20261125"
    )
    return conexion
  
#primer endpoint
@app.route("/")
def inicio():

  conexion = conectar()
  cursor = conexion.cursor(dictionary=True)
  
  #consultamos los videojuegos
  cursor.execute("SELECT * FROM videojuegos")
  videojuegos = cursor.fetchall()
                       
  cursor.close()
  conexion.close()
  
  #enviamos datos al html
  return render_template("videojuegos.html", videojuegos=videojuegos)
  
if __name__ == "__main__":
  app.run(debug=True)
