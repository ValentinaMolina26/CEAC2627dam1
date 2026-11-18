import requests

url = "https://jocarsa.com"

contenido = requests.get(url, timeout=10)

ruta = "http://localhost:11434/api/generate"		# La ruta donde ollama escucha
modelo = "codellama:7b" 												# Elijo un modelo
pregunta = "Responde 'si' o 'no': Esta web trata sobre marketing, sobre servicios de marketing? "+contenido.text+" - Importante, quiero un 'si' o un 'no' - y luego el por qué en una frase - no hagas muchos párrafos de explicación - solo una frase!!!"		# Elevo un prompt
flujo = False 																	# Desactivo el flujo
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})																							# Ejecuto la eticion
print(r.json()["response"])											# Devuelvo el resultado
