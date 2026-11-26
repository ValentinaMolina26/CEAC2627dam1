from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

#conexion con mysql
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="vehículos20261125",
        password="Ceac2627DAM123$",
        database="vehículos20261125"
    )
    return conexion

#primer endpoint
@app.route("/")
def inicio():

  conexion = conectar()
  cursor = conexion.cursor(dictionary=True)
  
  #consultamos los vehiculos
  cursor.execute("SELECT * FROM vehiculos")
  vehiculos = cursor.fetchall()
                       
  cursor.close()
  conexion.close()
  
  #enviamos datos al html
  return render_template("vehiculos.html", vehiculos=vehiculos)
  
if __name__ == "__main__":
  app.run(debug=True)

