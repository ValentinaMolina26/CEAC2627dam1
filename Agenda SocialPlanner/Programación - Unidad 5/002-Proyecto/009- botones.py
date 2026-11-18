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


ventana = tk.Tk()
ventana.title("Social Media Agenda v0.1")
ventana.geometry("400x500")

titulo = tk.Label(text="Social Media Agenda")
titulo.pack(padx=20, pady=20)

empresa = tk.Label(text="Nombre de la empresa")
empresa.pack(padx=2, pady=2)
inputempresa = tk.Entry()
inputempresa.pack(padx=10, pady=5)

contacto = tk.Label(text="Contacto")
contacto.pack(padx=2, pady=2)
inputcontacto = tk.Entry()
inputcontacto.pack(padx=10, pady=5)

instagram = tk.Label(text="Instagram")
instagram.pack(padx=2, pady=2)
inputinstagram = tk.Entry()
inputinstagram.pack(padx=10, pady=5)

boton = tk.Button(
    text="Guardar contacto",
    command=insertaCliente
)
boton.pack(padx=10, pady=10)

resultado = tk.Label(text="")
resultado.pack(padx=10, pady=5)

ventana.mainloop()

