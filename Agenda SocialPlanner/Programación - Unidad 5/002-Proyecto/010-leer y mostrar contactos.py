
import tkinter as tk

def insertaCliente():
    print("Voy a insertar una empresa")

    nombre_empresa = inputempresa.get()
    contacto = inputcontacto.get()
    instagram = inputinstagram.get()

    archivo = open("agenda.csv", "a")
    archivo.write(nombre_empresa + "," + contacto + "," + instagram + "\n")
    archivo.close()

    resultado.config(text="Contacto guardado correctamente")

    inputempresa.delete(0, tk.END)
    inputcontacto.delete(0, tk.END)
    inputinstagram.delete(0, tk.END)

    cargarContactos()


def cargarContactos():
    campodetexto.delete("1.0", tk.END)

    archivo = open("agenda.csv", "r")
    lineas = archivo.readlines()

    for linea in lineas:
        campodetexto.insert(tk.END, linea)

    archivo.close()


ventana = tk.Tk()
ventana.title("Social Media Agenda v0.1")
ventana.geometry("750x500")

marco = tk.Frame(ventana)
marco.grid(row=0, column=0, padx=20, pady=20)

titulo = tk.Label(marco, text="Social Media Agenda")
titulo.pack(padx=20, pady=20)

empresa = tk.Label(marco, text="Nombre de la empresa")
empresa.pack(padx=2, pady=2)
inputempresa = tk.Entry(marco)
inputempresa.pack(padx=10, pady=5)

contacto = tk.Label(marco, text="Contacto")
contacto.pack(padx=2, pady=2)
inputcontacto = tk.Entry(marco)
inputcontacto.pack(padx=10, pady=5)

instagram = tk.Label(marco, text="Instagram")
instagram.pack(padx=2, pady=2)
inputinstagram = tk.Entry(marco)
inputinstagram.pack(padx=10, pady=5)

boton = tk.Button(
    marco,
    text="Guardar contacto",
    command=insertaCliente
)
boton.pack(padx=10, pady=10)

resultado = tk.Label(marco, text="")
resultado.pack(padx=10, pady=5)

botonlistar = tk.Button(
    marco,
    text="Ver contactos guardados",
    command=cargarContactos
)
botonlistar.pack(padx=10, pady=10)

campodetexto = tk.Text(ventana, width=40, height=20)
campodetexto.grid(row=0, column=1, padx=20, pady=20)

archivo = open("agenda.csv", "a")
archivo.close()

ventana.mainloop()

