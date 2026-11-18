
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
import uuid
from datetime import datetime

# -----------------------------------
# CONFIGURACIÓN
# -----------------------------------

ARCHIVO = "agenda.csv"

CAMPOS = [
    "id",
    "empresa",
    "contacto",
    "telefono",
    "correo",
    "instagram",
    "tiktok",
    "facebook",
    "sector",
    "ciudad",
    "tipo",
    "estado",
    "notas",
    "fecha_registro",
    "ultimo_contacto",
    "proximo_contacto"
]

contactos = []
contacto_seleccionado = None

COLOR_FONDO = "#f5f0fa"
COLOR_PRINCIPAL = "#8064a2"
COLOR_SECUNDARIO = "#e9ddf3"
COLOR_TEXTO = "#40334d"


# -----------------------------------
# GUARDAR Y CARGAR DATOS
# -----------------------------------

def guardarContactos():
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(contactos)


def cargarContactos():
    global contactos

    if not os.path.exists(ARCHIVO):
        contactos = []
        return

    try:
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            if lector.fieldnames is None:
                contactos = []
                return

            contactos = []

            for fila in lector:
                if "empresa" not in fila:
                    continue

                contacto = {}

                for campo in CAMPOS:
                    contacto[campo] = fila.get(campo, "") or ""

                if not contacto["id"]:
                    contacto["id"] = str(uuid.uuid4())

                if not contacto["fecha_registro"]:
                    contacto["fecha_registro"] = datetime.now().strftime("%Y-%m-%d")

                contactos.append(contacto)

        guardarContactos()

    except (OSError, csv.Error) as error:
        messagebox.showerror(
            "Error",
            f"No se pudieron cargar los contactos:\n{error}"
        )
        contactos = []


# -----------------------------------
# LIMPIAR FORMULARIO
# -----------------------------------

def limpiarFormulario():
    global contacto_seleccionado

    for campo in entradas:
        entradas[campo].delete(0, tk.END)

    notas.delete("1.0", tk.END)

    tipo.set("Cliente")
    estado.set("Nuevo")

    contacto_seleccionado = None
    boton_guardar.config(text="Guardar contacto")
    mensaje.config(text="Formulario preparado para un nuevo contacto")

    lienzo.yview_moveto(0)


# -----------------------------------
# OBTENER DATOS DEL FORMULARIO
# -----------------------------------

def obtenerDatos():
    datos = {}

    for campo in entradas:
        datos[campo] = entradas[campo].get().strip()

    datos["tipo"] = tipo.get()
    datos["estado"] = estado.get()
    datos["notas"] = notas.get("1.0", tk.END).strip()

    return datos


# -----------------------------------
# VALIDAR INFORMACIÓN
# -----------------------------------

def validarDatos(datos):
    if not datos["empresa"]:
        messagebox.showwarning(
            "Campo obligatorio",
            "Debes introducir el nombre de la empresa."
        )
        return False

    correo = datos["correo"]

    if correo and ("@" not in correo or "." not in correo.split("@")[-1]):
        messagebox.showwarning(
            "Correo incorrecto",
            "Comprueba que el correo electrónico sea válido."
        )
        return False

    for campo in ["ultimo_contacto", "proximo_contacto"]:
        fecha = datos[campo]

        if fecha:
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                messagebox.showwarning(
                    "Fecha incorrecta",
                    f"El campo {campo.replace('_', ' ')} debe tener el formato AAAA-MM-DD."
                )
                return False

    return True


# -----------------------------------
# AÑADIR CONTACTO
# -----------------------------------

def insertaCliente():
    datos = obtenerDatos()

    if not validarDatos(datos):
        return

    datos["id"] = str(uuid.uuid4())
    datos["fecha_registro"] = datetime.now().strftime("%Y-%m-%d")

    contactos.append(datos)

    guardarContactos()
    mostrarContactos()
    actualizarEstadisticas()
    limpiarFormulario()

    mensaje.config(text="Contacto guardado correctamente")


# -----------------------------------
# MOSTRAR CONTACTOS
# -----------------------------------

def mostrarContactos():
    for elemento in tabla.get_children():
        tabla.delete(elemento)

    busqueda = buscar.get().strip().lower()
    filtro = filtro_estado.get()

    for contacto in contactos:

        texto = " ".join(str(valor) for valor in contacto.values()).lower()

        if busqueda not in texto:
            continue

        if filtro != "Todos" and contacto["estado"] != filtro:
            continue

        tabla.insert(
            "",
            tk.END,
            iid=contacto["id"],
            values=(
                contacto["empresa"],
                contacto["contacto"],
                contacto["telefono"],
                contacto["correo"],
                contacto["sector"],
                contacto["estado"]
            )
        )


# -----------------------------------
# SELECCIONAR CONTACTO
# -----------------------------------

def seleccionarContacto(event=None):
    global contacto_seleccionado

    seleccion = tabla.selection()

    if not seleccion:
        return

    identificador = seleccion[0]

    for contacto in contactos:
        if contacto["id"] == identificador:

            contacto_seleccionado = identificador

            for campo in entradas:
                entradas[campo].delete(0, tk.END)
                entradas[campo].insert(0, contacto[campo])

            tipo.set(contacto["tipo"] or "Cliente")
            estado.set(contacto["estado"] or "Nuevo")

            notas.delete("1.0", tk.END)
            notas.insert("1.0", contacto["notas"])

            boton_guardar.config(text="Guardar cambios")
            mensaje.config(text=f"Editando: {contacto['empresa']}")

            break


# -----------------------------------
# EDITAR CONTACTO
# -----------------------------------

def actualizarCliente():
    if not contacto_seleccionado:
        insertaCliente()
        return

    datos = obtenerDatos()

    if not validarDatos(datos):
        return

    for contacto in contactos:
        if contacto["id"] == contacto_seleccionado:

            for campo in datos:
                contacto[campo] = datos[campo]

            break

    guardarContactos()
    mostrarContactos()
    actualizarEstadisticas()
    limpiarFormulario()

    mensaje.config(text="Contacto actualizado correctamente")


# -----------------------------------
# ELIMINAR CONTACTO
# -----------------------------------

def eliminarCliente():
    global contactos

    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showwarning(
            "Selecciona un contacto",
            "Primero debes seleccionar un contacto de la tabla."
        )
        return

    identificador = seleccion[0]

    confirmar = messagebox.askyesno(
        "Eliminar contacto",
        "¿Estás segura de que quieres eliminar este contacto?"
    )

    if confirmar:
        contactos = [
            contacto for contacto in contactos
            if contacto["id"] != identificador
        ]

        guardarContactos()
        mostrarContactos()
        actualizarEstadisticas()
        limpiarFormulario()

        mensaje.config(text="Contacto eliminado correctamente")


# -----------------------------------
# BUSCAR Y FILTRAR
# -----------------------------------

def buscarContactos(event=None):
    mostrarContactos()


def filtrarContactos(event=None):
    mostrarContactos()


# -----------------------------------
# ESTADÍSTICAS
# -----------------------------------

def actualizarEstadisticas():
    total = len(contactos)

    activos = sum(
        1 for contacto in contactos
        if contacto["estado"] == "Activo"
    )

    pendientes = sum(
        1 for contacto in contactos
        if contacto["estado"] == "Pendiente"
    )

    nuevos = sum(
        1 for contacto in contactos
        if contacto["estado"] == "Nuevo"
    )

    texto_estadisticas.config(
        text=f"Total: {total}     Activos: {activos}     "
             f"Pendientes: {pendientes}     Nuevos: {nuevos}"
    )


# -----------------------------------
# EXPORTAR CONTACTOS
# -----------------------------------

def exportarContactos():
    ruta = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("Archivo CSV", "*.csv")],
        initialfile="contactos_exportados.csv"
    )

    if not ruta:
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(contactos)

        messagebox.showinfo(
            "Exportación completada",
            "Los contactos se han exportado correctamente."
        )

    except OSError as error:
        messagebox.showerror("Error", str(error))


# -----------------------------------
# VENTANA PRINCIPAL
# -----------------------------------

ventana = tk.Tk()
ventana.title("Social Media Agenda")
ventana.geometry("1150x760")
ventana.minsize(950, 650)
ventana.configure(bg=COLOR_FONDO)


# -----------------------------------
# ESTILOS
# -----------------------------------

estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "Treeview",
    background="white",
    foreground=COLOR_TEXTO,
    rowheight=30,
    fieldbackground="white"
)

estilo.configure(
    "Treeview.Heading",
    background=COLOR_SECUNDARIO,
    foreground=COLOR_TEXTO,
    font=("Arial", 9, "bold")
)

estilo.map(
    "Treeview",
    background=[("selected", COLOR_PRINCIPAL)],
    foreground=[("selected", "white")]
)

estilo.configure(
    "TCombobox",
    padding=5
)


# -----------------------------------
# ENCABEZADO
# -----------------------------------

encabezado = tk.Frame(ventana, bg=COLOR_PRINCIPAL, pady=18)
encabezado.pack(fill="x")

tk.Label(
    encabezado,
    text="SOCIAL MEDIA AGENDA",
    font=("Arial", 21, "bold"),
    bg=COLOR_PRINCIPAL,
    fg="white"
).pack()

tk.Label(
    encabezado,
    text="Organiza y gestiona tus contactos profesionales",
    font=("Arial", 10),
    bg=COLOR_PRINCIPAL,
    fg="white"
).pack(pady=4)


# -----------------------------------
# ESTADÍSTICAS
# -----------------------------------

texto_estadisticas = tk.Label(
    ventana,
    text="",
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    font=("Arial", 11, "bold"),
    pady=12
)
texto_estadisticas.pack()


# -----------------------------------
# CONTENEDOR PRINCIPAL
# -----------------------------------

principal = tk.Frame(ventana, bg=COLOR_FONDO)
principal.pack(fill="both", expand=True, padx=15, pady=5)

principal.columnconfigure(0, weight=1)
principal.columnconfigure(1, weight=2)
principal.rowconfigure(0, weight=1)


# -----------------------------------
# FORMULARIO CON SCROLL
# -----------------------------------

panel_formulario = tk.LabelFrame(
    principal,
    text=" Información del contacto ",
    bg="white",
    fg=COLOR_PRINCIPAL,
    font=("Arial", 11, "bold"),
    padx=5,
    pady=5
)

panel_formulario.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=(0, 10)
)

panel_formulario.columnconfigure(0, weight=1)
panel_formulario.rowconfigure(0, weight=1)

lienzo = tk.Canvas(
    panel_formulario,
    bg="white",
    highlightthickness=0
)

lienzo.grid(row=0, column=0, sticky="nsew")

scroll = ttk.Scrollbar(
    panel_formulario,
    orient="vertical",
    command=lienzo.yview
)

scroll.grid(row=0, column=1, sticky="ns")

lienzo.configure(yscrollcommand=scroll.set)

contenido_formulario = tk.Frame(
    lienzo,
    bg="white",
    padx=8,
    pady=5
)

ventana_formulario = lienzo.create_window(
    (0, 0),
    window=contenido_formulario,
    anchor="nw"
)


def actualizarScroll(event=None):
    lienzo.configure(scrollregion=lienzo.bbox("all"))


contenido_formulario.bind("<Configure>", actualizarScroll)


def ajustarAncho(event):
    lienzo.itemconfigure(
        ventana_formulario,
        width=event.width
    )


lienzo.bind("<Configure>", ajustarAncho)


def moverScroll(event):
    lienzo.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


def activarScroll(event):
    lienzo.bind_all("<MouseWheel>", moverScroll)


def desactivarScroll(event):
    lienzo.unbind_all("<MouseWheel>")


lienzo.bind("<Enter>", activarScroll)
lienzo.bind("<Leave>", desactivarScroll)


entradas = {}


# -----------------------------------
# CREAR CAMPOS
# -----------------------------------

def crearCampo(nombre, etiqueta, fila):
    tk.Label(
        contenido_formulario,
        text=etiqueta,
        bg="white",
        fg=COLOR_TEXTO,
        font=("Arial", 9, "bold")
    ).grid(row=fila, column=0, sticky="w", pady=(5, 2))

    entrada = tk.Entry(
        contenido_formulario,
        font=("Arial", 10),
        relief="solid",
        bd=1
    )

    entrada.grid(row=fila + 1, column=0, sticky="ew", ipady=5)

    entradas[nombre] = entrada


contenido_formulario.columnconfigure(0, weight=1)

crearCampo("empresa", "Empresa *", 0)
crearCampo("contacto", "Persona de contacto", 2)
crearCampo("telefono", "Teléfono", 4)
crearCampo("correo", "Correo electrónico", 6)
crearCampo("instagram", "Instagram", 8)
crearCampo("tiktok", "TikTok", 10)
crearCampo("facebook", "Facebook", 12)
crearCampo("sector", "Sector o actividad", 14)
crearCampo("ciudad", "Ciudad", 16)


# -----------------------------------
# TIPO DE CONTACTO
# -----------------------------------

tk.Label(
    contenido_formulario,
    text="Tipo de contacto",
    bg="white",
    fg=COLOR_TEXTO
).grid(row=18, column=0, sticky="w", pady=(7, 2))

tipo = ttk.Combobox(
    contenido_formulario,
    values=["Cliente", "Posible cliente", "Proveedor", "Colaborador"],
    state="readonly"
)

tipo.set("Cliente")
tipo.grid(row=19, column=0, sticky="ew")


# -----------------------------------
# ESTADO
# -----------------------------------

tk.Label(
    contenido_formulario,
    text="Estado",
    bg="white",
    fg=COLOR_TEXTO
).grid(row=20, column=0, sticky="w", pady=(7, 2))

estado = ttk.Combobox(
    contenido_formulario,
    values=["Nuevo", "Pendiente", "Interesado", "Activo", "Inactivo"],
    state="readonly"
)

estado.set("Nuevo")
estado.grid(row=21, column=0, sticky="ew")


# -----------------------------------
# FECHAS
# -----------------------------------

crearCampo("ultimo_contacto", "Último contacto (AAAA-MM-DD)", 22)
crearCampo("proximo_contacto", "Próximo contacto (AAAA-MM-DD)", 24)


# -----------------------------------
# NOTAS
# -----------------------------------

tk.Label(
    contenido_formulario,
    text="Notas",
    bg="white",
    fg=COLOR_TEXTO
).grid(row=26, column=0, sticky="w", pady=(7, 2))

notas = tk.Text(
    contenido_formulario,
    height=4,
    font=("Arial", 10),
    relief="solid",
    bd=1
)

notas.grid(row=27, column=0, sticky="ew")


# -----------------------------------
# BOTONES DEL FORMULARIO
# -----------------------------------

boton_guardar = tk.Button(
    contenido_formulario,
    text="Guardar contacto",
    command=insertaCliente,
    bg=COLOR_PRINCIPAL,
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    pady=8
)

boton_guardar.grid(row=28, column=0, sticky="ew", pady=(12, 5))

tk.Button(
    contenido_formulario,
    text="Limpiar formulario",
    command=limpiarFormulario,
    bg=COLOR_SECUNDARIO,
    fg=COLOR_TEXTO,
    relief="flat",
    pady=7
).grid(row=29, column=0, sticky="ew", pady=3)


# -----------------------------------
# PANEL DE CONTACTOS
# -----------------------------------

panel_contactos = tk.LabelFrame(
    principal,
    text=" Directorio de contactos ",
    bg="white",
    fg=COLOR_PRINCIPAL,
    font=("Arial", 11, "bold"),
    padx=12,
    pady=10
)

panel_contactos.grid(
    row=0,
    column=1,
    sticky="nsew"
)

panel_contactos.columnconfigure(0, weight=1)
panel_contactos.rowconfigure(3, weight=1)


# -----------------------------------
# BUSCADOR
# -----------------------------------

tk.Label(
    panel_contactos,
    text="Buscar contacto",
    bg="white",
    fg=COLOR_TEXTO
).grid(row=0, column=0, sticky="w")

buscar = tk.Entry(
    panel_contactos,
    font=("Arial", 10),
    relief="solid",
    bd=1
)

buscar.grid(row=1, column=0, sticky="ew", ipady=6, pady=5)
buscar.bind("<KeyRelease>", buscarContactos)


# -----------------------------------
# FILTRO DE ESTADO
# -----------------------------------

filtros = tk.Frame(panel_contactos, bg="white")
filtros.grid(row=2, column=0, sticky="ew", pady=5)

tk.Label(
    filtros,
    text="Filtrar por estado:",
    bg="white",
    fg=COLOR_TEXTO
).pack(side="left")

filtro_estado = ttk.Combobox(
    filtros,
    values=["Todos", "Nuevo", "Pendiente", "Interesado", "Activo", "Inactivo"],
    state="readonly",
    width=15
)

filtro_estado.set("Todos")
filtro_estado.pack(side="left", padx=8)
filtro_estado.bind("<<ComboboxSelected>>", filtrarContactos)


# -----------------------------------
# TABLA
# -----------------------------------

columnas = (
    "empresa",
    "contacto",
    "telefono",
    "correo",
    "sector",
    "estado"
)

tabla = ttk.Treeview(
    panel_contactos,
    columns=columnas,
    show="headings"
)

tabla.heading("empresa", text="Empresa")
tabla.heading("contacto", text="Contacto")
tabla.heading("telefono", text="Teléfono")
tabla.heading("correo", text="Correo")
tabla.heading("sector", text="Sector")
tabla.heading("estado", text="Estado")

tabla.column("empresa", width=130)
tabla.column("contacto", width=110)
tabla.column("telefono", width=100)
tabla.column("correo", width=150)
tabla.column("sector", width=100)
tabla.column("estado", width=90)

tabla.grid(row=3, column=0, sticky="nsew", pady=8)

tabla.bind("<<TreeviewSelect>>", seleccionarContacto)


# -----------------------------------
# BARRA DE DESPLAZAMIENTO TABLA
# -----------------------------------

barra = ttk.Scrollbar(
    panel_contactos,
    orient="vertical",
    command=tabla.yview
)

tabla.configure(yscrollcommand=barra.set)
barra.grid(row=3, column=1, sticky="ns")


# -----------------------------------
# BOTONES DE GESTIÓN
# -----------------------------------

botones = tk.Frame(panel_contactos, bg="white")
botones.grid(row=4, column=0, sticky="ew", pady=10)

tk.Button(
    botones,
    text="Guardar cambios",
    command=actualizarCliente,
    bg=COLOR_PRINCIPAL,
    fg="white",
    relief="flat",
    padx=10,
    pady=7
).pack(side="left", padx=3)

tk.Button(
    botones,
    text="Eliminar",
    command=eliminarCliente,
    bg="#b75b70",
    fg="white",
    relief="flat",
    padx=10,
    pady=7
).pack(side="left", padx=3)

tk.Button(
    botones,
    text="Exportar CSV",
    command=exportarContactos,
    bg=COLOR_SECUNDARIO,
    fg=COLOR_TEXTO,
    relief="flat",
    padx=10,
    pady=7
).pack(side="left", padx=3)


# -----------------------------------
# MENSAJE INFERIOR
# -----------------------------------

mensaje = tk.Label(
    ventana,
    text="Bienvenida a Social Media Agenda",
    bg=COLOR_FONDO,
    fg=COLOR_PRINCIPAL,
    font=("Arial", 9),
    pady=8
)

mensaje.pack(fill="x")


# -----------------------------------
# INICIAR APLICACIÓN
# -----------------------------------

cargarContactos()
mostrarContactos()
actualizarEstadisticas()

ventana.mainloop()

