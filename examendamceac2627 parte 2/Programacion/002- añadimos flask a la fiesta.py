from flask import Flask, render_template

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():

    medicos = obtener_medicos()

    return render_template("simulacro.html", medicos=medicos)

if __name__ == "__main__":
    aplicacion.run(debug=True)
