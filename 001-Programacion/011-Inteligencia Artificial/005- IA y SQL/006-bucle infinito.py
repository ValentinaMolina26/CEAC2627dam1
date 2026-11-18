import requests
import sqlite3
# Variables invariables ##################################
ruta = "http://localhost:11434/api/generate" 	# Defino la ruta 
modelo = "codellama:7b"												# Elijo un modelo
conexion = sqlite3.connect("empresa.db")			# Abro la base de datos
cursor = conexion.cursor()										# Creo un cursor
while True:																		# Entro en un bucle infinito
  preguntausuario = input("Dime qué es lo que quieres: ")
  pregunta = """ 
  	Eres un generador de SQL - solo puedes lanzar SQL sin fences
    Dame el SQL para:
    -"""+preguntausuario+"""
    -La estructura de la tabla es esta: 
        CREATE TABLE "clientes" (
        "id"	INTEGER,
        "nombre"	TEXT,
        "apellidos"	TEXT,
        "email"	TEXT,
        "telefono"	TEXT,
        "ciudad"	TEXT,
        "provincia"	TEXT,
        "direccionpostal"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
      );
      - Dame solo código SQL - no pongas comentarios
      - no me des otra cosa que no sea código SQL - no me comentes el resultado - Importante!!!!!
      - En la respuesta incluye solo SQL - no incluyas cualquier otro tipo de texto, datos, explicación, anotaciones, etcétera
      - Elimina los fences markdown opentick

  """									# Establezco una pregunta
  flujo = False																	# Elijo stream
  r = requests.post(ruta, json={
      "model":modelo,
      "prompt": pregunta,
      "stream": flujo
  })																						# Hago una petición
  print(r.json()["response"])										# Imprime la respuesta

  cursor.execute(r.json()["response"].replace("`", ""))	# Ejecuto la peticion
  filas = cursor.fetchall()											# Recupero el resultado

  for fila in filas:														# PAra cada fila
      print(fila)																# Imprime la fila


conexion.close()
