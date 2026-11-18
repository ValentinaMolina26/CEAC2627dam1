
import requests                                          # Importa peticiones HTTP
import time                                              # Importa funciones de tiempo
import sqlite3                                           # Importa SQLite
import tldextract                                        # Importa extracción de dominios principales
from collections import deque                           # Importa una cola de URLs
from lxml import html                                    # Importa HTML
from urllib.parse import urljoin, urldefrag, urlparse    # Importa funciones para trabajar con URLs
from urllib.robotparser import RobotFileParser           # Importa el lector de robots.txt

MAX_POR_DOMINIO = 10                                     # Máximo de páginas por dominio principal
MAX_PROFUNDIDAD = 3                                      # Máxima profundidad de exploración
ESPERA = 2                                              # Segundos de espera entre peticiones
URL_INICIAL = input("Introduce la URL: ")                     # Página desde la que comienza el crawler
USER_AGENT = "JocarsaBuscador/1.0"                       # Identifica nuestro crawler

conexion = sqlite3.connect("jocarsa-buscador.db")        # Conecta con SQLite
cursor = conexion.cursor()                               # Crea un cursor SQL

cursor.execute("""
CREATE TABLE IF NOT EXISTS paginas (                     -- Crea la tabla de páginas
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    titulo TEXT,
    descripcion TEXT
)
""")

conexion.commit()                                        # Guarda los cambios

extractor = tldextract.TLDExtract(suffix_list_urls=())   # Utiliza la lista de dominios incluida en la librería


def obtener_dominio(url):                                # Obtiene el dominio principal de una URL

    resultado = extractor(url)                            # Separa subdominio, dominio y extensión

    dominio = resultado.top_domain_under_public_suffix    # Obtiene el dominio registrable

    return dominio.lower()                                # Devuelve el dominio en minúsculas


def normalizar_url(url):                                  # Normaliza una URL para evitar duplicados

    url, _ = urldefrag(url)                               # Elimina los fragmentos de la URL

    partes = urlparse(url)                                # Divide la URL en sus componentes

    if partes.scheme.lower() not in ("http", "https"):     # Comprueba que sea una URL web
        return ""                                         # Descarta otros protocolos

    if not partes.hostname:                               # Comprueba que tenga un servidor
        return ""                                         # Descarta URLs incorrectas

    esquema = partes.scheme.lower()                       # Normaliza el protocolo
    servidor = partes.netloc.lower()                       # Normaliza el servidor

    if servidor.endswith(":80") and esquema == "http":     # Comprueba el puerto HTTP estándar
        servidor = servidor[:-3]                          # Elimina el puerto innecesario

    if servidor.endswith(":443") and esquema == "https":   # Comprueba el puerto HTTPS estándar
        servidor = servidor[:-4]                          # Elimina el puerto innecesario

    ruta = partes.path or "/"                              # Utiliza / cuando no existe ruta

    return partes._replace(                               # Reconstruye la URL
        scheme=esquema,                                   # Establece el protocolo
        netloc=servidor,                                  # Establece el servidor
        path=ruta,                                        # Mantiene la ruta
        fragment=""                                       # Elimina el fragmento
    ).geturl()                                            # Devuelve la URL normalizada


cursor.execute("SELECT url FROM paginas")                 # Recupera las páginas ya guardadas

guardadas = set()                                         # Crea el conjunto de URLs guardadas
dominios = {}                                            # Crea el contador de páginas por dominio

for fila in cursor.fetchall():                           # Recorre los registros de SQLite

    url_guardada = normalizar_url(fila[0])                # Normaliza la URL existente

    if not url_guardada:                                  # Comprueba si es válida
        continue                                          # Ignora URLs incorrectas

    guardadas.add(url_guardada)                           # Añade la URL al conjunto

    dominio = obtener_dominio(url_guardada)               # Obtiene el dominio principal

    dominios[dominio] = dominios.get(dominio, 0) + 1      # Cuenta páginas incluyendo subdominios


visitadas = set(guardadas)                                # Inicializa las URLs visitadas
pendientes = deque()                                     # Crea la cola de URLs pendientes
encoladas = set()                                        # Controla las URLs ya encoladas
robots_cache = {}                                        # Guarda las reglas robots.txt consultadas
ultima_peticion = {}                                     # Guarda el instante de la última petición por servidor

sesion = requests.Session()                              # Crea una sesión HTTP reutilizable
sesion.headers.update({"User-Agent": USER_AGENT})        # Identifica el crawler en las peticiones


def permitido_por_robots(url):                           # Comprueba si podemos explorar una URL

    partes = urlparse(url)                                # Analiza la URL
    origen = partes.scheme + "://" + partes.netloc         # Obtiene el origen del servidor

    if origen not in robots_cache:                        # Comprueba si ya consultamos sus reglas

        parser = RobotFileParser()                        # Crea un lector de robots.txt
        parser.set_url(origen + "/robots.txt")            # Indica dónde se encuentran las reglas

        try:                                              # Intenta descargar las reglas

            respuesta = sesion.get(                       # Descarga robots.txt
                origen + "/robots.txt",
                timeout=10
            )

            if respuesta.status_code == 404:              # Comprueba si no existe robots.txt
                robots_cache[origen] = None               # Permite explorar sin reglas publicadas

            elif respuesta.status_code == 200:            # Comprueba si se han recibido reglas
                parser.parse(respuesta.text.splitlines()) # Interpreta las reglas
                robots_cache[origen] = parser             # Guarda las reglas del servidor

            else:                                         # Otros estados HTTP
                robots_cache[origen] = False              # Evita explorar si no podemos comprobarlas

        except requests.RequestException:                # Captura errores de conexión
            robots_cache[origen] = False                  # Evita explorar sin verificar las reglas

    reglas = robots_cache[origen]                          # Recupera las reglas

    if reglas is False:                                   # Comprueba si se ha bloqueado el origen
        return False                                      # No permite la exploración

    if reglas is None:                                    # Comprueba si no existe robots.txt
        return True                                       # Permite la exploración

    return reglas.can_fetch(USER_AGENT, url)              # Comprueba si la URL está permitida


def agregar_url(url, profundidad):                        # Añade una URL a la cola

    url = normalizar_url(url)                             # Normaliza la URL

    if not url:                                           # Comprueba si la URL es válida
        return                                            # Descarta URLs incorrectas

    if profundidad > MAX_PROFUNDIDAD:                      # Comprueba la profundidad máxima
        return                                            # Descarta URLs demasiado profundas

    if url in visitadas or url in encoladas:               # Comprueba si la URL ya se conoce
        return                                            # Evita duplicados

    dominio = obtener_dominio(url)                        # Obtiene el dominio principal

    if not dominio:                                       # Comprueba que exista dominio
        return                                            # Descarta la URL

    if dominios.get(dominio, 0) >= MAX_POR_DOMINIO:        # Comprueba el límite por dominio
        return                                            # Descarta páginas de dominios completos

    pendientes.append((url, profundidad))                  # Añade la URL a la cola
    encoladas.add(url)                                     # Marca la URL como pendiente


def seleccionar_url():                                    # Selecciona el siguiente dominio a explorar

    mejor_posicion = None                                 # Guarda la posición seleccionada
    menor_cantidad = float("inf")                          # Inicializa el mínimo de páginas

    for posicion, (url, profundidad) in enumerate(pendientes): # Recorre la cola

        dominio = obtener_dominio(url)                    # Obtiene el dominio principal
        cantidad = dominios.get(dominio, 0)               # Consulta sus páginas guardadas

        if cantidad >= MAX_POR_DOMINIO:                    # Comprueba si alcanzó el límite
            continue                                      # Ignora el dominio completo

        if cantidad < menor_cantidad:                      # Busca el dominio menos explorado
            menor_cantidad = cantidad                     # Actualiza la cantidad mínima
            mejor_posicion = posicion                      # Guarda la posición

            if cantidad == 0:                             # Comprueba si el dominio es nuevo
                break                                     # Prioriza inmediatamente ese dominio

    if mejor_posicion is None:                             # Comprueba si quedan dominios disponibles
        return None                                       # Indica que no quedan páginas válidas

    pendientes.rotate(-mejor_posicion)                     # Mueve la URL seleccionada al principio
    resultado = pendientes.popleft()                      # Extrae la URL
    pendientes.rotate(mejor_posicion)                      # Restaura el orden de la cola

    encoladas.discard(resultado[0])                        # Elimina la URL de las pendientes

    return resultado                                      # Devuelve URL y profundidad


def inspecciona():                                        # Define la función principal del crawler

    while pendientes:                                     # Continúa mientras existan URLs pendientes

        seleccion = seleccionar_url()                      # Selecciona el dominio menos explorado

        if seleccion is None:                              # Comprueba si hay una URL válida
            break                                         # Finaliza la exploración

        url, profundidad = seleccion                       # Obtiene la URL y su profundidad

        if url in visitadas:                               # Comprueba si ya se visitó
            continue                                      # Evita repetir la inspección

        dominio = obtener_dominio(url)                     # Obtiene el dominio principal

        if dominios.get(dominio, 0) >= MAX_POR_DOMINIO:     # Comprueba el límite del dominio
            continue                                      # Pasa al siguiente dominio

        visitadas.add(url)                                 # Marca la URL como visitada

        if not permitido_por_robots(url):                  # Comprueba las reglas robots.txt
            print("No permitido por robots.txt:", url)     # Informa del bloqueo
            continue                                      # Pasa a la siguiente URL

        print("  " * profundidad + "Inspeccionando:", url) # Muestra la URL

        try:                                               # Intenta descargar la página

            servidor = urlparse(url).netloc                # Obtiene el servidor actual
            ahora = time.monotonic()                       # Obtiene el instante actual
            anterior = ultima_peticion.get(servidor, 0)    # Obtiene la última petición

            espera = max(0, ESPERA - (ahora - anterior))   # Calcula la espera necesaria

            if espera > 0:                                 # Comprueba si debe esperar
                time.sleep(espera)                         # Respeta el intervalo por servidor

            ultima_peticion[servidor] = time.monotonic()   # Registra el momento de la petición

            respuesta = sesion.get(                        # Descarga la página
                url,
                timeout=10,
                allow_redirects=False
            )

            if respuesta.status_code in (301, 302, 303, 307, 308): # Comprueba redirecciones

                destino = respuesta.headers.get("Location", "") # Obtiene la nueva ubicación

                if destino:                                # Comprueba que exista destino
                    destino = normalizar_url(urljoin(url, destino)) # Construye la URL definitiva

                    if destino:                            # Comprueba que sea válida
                        agregar_url(destino, profundidad)  # Añade el destino a la cola

                continue                                   # No procesa la respuesta de redirección

            respuesta.raise_for_status()                   # Comprueba que la petición fue correcta

            tipo = respuesta.headers.get("Content-Type", "").lower() # Obtiene el tipo de contenido

            if "text/html" not in tipo:                     # Comprueba que sea HTML
                continue                                   # Ignora imágenes, PDF y otros archivos

            arbol = html.fromstring(respuesta.content)     # Convierte la respuesta en árbol HTML

            titulos = arbol.xpath("//title/text()")        # Busca el título de la página
            titulo = titulos[0].strip() if titulos else ""  # Obtiene el título

            descripciones = arbol.xpath(                    # Busca la metadescripción
                "//meta[translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='description']/@content"
            )

            descripcion = descripciones[0].strip() if descripciones else "" # Obtiene la descripción

            if url not in guardadas:                        # Comprueba si la página es nueva

                cursor.execute("""                       
                    INSERT INTO paginas (url, titulo, descripcion)
                    VALUES (?, ?, ?)
                """, (url, titulo, descripcion))

                conexion.commit()                          # Guarda el registro

                guardadas.add(url)                         # Añade la URL a las guardadas

                dominios[dominio] = dominios.get(dominio, 0) + 1 # Incrementa el contador

                print("  " * profundidad + "Guardada:", titulo) # Muestra el título

                print(                                     # Muestra estadísticas
                    "Dominios:", len(dominios),
                    "| Páginas:", len(guardadas),
                    "| Dominio actual:", dominio,
                    "| Páginas del dominio:", dominios[dominio]
                )

            enlaces = arbol.xpath("//a/@href")             # Extrae todos los enlaces

            for enlace in enlaces:                         # Recorre los enlaces encontrados

                enlace = urljoin(url, enlace)              # Convierte enlaces relativos en absolutos

                agregar_url(enlace, profundidad + 1)        # Añade los enlaces a la cola

        except requests.RequestException as error:        # Captura errores HTTP
            print("Error de conexión:", error)             # Muestra el error

        except (ValueError, TypeError) as error:           # Captura errores de procesamiento
            print("Error procesando página:", error)       # Muestra el error


try:                                                       # Inicia el crawler

    print("Páginas existentes:", len(guardadas))            # Muestra páginas guardadas
    print("Dominios existentes:", len(dominios))            # Muestra dominios registrados

    agregar_url(URL_INICIAL, 0)                            # Añade la URL inicial

    inspecciona()                                          # Comienza la exploración

finally:                                                   # Se ejecuta al terminar

    sesion.close()                                         # Cierra la sesión HTTP
    conexion.close()                                       # Cierra SQLite

    print("Exploración finalizada")                         # Informa de la finalización

