import tkinter as tk

# ============================================
# COLORES
# ============================================

FONDO = "#F7F4FC"
MORADO = "#7952A3"
MORADO_OSCURO = "#4B3268"
LILA = "#EDE4F7"
BLANCO = "#FFFFFF"
TEXTO = "#30263D"
GRIS = "#81768D"
VERDE = "#328568"
ROJO = "#C65365"


# ============================================
# FUNCIONES
# ============================================

def insertaCliente():
    nombre_empresa = inputempresa.get().strip()
    contacto = inputcontacto.get().strip()
    instagram = inputinstagram.get().strip()

    if nombre_empresa == "" and contacto == "" and instagram == "":
        resultado.config(
            text="Introduce algún dato antes de guardar.",
            fg=ROJO
        )
        return

    archivo = open("agenda.csv", "a", encoding="utf-8")
    archivo.write(
        nombre_empresa + "," +
        contacto + "," +
        instagram + "\n"
    )
    archivo.close()

    inputempresa.delete(0, tk.END)
    inputcontacto.delete(0, tk.END)
    inputinstagram.delete(0, tk.END)

    resultado.config(
        text="✓ Contacto guardado correctamente",
        fg=VERDE
    )

    cargarContactos()
    inputempresa.focus()


def cargarContactos():
    campodetexto.delete("1.0", tk.END)

    archivo = open("agenda.csv", "a", encoding="utf-8")
    archivo.close()

    archivo = open("agenda.csv", "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        campodetexto.insert(tk.END, linea)

    contador.config(
        text=str(len(lineas)) + " contactos registrados"
    )


# ============================================
# VENTANA
# ============================================

ventana = tk.Tk()
ventana.title("Social Media Agenda")
ventana.geometry("950x600")
ventana.minsize(800, 520)
ventana.configure(bg=FONDO)


# ============================================
# CONTENEDOR PRINCIPAL
# ============================================

principal = tk.Frame(ventana, bg=FONDO)
principal.pack(fill="both", expand=True, padx=30, pady=25)

principal.columnconfigure(0, weight=1)
principal.columnconfigure(1, weight=2)
principal.rowconfigure(1, weight=1)


# ============================================
# CABECERA
# ============================================

cabecera = tk.Frame(principal, bg=FONDO)
cabecera.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="ew",
    pady=(0, 22)
)

titulo = tk.Label(
    cabecera,
    text="Social Media Agenda",
    font=("Arial", 25, "bold"),
    bg=FONDO,
    fg=MORADO_OSCURO
)
titulo.pack(anchor="w")

subtitulo = tk.Label(
    cabecera,
    text="Organiza tus contactos creativos en un solo lugar.",
    font=("Arial", 11),
    bg=FONDO,
    fg=GRIS
)
subtitulo.pack(anchor="w", pady=(5, 0))


# ============================================
# FORMULARIO
# ============================================

marco = tk.LabelFrame(
    principal,
    text="  NUEVA EMPRESA  ",
    font=("Arial", 10, "bold"),
    bg=BLANCO,
    fg=MORADO,
    padx=20,
    pady=20,
    relief="flat",
    bd=0
)

marco.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=(0, 12)
)


empresa = tk.Label(
    marco,
    text="Nombre de la empresa",
    font=("Arial", 10, "bold"),
    bg=BLANCO,
    fg=TEXTO
)
empresa.pack(anchor="w", pady=(5, 5))

inputempresa = tk.Entry(
    marco,
    font=("Arial", 11),
    relief="flat",
    bg=LILA,
    fg=TEXTO,
    insertbackground=MORADO
)
inputempresa.pack(fill="x", ipady=8, pady=(0, 18))


contacto = tk.Label(
    marco,
    text="Contacto",
    font=("Arial", 10, "bold"),
    bg=BLANCO,
    fg=TEXTO
)
contacto.pack(anchor="w", pady=(0, 5))

inputcontacto = tk.Entry(
    marco,
    font=("Arial", 11),
    relief="flat",
    bg=LILA,
    fg=TEXTO,
    insertbackground=MORADO
)
inputcontacto.pack(fill="x", ipady=8, pady=(0, 18))


instagram = tk.Label(
    marco,
    text="Instagram",
    font=("Arial", 10, "bold"),
    bg=BLANCO,
    fg=TEXTO
)
instagram.pack(anchor="w", pady=(0, 5))

inputinstagram = tk.Entry(
    marco,
    font=("Arial", 11),
    relief="flat",
    bg=LILA,
    fg=TEXTO,
    insertbackground=MORADO
)
inputinstagram.pack(fill="x", ipady=8, pady=(0, 22))


boton = tk.Button(
    marco,
    text="＋  Guardar contacto",
    command=insertaCliente,
    font=("Arial", 11, "bold"),
    bg=MORADO,
    fg=BLANCO,
    activebackground=MORADO_OSCURO,
    activeforeground=BLANCO,
    relief="flat",
    cursor="hand2",
    pady=10
)
boton.pack(fill="x")


resultado = tk.Label(
    marco,
    text="",
    font=("Arial", 9),
    bg=BLANCO,
    fg=VERDE,
    wraplength=230
)
resultado.pack(anchor="w", pady=(15, 0))


# ============================================
# LISTADO DE CONTACTOS
# ============================================

derecha = tk.LabelFrame(
    principal,
    text="  MIS CONTACTOS  ",
    font=("Arial", 10, "bold"),
    bg=BLANCO,
    fg=MORADO,
    padx=18,
    pady=18,
    relief="flat",
    bd=0
)

derecha.grid(
    row=1,
    column=1,
    sticky="nsew",
    padx=(12, 0)
)

derecha.columnconfigure(0, weight=1)
derecha.rowconfigure(1, weight=1)


contador = tk.Label(
    derecha,
    text="0 contactos registrados",
    font=("Arial", 10),
    bg=BLANCO,
    fg=GRIS
)
contador.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(0, 12)
)


campodetexto = tk.Text(
    derecha,
    font=("Ubuntu Mono", 10),
    bg="#FCFAFF",
    fg=TEXTO,
    relief="flat",
    padx=12,
    pady=12,
    wrap="none",
    selectbackground=LILA
)
campodetexto.grid(
    row=1,
    column=0,
    sticky="nsew"
)


scroll = tk.Scrollbar(
    derecha,
    orient="vertical",
    command=campodetexto.yview
)
scroll.grid(row=1, column=1, sticky="ns")

campodetexto.config(yscrollcommand=scroll.set)


# ============================================
# PIE DE VENTANA
# ============================================

pie = tk.Label(
    principal,
    text="SOCIAL MEDIA AGENDA  ·  PYTHON + TKINTER",
    font=("Arial", 9),
    bg=FONDO,
    fg=GRIS
)
pie.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(18, 0)
)


# ============================================
# INICIO
# ============================================

cargarContactos()
inputempresa.focus()

ventana.mainloop()

