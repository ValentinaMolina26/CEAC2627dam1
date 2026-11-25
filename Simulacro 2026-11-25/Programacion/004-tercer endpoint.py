from flask import Flask, render_template, request, redirect
import mysql.connector
import requests

app = Flask(__name__)

# conexion a mysql
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="videojuegos20261125",
        password="CEAC2627dam123$",
        database="videojuegos20261125"
    )
    return conexion


# primer endpoint
@app.route("/")
def inicio():

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    # consultamos los videojuegos
    cursor.execute("SELECT * FROM videojuegos")
    videojuegos = cursor.fetchall()

    cursor.close()
    conexion.close()

    # enviamos datos al html
    return render_template("videojuegos.html", videojuegos=videojuegos)


# segundo endpoint
@app.route("/formulario", methods=["GET", "POST"])
def nuevo_videojuego():

    if request.method == "POST":

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO videojuegos (
                titulo, desarrollador, distribuidor, genero, descripcion, anio_lanzamiento,
                fecha_lanzamiento, plataforma, pais, idioma, clasificacion_edades, presupuesto,
                ingresos, valoracion_media, numero_valoraciones, unidades_vendidas, disponible,
                multijugador, favorito, imagen_portada, url_trailer, precio_original,
                precio_rebajado, espacio_requerido, compras_integradas
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s
            )
        """, (
            request.form["titulo"],
            request.form["desarrollador"],
            request.form["distribuidor"],
            request.form["genero"],
            request.form["descripcion"],
            request.form["anio_lanzamiento"],
            request.form["fecha_lanzamiento"],
            request.form["plataforma"],
            request.form["pais"],
            request.form["idioma"],
            request.form["clasificacion_edades"],
            request.form["presupuesto"],
            request.form["ingresos"],
            request.form["valoracion_media"],
            request.form["numero_valoraciones"],
            request.form["unidades_vendidas"],
            request.form["disponible"],
            request.form["multijugador"],
            request.form["favorito"],
            request.form["imagen_portada"],
            request.form["url_trailer"],
            request.form["precio_original"],
            request.form["precio_rebajado"],
            request.form["espacio_requerido"],
            request.form["compras_integradas"]
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

        La tabla se llama videojuegos.

        Sus columnas son:
        titulo, desarrollador, distribuidor, genero, descripcion,
        anio_lanzamiento, fecha_lanzamiento, plataforma, pais,
        idioma, clasificacion_edades, presupuesto, ingresos,
        valoracion_media, numero_valoraciones, unidades_vendidas,
        disponible, multijugador, favorito, imagen_portada,
        url_trailer, precio_original, precio_rebajado,
        espacio_requerido, compras_integradas.

        IMPORTANTE:
        - Utiliza solamente columnas de esta lista.
        - Para buscar videojuegos de aventuras utiliza la columna genero.
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
        videojuegos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template(
            "peticion.html",
            videojuegos=videojuegos
        )

    return render_template("peticion.html")

if __name__ == "__main__":
    app.run(debug=True)

