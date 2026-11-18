import requests

archivo = open("miprograma.py",'w') 					# Abro un archivo en modo escritura

ruta = "http://localhost:11434/api/generate" 	# Defino la ruta 
modelo = "codellama:7b"												# Elijo un modelo
pregunta = """ 
	Crea una calculadora de IVA en Python
  quiero que el usuario pueda introducir informacion
  quiero que hagas una interfaz web con Flask
  quiero que embebas el código html dentro del archivo sin usar templates
  solo quiero un archivo, no dos - mete el html dentro de python
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

archivo.write(r.json()["response"])						# En el archivo escribo el contenido

archivo.close()																# Cierro el archivo
