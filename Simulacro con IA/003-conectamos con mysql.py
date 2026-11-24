import requests
import mysql.connector

ruta = "http://localhost:11434/api/generate" 	# Defino la ruta 
modelo = "qwen2.5:7b"												# Elijo un modelo
preguntausuario = input("Dime qué es lo que quieres: ")
pregunta = """ 
	Dame el SQL para:
  -"""+preguntausuario+"""
  -La estructura de la tabla es esta: 
      CREATE TABLE medicos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100),
  especialidad VARCHAR(100),
  numero_de_colegiado INT,
  activo INT
  
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
conexion = mysql.connector.connect(
	host="localhost",
	user="examendamceac2026",
	password="CEACExamenDAM123$",
	database="examendamceac2627"
)
cursor = conexion.cursor()
cursor.execute(r.json()["response"].replace("`", ""))
filas = cursor.fetchall()

for fila in filas:
    print(fila)

conexion.commit()
conexion.close()
