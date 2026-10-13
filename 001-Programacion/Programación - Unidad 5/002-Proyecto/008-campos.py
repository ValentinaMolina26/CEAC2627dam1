import tkinter as tk

ventana = tk.Tk()
ventana.title("Social Media Agenda v0.1")
ventana.geometry("400x450")

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

ventana.mainloop()

