import requests

url = "https://jocarsa.com"

contenido = requests.get(url, timeout=10)

ruta = "http://localhost:11434/api/generate"		# La ruta donde ollama escucha
modelo = "qwen3.5:0.8b" 												# Elijo un modelo
pregunta = "Resume esta web: "+contenido.text		# Elevo un prompt
flujo = False 																	# Desactivo el flujo
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																							# Ejecuto la eticion
print(r.json()["response"])											# Devuelvo el resultado
