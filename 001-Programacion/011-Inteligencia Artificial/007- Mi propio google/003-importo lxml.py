import requests
import lxml # pip3 install lxml --break-system-packages

url = "https://jocarsa.com"

contenido = requests.get(url, timeout=10)

print(contenido.text)


