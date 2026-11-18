import requests

url = "https://jocarsa.com"

contenido = requests.get(url, timeout=10)

ruta = "http://localhost:11434/api/generate"		# La ruta donde ollama escucha
modelo = "codegemma:7b" 												# Elijo un modelo
pregunta = "Resume esta web en un solo párrafo: "+contenido.text+" - Importante, solo quiero un párrafo de texto como resumen."		# Elevo un prompt
flujo = False 																	# Desactivo el flujo
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																							# Ejecuto la eticion
print(r.json()["response"])											# Devuelvo el resultado
