import requests
import sqlite3

ruta = "http://localhost:11434/api/generate" 	# Defino la ruta 
modelo = "codellama:7b"												# Elijo un modelo
preguntausuario = input("Dime qué es lo que quieres: ")
pregunta = """ 
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
    - Elimina los fences markdown opentick
  
"""									# Establezco una pregunta
flujo = False																	# Elijo stream
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																						# Hago una petición
print(r.json()["response"])										# Imprime la respuesta
conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()
cursor.execute(r.json()["response"].replace("`", ""))
filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.commit()
conexion.close()
