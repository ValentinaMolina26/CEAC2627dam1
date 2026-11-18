import requests																# Importamos librería de requests
from lxml import html													# Importamos librería de XML

url = "https://jocarsa.com"										# Indicamos la URL

contenido = requests.get(url, timeout=10)			# Cojo el contenido de la web en crudo
contenido.raise_for_status()									# Espero el timeout por si tarda en cargar

arbol = html.fromstring(contenido.content)		# El contenido crudo lo convierto a HTML (XML con estructura)

titulo = arbol.xpath("//title/text()")				# Busco el titulo (title)

print(titulo[0].strip() if titulo else "Sin título")	# Lo imprimo en pantalla
