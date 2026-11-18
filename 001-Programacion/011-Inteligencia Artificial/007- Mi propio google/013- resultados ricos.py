
import requests                                      # Importa peticiones HTTP
import time                                          # Importa funciones de tiempo
import sqlite3                                       # Importa SQLite
from collections import deque                       # Importa una cola de URLs
from urllib.parse import urljoin, urldefrag, urlparse # Importa funciones para trabajar con URLs
from lxml import html                                # Importa HTML

conexion = sqlite3.connect("jocarsa-buscador.db")    # Conecta con la base de datos
cursor = conexion.cursor()                           # Crea un cursor para ejecutar SQL

cursor.execute("""
CREATE TABLE IF NOT EXISTS paginas (                 -- Crea la tabla si no existe
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    titulo TEXT,
    descripcion TEXT
)
""")

conexion.commit()                                    # Guarda los cambios

MAX_POR_DOMINIO = 10                                 # Máximo de páginas por dominio
MAX_PROFUNDIDAD = 3                                  # Profundidad máxima de exploración

cursor.execute("SELECT url FROM paginas")            # Recupera las URLs ya guardadas
guardadas = {fila[0] for fila in cursor.fetchall()}  # Crea un conjunto para evitar duplicados

dominios = {}                                        # Guarda el número de páginas por dominio

for url_guardada in guardadas:                       # Recorre las páginas existentes
    dominio = urlparse(url_guardada).netloc.lower()  # Obtiene el dominio
    dominios[dominio] = dominios.get(dominio, 0) + 1 # Cuenta las páginas de cada dominio

visitadas = set(guardadas)                           # Evita visitar páginas ya guardadas
pendientes = deque()                                 # Crea una cola de páginas pendientes
encoladas = set()                                    # Evita introducir URLs repetidas en la cola


def obtener_dominio(url):                            # Define una función para obtener el dominio
    dominio = urlparse(url).netloc.lower()           # Extrae el dominio de la URL
    return dominio.removeprefix("www.")               # Elimina www para unificar dominios


def agregar_url(url, profundidad):                    # Añade una URL a la cola

    if profundidad > MAX_PROFUNDIDAD:                 # Comprueba la profundidad máxima
        return                                       # Descarta la URL

    if url in visitadas or url in encoladas:          # Comprueba si ya conocemos la URL
        return                                       # Evita duplicados

    dominio = obtener_dominio(url)                    # Obtiene el dominio

    if dominios.get(dominio, 0) >= MAX_POR_DOMINIO:   # Comprueba el límite del dominio
        return                                       # No añade más páginas de ese dominio

    pendientes.append((url, profundidad))             # Añade la URL a la cola
    encoladas.add(url)                                # Marca la URL como encolada


def inspecciona():                                    # Define la función principal del crawler

    while pendientes:                                # Continúa mientras existan páginas pendientes

        posicion = None                              # Posición de la próxima página
        minimo = float("inf")                         # Inicializa el mínimo de páginas

        for i, (url, profundidad) in enumerate(pendientes): # Recorre las páginas pendientes

            dominio = obtener_dominio(url)            # Obtiene el dominio
            cantidad = dominios.get(dominio, 0)       # Cuenta sus páginas guardadas

            if cantidad < minimo:                     # Busca el dominio menos explorado
                minimo = cantidad                     # Actualiza el mínimo
                posicion = i                          # Guarda su posición

        if posicion is None:                          # Comprueba si quedan páginas válidas
            break                                     # Termina la exploración

        pendientes.rotate(-posicion)                   # Mueve la URL seleccionada al principio
        url, profundidad = pendientes.popleft()       # Extrae la URL
        pendientes.rotate(posicion)                    # Restaura el orden de la cola
        encoladas.discard(url)                         # Elimina la URL del conjunto de pendientes

        if url in visitadas:                           # Comprueba si ya se visitó
            continue                                  # Pasa a la siguiente URL

        dominio = obtener_dominio(url)                 # Obtiene el dominio actual

        if dominios.get(dominio, 0) >= MAX_POR_DOMINIO: # Comprueba el límite
            continue                                  # Salta a otro dominio

        visitadas.add(url)                             # Marca la URL como visitada

        print("  " * profundidad + "Inspeccionando:", url) # Muestra la URL

        try:                                           # Intenta descargar la página

            time.sleep(2)                              # Espera dos segundos

            contenido = requests.get(url, timeout=10)  # Descarga la página
            contenido.raise_for_status()               # Comprueba la respuesta HTTP

            if "text/html" not in contenido.headers.get("Content-Type", "").lower():
                continue                               # Ignora archivos que no sean HTML

            arbol = html.fromstring(contenido.content) # Convierte el contenido a HTML

            titulos = arbol.xpath("//title/text()")    # Busca el título
            titulo = titulos[0].strip() if titulos else "" # Obtiene el título

            descripciones = arbol.xpath(                # Busca la descripción
                "//meta[translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='description']/@content"
            )

            descripcion = descripciones[0].strip() if descripciones else "" # Obtiene la descripción

            url_final, _ = urldefrag(contenido.url)    # Obtiene la URL después de redirecciones
            dominio_final = obtener_dominio(url_final) # Obtiene el dominio definitivo

            if url_final not in guardadas and dominios.get(dominio_final, 0) < MAX_POR_DOMINIO:

                cursor.execute("""                 
                    INSERT INTO paginas (url, titulo, descripcion)
                    VALUES (?, ?, ?)
                """, (url_final, titulo, descripcion))

                conexion.commit()                      # Guarda los cambios

                guardadas.add(url_final)               # Registra la URL guardada
                visitadas.add(url_final)               # Marca la URL definitiva como visitada

                dominios[dominio_final] = dominios.get(dominio_final, 0) + 1 # Actualiza contador

                print("  " * profundidad + "Guardada:", titulo) # Muestra el resultado
                print("Dominios:", len(dominios), "| Páginas:", len(guardadas)) # Muestra estadísticas

            enlaces = arbol.xpath("//a/@href")         # Obtiene todos los enlaces

            for enlace in enlaces:                     # Recorre los enlaces

                enlace = urljoin(url_final, enlace)    # Convierte URLs relativas en absolutas
                enlace, _ = urldefrag(enlace)          # Elimina fragmentos

                if enlace.startswith(("http://", "https://")): # Comprueba el protocolo
                    agregar_url(enlace, profundidad + 1) # Añade la URL a la cola

        except requests.RequestException as error:    # Captura errores HTTP
            print("Error:", error)                     # Muestra el error

        except (ValueError, TypeError) as error:       # Captura errores de procesamiento
            print("Error procesando HTML:", error)     # Muestra el error


url = input("Introduce la url del punto de entrada: ") # Indica la página inicial

try:                                                   # Inicia el programa
    agregar_url(url, 0)                                # Añade la primera página
    inspecciona()                                      # Comienza la exploración
finally:                                               # Se ejecuta al terminar
    conexion.close()                                   # Cierra SQLite

