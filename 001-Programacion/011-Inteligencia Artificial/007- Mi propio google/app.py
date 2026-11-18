from flask import Flask, render_template, request
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
aplicacion = Flask(__name__)
DB = BASE / 'jocarsa-buscador.db'

@aplicacion.route('/')
def inicio():
    return render_template('buscador.html')

@aplicacion.route('/buscar', methods=['GET', 'POST'])
def buscar():
    consulta = request.values.get('busca', '').strip()
    resultados = []
    if consulta:
        palabras = consulta.split()[:10]
        # Todas las palabras deben aparecer en al menos uno de los campos.
        condiciones = []
        parametros = []
        for palabra in palabras:
            condiciones.append('(' + ' OR '.join("LOWER(COALESCE(" + campo + ", '')) LIKE ?" for campo in ('titulo', 'descripcion', 'descripcionia', 'url')) + ')')
            parametros.extend(['%' + palabra.lower() + '%'] * 4)
        sql = f'''SELECT url, titulo, descripcion, descripcionia
                  FROM paginas
                  WHERE {' AND '.join(condiciones)}
                  ORDER BY
                    CASE WHEN LOWER(COALESCE(titulo,'')) LIKE ? THEN 0 ELSE 1 END,
                    CASE WHEN LOWER(COALESCE(descripcion,'')) LIKE ? THEN 0 ELSE 1 END,
                    CASE WHEN LOWER(COALESCE(descripcionia,'')) LIKE ? THEN 0 ELSE 1 END,
                    titulo COLLATE NOCASE
                  LIMIT 100'''
        patron = '%' + consulta.lower() + '%'
        with sqlite3.connect(DB) as conexion:
            conexion.row_factory = sqlite3.Row
            resultados = [dict(fila) for fila in conexion.execute(sql, parametros + [patron] * 3)]
    return render_template('resultados.html', busca=consulta, resultados=resultados)

if __name__ == '__main__':
    aplicacion.run(debug=True)

