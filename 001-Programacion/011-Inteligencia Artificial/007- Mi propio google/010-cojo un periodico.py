import requests
import time
from lxml import html
from urllib.parse import urljoin, urldefrag

visitadas = set()

def inspecciona(url, profundidad=0, max_profundidad=3):

    if url in visitadas or profundidad > max_profundidad:
        return

    visitadas.add(url)

    print("  " * profundidad + "Inspeccionando:", url)

    try:
        # Esperar 2 segundos antes de cada petición
        time.sleep(2)

        contenido = requests.get(url, timeout=10)
        contenido.raise_for_status()

        arbol = html.fromstring(contenido.content)

        enlaces = arbol.xpath("//a/@href")

        for enlace in enlaces:

            enlace = urljoin(url, enlace)
            enlace, _ = urldefrag(enlace)

            if enlace.startswith(("http://", "https://")):
                inspecciona(
                    enlace,
                    profundidad + 1,
                    max_profundidad
                )

    except requests.RequestException as error:
        print("Error:", error)


url = "https://elmundo.es"

inspecciona(url)
