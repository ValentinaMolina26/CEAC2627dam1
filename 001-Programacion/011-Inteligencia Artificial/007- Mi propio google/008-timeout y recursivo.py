import requests
from lxml import html
from urllib.parse import urljoin, urldefrag

visitadas = set()

def inspecciona(url, profundidad=0, max_profundidad=3):
    # Evitar repeticiones y limitar profundidad
    if url in visitadas or profundidad > max_profundidad:
        return
    visitadas.add(url)
    print("  " * profundidad + "Inspeccionando:", url)
    try:
        # Petición con timeout de 10 segundos
        contenido = requests.get(url, timeout=10)
        contenido.raise_for_status()
        # Convertir contenido a HTML
        arbol = html.fromstring(contenido.content)
        # Obtener enlaces
        enlaces = arbol.xpath("//a/@href")
        # Recorrer enlaces recursivamente
        for enlace in enlaces:
            # Convertir enlaces relativos en absolutos
            enlace = urljoin(url, enlace)
            # Eliminar fragmentos (#seccion)
            enlace, _ = urldefrag(enlace)
            # Solo HTTP y HTTPS
            if enlace.startswith(("http://", "https://")):
                inspecciona(
                    enlace,
                    profundidad + 1,
                    max_profundidad
                )

    except requests.RequestException as error:
        print("Error:", error)


url = "https://josevicentecarratala.com"

inspecciona(url)
