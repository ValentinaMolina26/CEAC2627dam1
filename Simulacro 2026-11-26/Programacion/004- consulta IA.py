from flask import Flask, render_template, request, redirect
import mysql.connector
import requests

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

# tercer endpoint
@app.route("/consulta", methods=["GET", "POST"])
def consulta_ia():

    if request.method == "POST":

        peticion = request.form["peticion"]

        prompt = f"""
        Convierte la petición en una consulta SQL SELECT.

        La tabla se llama vehiculos.

        Sus columnas son:
        marca, modelo, version, categoria, descripcion, anio_fabricacion,
        fecha_matriculacion, matricula, pais, color, combustible, potencia,
        cilindrada, kilometraje, numero_puertas, numero_plazas, consumo_medio,
        automatico, disponible, segunda_mano, imagen, url_fabricante,
        precio_original, precio_venta, garantia_vigente

        IMPORTANTE:
        - Utiliza solamente columnas de esta lista: marca, modelo, version,
          categoria, descripcion, anio_fabricacion, fecha_matriculacion,
          matricula, pais, color, combustible, potencia, cilindrada,
          kilometraje, numero_puertas, numero_plazas, consumo_medio,
          automatico, disponible, segunda_mano, imagen, url_fabricante,
          precio_original, precio_venta, garantia_vigente.
        - Para buscar vehículos de una categoría concreta utiliza la columna categoria.
        - Devuelve solamente una consulta SQL.
        - No incluyas explicaciones ni etiquetas markdown.

        Petición: {peticion}
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

        sql = sql.replace("```sql", "")
        sql = sql.replace("```", "")
        sql = sql.strip()

        sql = sql.rstrip(";").strip()

        print("CONSULTA SQL:")
        print(sql)

        if not sql.upper().startswith("SELECT") or ";" in sql:
            return render_template(
                "peticion.html",
                mensaje="La IA no ha generado una consulta válida"
            )

        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(sql)
        vehiculos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template(
            "peticion.html",
            vehiculos=vehiculos
        )

    return render_template("peticion.html")

if __name__ == "__main__":
    app.run(debug=True)    

