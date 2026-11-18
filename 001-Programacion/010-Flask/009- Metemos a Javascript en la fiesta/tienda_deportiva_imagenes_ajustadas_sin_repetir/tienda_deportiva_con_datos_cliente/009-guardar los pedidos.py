from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import sqlite3
from datetime import datetime
import os

aplicacion = Flask(__name__)
aplicacion.secret_key = os.environ.get("TIENDA_SECRET_KEY", "cambia-esta-clave-en-tu-equipo")
USUARIO_ADMIN = "admin"
CONTRASENA_ADMIN = "Valentina2026!"  # Cámbiala antes de publicar la web
BASE_DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tienda.db")

# Estos son los 30 productos que ya tenía tu proyecto original.
PRODUCTOS_ORIGINALES = [
    ("Zapatillas running", "Zapatillas ligeras para correr", "59"),
    ("Zapatillas fútbol", "Botas de fútbol para césped artificial", "75"),
    ("Zapatillas baloncesto", "Zapatillas de baloncesto con amortiguación", "89"),
    ("Camiseta deportiva", "Camiseta transpirable de entrenamiento", "19"),
    ("Pantalón corto", "Pantalón corto para actividades deportivas", "24"),
    ("Sudadera deportiva", "Sudadera con capucha para entrenamiento", "45"),
    ("Chándal completo", "Conjunto deportivo de chaqueta y pantalón", "69"),
    ("Calcetines deportivos", "Pack de tres pares de calcetines", "12"),
    ("Mochila deportiva", "Mochila de entrenamiento de 30 litros", "39"),
    ("Bolsa de gimnasio", "Bolsa deportiva con compartimento para calzado", "35"),
    ("Balón de fútbol", "Balón de fútbol tamaño 5", "29"),
    ("Balón de baloncesto", "Balón de baloncesto de competición", "32"),
    ("Balón de voleibol", "Balón de voleibol para interior", "27"),
    ("Raqueta de tenis", "Raqueta de tenis de grafito", "95"),
    ("Pala de pádel", "Pala de pádel de fibra de carbono", "110"),
    ("Pelotas de tenis", "Bote de tres pelotas de tenis", "8"),
    ("Guantes de portero", "Guantes de fútbol con agarre reforzado", "42"),
    ("Espinilleras", "Protecciones ligeras para fútbol", "15"),
    ("Comba deportiva", "Cuerda de saltar ajustable", "14"),
    ("Mancuernas 5 kg", "Pareja de mancuernas de cinco kilogramos", "39"),
    ("Mancuernas 10 kg", "Pareja de mancuernas de diez kilogramos", "69"),
    ("Esterilla fitness", "Esterilla antideslizante para ejercicios", "22"),
    ("Bandas elásticas", "Juego de bandas de resistencia", "18"),
    ("Banco de musculación", "Banco ajustable para entrenamiento de fuerza", "149"),
    ("Bicicleta estática", "Bicicleta de ejercicio con pantalla digital", "249"),
    ("Casco de ciclismo", "Casco ligero con ventilación", "49"),
    ("Gafas de natación", "Gafas de piscina antivaho", "16"),
    ("Gorro de natación", "Gorro de silicona para piscina", "9"),
    ("Botella deportiva", "Botella reutilizable de un litro", "13"),
    ("Reloj deportivo", "Reloj con pulsómetro y seguimiento de actividad", "129"),
]

def preparar_base_datos():
    conexion = sqlite3.connect(BASE_DATOS)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            descripcion TEXT,
            precio TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numerodepedido TEXT,
            fecha TEXT,
            carga TEXT,
            nombre TEXT,
            apellido TEXT,
            correo TEXT
        )
    """)
    # Añade las columnas de cliente a bases de datos antiguas sin borrar pedidos.
    cursor.execute("PRAGMA table_info(pedidos)")
    columnas_pedido = [columna[1] for columna in cursor.fetchall()]
    for columna in ("nombre", "apellido", "correo"):
        if columna not in columnas_pedido:
            cursor.execute(f"ALTER TABLE pedidos ADD COLUMN {columna} TEXT")
    # Solo carga el catálogo original si la tabla está vacía.
    # Si ya tienes productos en tu base de datos, no los borra ni los duplica.
    cursor.execute("SELECT COUNT(*) FROM productos")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO productos (nombre, descripcion, precio) VALUES (?, ?, ?)",
            PRODUCTOS_ORIGINALES
        )
    conexion.commit()
    conexion.close()

@aplicacion.route("/")
def inicio():
    preparar_base_datos()
    return render_template("tienda.html")

@aplicacion.route("/datos")
def datos():
    preparar_base_datos()
    conexion = sqlite3.connect(BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY id")
    productos = [dict(producto) for producto in cursor.fetchall()]
    conexion.close()
    return jsonify(productos)

@aplicacion.route("/insertapedido", methods=["POST"])
def insertapedido():
    preparar_base_datos()
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return jsonify({"ok": False, "mensaje": "Faltan los datos del cliente."}), 400

    cliente = datos.get("cliente", {})
    pedido = datos.get("productos", [])
    nombre = str(cliente.get("nombre", "")).strip()
    apellido = str(cliente.get("apellido", "")).strip()
    correo = str(cliente.get("correo", "")).strip()

    if not nombre or not apellido or not correo:
        return jsonify({"ok": False, "mensaje": "Completa nombre, apellido y correo."}), 400
    if "@" not in correo or "." not in correo.rsplit("@", 1)[-1]:
        return jsonify({"ok": False, "mensaje": "Introduce un correo electrónico válido."}), 400
    if not isinstance(pedido, list) or not pedido:
        return jsonify({"ok": False, "mensaje": "El carrito está vacío."}), 400

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numero_pedido = "PED-" + datetime.now().strftime("%Y%m%d%H%M%S%f")

    conexion = None
    try:
        conexion = sqlite3.connect(BASE_DATOS, timeout=10)
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO pedidos (numerodepedido, fecha, carga, nombre, apellido, correo) VALUES (?, ?, ?, ?, ?, ?)",
            (numero_pedido, fecha, json.dumps(pedido, ensure_ascii=False), nombre, apellido, correo)
        )
        conexion.commit()
        return jsonify({"ok": True, "mensaje": "Pedido guardado correctamente", "numero": numero_pedido})
    except sqlite3.Error:
        if conexion:
            conexion.rollback()
        aplicacion.logger.exception("No se pudo guardar el pedido en SQLite")
        return jsonify({"ok": False, "mensaje": "No se pudo guardar el pedido en SQLite. Revisa el error que aparece en la terminal."}), 500
    finally:
        if conexion:
            conexion.close()

@aplicacion.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        contrasena = request.form.get("contrasena", "")
        if usuario == USUARIO_ADMIN and contrasena == CONTRASENA_ADMIN:
            session["admin_autenticado"] = True
            return redirect(url_for("admin"))
        error = "Usuario o contraseña incorrectos."
    return render_template("login.html", error=error)

@aplicacion.route("/logout")
def logout():
    session.pop("admin_autenticado", None)
    return redirect(url_for("login"))

@aplicacion.route("/admin")
def admin():
    if not session.get("admin_autenticado"):
        return redirect(url_for("login"))
    preparar_base_datos()
    conexion = sqlite3.connect(BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT id, numerodepedido, fecha, carga, nombre, apellido, correo FROM pedidos ORDER BY id DESC")
    pedidos = [dict(p) for p in cursor.fetchall()]
    conexion.close()

    for pedido in pedidos:
        try:
            productos = json.loads(pedido.get("carga") or "[]")
            if not isinstance(productos, list):
                productos = []
        except (json.JSONDecodeError, TypeError):
            productos = []
        pedido["productos"] = productos
        pedido["total"] = sum(float(p.get("precio", 0)) for p in productos)
        pedido["cantidad"] = len(productos)

    return render_template("admin.html", pedidos=pedidos,
                           total_pedidos=len(pedidos),
                           total_ventas=sum(p["total"] for p in pedidos))

if __name__ == "__main__":
    preparar_base_datos()
    aplicacion.run(debug=True)
