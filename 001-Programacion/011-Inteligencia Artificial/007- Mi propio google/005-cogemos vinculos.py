import requests																# Importa peticiones
from lxml import html													# Importa XML

url = "https://jocarsa.com"										# La web a inspeccionar

contenido = requests.get(url, timeout=10)			# Dame el contenido
contenido.raise_for_status()									# Espera un poco

arbol = html.fromstring(contenido.content)		# Lo convertimos a HTML

enlaces = arbol.xpath("//a/@href")						# Seleccionamos todos los enlaces <a> y cogemos su href

for enlace in enlaces:												# Para cada uno de los enlaces
    print(enlace)															# Imprime el enlace
