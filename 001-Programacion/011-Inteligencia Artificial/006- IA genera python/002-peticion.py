import requests

ruta = "http://localhost:11434/api/generate" 	# Defino la ruta 
modelo = "codegemma:7b"												# Elijo un modelo
pregunta = """ 
	Crea una calculadora de IVA en Python
  Solo dame el codigo Python
  No me des comentarios ni explicaciones
  No me des fences ni nada de markdown
"""									# Establezco una pregunta
flujo = False																	# Elijo stream
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																						# Hago una petición
print(r.json()["response"])										# Imprime la respuesta
