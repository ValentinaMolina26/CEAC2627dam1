from flask import Flask, render_template, request, redirect
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
  
# segundo endpoint
@app.route("/formulario", methods=["GET", "POST"])
def nuevo_vehiculo():

    if request.method == "POST":

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO vehiculos (
                marca, modelo, version, categoria, descripcion, anio_fabricacion, fecha_matriculacion, 
                matricula, pais, color, combustible, potencia, cilindrada, kilometraje, 
                numero_puertas, numero_plazas, consumo_medio, automatico, disponible, 
                segunda_mano, imagen, url_fabricante, precio_original, precio_venta, garantia_vigente
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s
            )
        """, (
            request.form["marca"],
            request.form["modelo"],
            request.form["version"],
            request.form["categoria"],
            request.form["descripcion"],
            request.form["anio_fabricacion"],
            request.form["fecha_matriculacion"],
            request.form["matricula"],
            request.form["pais"],
            request.form["color"],
            request.form["combustible"],
            request.form["potencia"],
            request.form["cilindrada"],
            request.form["kilometraje"],
            request.form["numero_puertas"],
            request.form["numero_plazas"],
            request.form["consumo_medio"],
            request.form["automatico"],
            request.form["disponible"],
            request.form["segunda_mano"],
            request.form["imagen"],
            request.form["url_fabricante"],
            request.form["precio_original"],
            request.form["precio_venta"],
            request.form["garantia_vigente"]
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

        return redirect("/")

    return render_template("formulario.html")


if __name__ == "__main__":
    app.run(debug=True)
