import requests

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
    - Elimina los fences markdown opentick
  
"""									# Establezco una pregunta
flujo = False																	# Elijo stream
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																						# Hago una petición
print(r.json()["response"])										# Imprime la respuesta
