import requests

ruta = "http://localhost:11434/api/generate" 	# Defino la ruta 
modelo = "codellama:7b"												# Elijo un modelo
pregunta = """ 
	Dame el SQL para:
  -Listar todos los cliente de Valencia
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
    - Elimina los fences markdown opentick
  
"""									# Establezco una pregunta
flujo = False																	# Elijo stream
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																						# Hago una petición
print(r.json()["response"])										# Imprime la respuesta
