import requests

url = "https://jocarsa.com"

contenido = requests.get(url, timeout=10)

print(contenido.text)


