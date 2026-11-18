from flask import Flask	# Para la web
import requests																		# Para hacer peticiones http

aplicacion = Flask("__name__") 										# Creamos una aplicacion


@aplicacion.route("/")														# Escucho en la raiz
def inicio():
  ruta = "http://localhost:11434/api/generate"		# Llamo a ollama
  modelo = "qwen2.5-coder:3b"										# Elijo el modelo
  pregunta = """
  	-create an amazing html web page with css
   -add fancy CSS styling with a modern, elegant, and creative design.
	-use a clear color palette with shades of purple, lavender, and white.
	-the website will be about me, Valentina Molina, a programmer and creative person interested in technology, web development, design, marketing, and artificial intelligence.
	-include a beautiful hero section with my name, a short introduction, and a professional portrait placeholder.
	-add sections for About Me, My Skills, My Projects, and Contact.
	-use modern typography, smooth animations, gradients, rounded cards, subtle shadows, and interactive hover effects.
	-make the website responsive and visually appealing on desktop and mobile devices.
	-use only HTML and CSS, without JavaScript or external frameworks.
	-write all the HTML and CSS in a single file.
	-use Spanish for all the website content.
	-make the design look like a professional personal portfolio, with a unique and memorable visual identity.
	-include realistic content related to my studies in Desarrollo de Aplicaciones Multiplataforma (DAM) and my interests in programming, creativity, and digital innovation.
	-make the final result polished, beautiful, and suitable for a programming class presentation.
    """ 																					# Es la pregunta que le lanzo
  flujo = False																		# No me des palabra por palabra
  r = requests.post(ruta, json={
      "model":modelo,
      "prompt": pregunta,
      "stream": flujo
  })																							# Ejecutamos la petición
  mirespuesta = str(r.json()["response"])					# Obtenemos la respuesta
  return mirespuesta															# Lo que sea que venga, lo pinto en html

if __name__ == "__main__":
  aplicacion.run()
