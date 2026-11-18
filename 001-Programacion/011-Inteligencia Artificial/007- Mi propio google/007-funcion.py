import requests																# Importa peticiones
from lxml import html													# Importa XML



def inspecciona(url):														# Defino una funcion con url de entrada
  contenido = requests.get(url, timeout=10)			# Dame el contenido
  contenido.raise_for_status()									# Espera un poco
  arbol = html.fromstring(contenido.content)		# Lo convertimos a HTML
  enlaces = arbol.xpath("//a/@href")						# Seleccionamos todos los enlaces <a> y cogemos su href
  return enlaces																# Retorno un listado de enlaces

url = "https://josevicentecarratala.com"				# La web a inspeccionar

while True: 																		# BUCLE INFINITO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  enlaces = inspecciona(url)										# Ejecuta la inspeccion
  for enlace in enlaces:												# Para cada uno de los enlaces
    inspecciona(enlace)													# Inspecciona ese enlace
