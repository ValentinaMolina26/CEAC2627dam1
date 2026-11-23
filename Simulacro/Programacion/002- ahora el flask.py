from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Crear la ruta principal
@app.route("/")
def inicio():
    return "<h1>Bienvenido a SOCIAL HUB</h1><p>Mi primera aplicación con Flask</p>"

# Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)

