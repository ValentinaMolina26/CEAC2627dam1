from flask import Flask, render_template,request

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("buscador.html")

@aplicacion.route("/buscar",methods=['POST'])
def buscar():
  return render_template("resultados.html")
  
if __name__ == "__main__":
  aplicacion.run()
