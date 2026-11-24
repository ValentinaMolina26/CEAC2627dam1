from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import requests

app = Flask(__name__, template_folder="templates")


# conexion a mysql
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

    cursor.execute("SELECT * FROM peliculas")
    peliculas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("videoteca.html", peliculas=peliculas)


# segundo endpoint
@app.route("/nueva_pelicula", methods=["GET", "POST"])
def nueva_pelicula():

    if request.method == "POST":

        titulo = request.form["titulo"]
        titulo_original = request.form["titulo_original"]
        director = request.form["director"]
        genero = request.form["genero"]
        sinopsis = request.form["sinopsis"]
        anio_estreno = request.form["anio_estreno"]
        fecha_estreno = request.form["fecha_estreno"]
        duracion_minutos = request.form["duracion_minutos"]
        pais = request.form["pais"]
        idioma_original = request.form["idioma_original"]
        clasificacion_edades = request.form["clasificacion_edades"]
        presupuesto = request.form["presupuesto"]
        recaudacion = request.form["recaudacion"]
        valoracion_media = request.form["valoracion_media"]
        numero_valoraciones = request.form["numero_valoraciones"]
        numero_visualizaciones = request.form["numero_visualizaciones"]
        disponible = request.form["disponible"]
        vista = request.form["vista"]
        favorita = request.form["favorita"]
        imagen_portada = request.form["imagen_portada"]
        url_trailer = request.form["url_trailer"]
        precio_alquiler = request.form["precio_alquiler"]
        precio_compra = request.form["precio_compra"]
        formato = request.form["formato"]
        subtitulos_disponibles = request.form["subtitulos_disponibles"]

        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO peliculas (
            titulo, titulo_original, director, genero, sinopsis,
            anio_estreno, fecha_estreno, duracion_minutos, pais,
            idioma_original, clasificacion_edades, presupuesto,
            recaudacion, valoracion_media, numero_valoraciones,
            numero_visualizaciones, disponible, vista, favorita,
            imagen_portada, url_trailer, precio_alquiler,
            precio_compra, formato, subtitulos_disponibles
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s)
        """

        valores = (
            titulo, titulo_original, director, genero, sinopsis,
            anio_estreno, fecha_estreno, duracion_minutos, pais,
            idioma_original, clasificacion_edades, presupuesto,
            recaudacion, valoracion_media, numero_valoraciones,
            numero_visualizaciones, disponible, vista, favorita,
            imagen_portada, url_trailer, precio_alquiler,
            precio_compra, formato, subtitulos_disponibles
        )

        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("inicio"))

    return render_template("formulario.html")


# tercer endpoint
@app.route("/consulta_ia", methods=["GET", "POST"])
def consulta_ia():

    if request.method == "POST":

        peticion = request.form["peticion"]

        prompt = f"""
        Convierte la petición en una consulta SQL SELECT.

        La tabla se llama peliculas.

        Sus columnas son:
        titulo, titulo_original, director, genero, sinopsis,
        anio_estreno, fecha_estreno, duracion_minutos, pais,
        idioma_original, clasificacion_edades, presupuesto,
        recaudacion, valoracion_media, numero_valoraciones,
        numero_visualizaciones, disponible, vista, favorita,
        imagen_portada, url_trailer, precio_alquiler,
        precio_compra, formato, subtitulos_disponibles.

        IMPORTANTE:
        - Utiliza solamente columnas de esta lista.
        - Para buscar películas de animación utiliza la columna genero.
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
        peliculas = cursor.fetchall()

        cursor.close()
        conexion.close()

        return render_template(
            "peticion.html",
            peliculas=peliculas
        )

    return render_template("peticion.html")


if __name__ == "__main__":
    app.run(debug=True)

