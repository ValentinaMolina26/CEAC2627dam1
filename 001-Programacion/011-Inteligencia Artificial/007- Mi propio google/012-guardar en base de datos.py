import requests                                      # Importa peticiones HTTP
import time                                          # Importa funciones de tiempo
import sqlite3                                       # Importa SQLite
from lxml import html                                # Importa HTML
from urllib.parse import urljoin, urldefrag           # Importa funciones para trabajar con URLs

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

visitadas = set()                                    # Crea un conjunto de páginas visitadas


def inspecciona(url, profundidad=0, max_profundidad=3):  # Define una función recursiva

    if url in visitadas or profundidad > max_profundidad: # Comprueba si ya hemos visitado la página
        return                                           # Sale de la función

    visitadas.add(url)                               # Añade la URL a las visitadas

    print("  " * profundidad + "Inspeccionando:", url) # Muestra la página que inspeccionamos

    try:                                             # Intenta ejecutar el siguiente código

        time.sleep(2)                                # Espera 2 segundos

        contenido = requests.get(url, timeout=10)    # Descarga el contenido de la página
        contenido.raise_for_status()                 # Comprueba que la petición ha funcionado

        arbol = html.fromstring(contenido.content)   # Convierte el contenido en un árbol HTML

        titulos = arbol.xpath("//title/text()")      # Busca el título de la página
        titulo = titulos[0].strip() if titulos else "" # Obtiene el título o una cadena vacía

        descripciones = arbol.xpath(                  # Busca la descripción de la página
            "//meta[@name='description']/@content"
        )

        descripcion = descripciones[0].strip() if descripciones else "" # Obtiene la descripción

        cursor.execute("""                          
            INSERT INTO paginas (url, titulo, descripcion)
            VALUES (?, ?, ?)
        """, (url, titulo, descripcion))              # Inserta los datos de la página

        conexion.commit()                            # Guarda los datos en SQLite

        print("  " * profundidad + "Guardada:", titulo) # Muestra el título guardado

        enlaces = arbol.xpath("//a/@href")           # Busca todos los enlaces y obtiene su href

        for enlace in enlaces:                       # Recorre cada enlace encontrado

            enlace = urljoin(url, enlace)            # Convierte enlaces relativos en absolutos
            enlace, _ = urldefrag(enlace)            # Elimina los fragmentos de la URL

            if enlace.startswith(("http://", "https://")): # Comprueba que sea una URL web

                inspecciona(                         # Llama de nuevo a la función
                    enlace,                          # Pasa la nueva URL
                    profundidad + 1,                 # Aumenta la profundidad
                    max_profundidad                  # Mantiene la profundidad máxima
                )

    except requests.RequestException as error:      # Captura errores de conexión
        print("Error:", error)                       # Muestra el error


url = "https://www.ceac.es/"                           # Indica la web inicial

try:                                                 # Intenta ejecutar el crawler
    inspecciona(url)                                 # Comienza la inspección recursiva
finally:                                             # Se ejecuta al terminar o producirse un error
    conexion.close()                                 # Cierra la conexión con SQLite
