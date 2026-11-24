import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="examenbasesdedatos",
  password="Simulacrobasesdedatos12$",
  database="biblioteca20261123"
)

cursor = connection.cursor()                        
cursor.execute("SELECT * FROM libros")

libros = cursor.fetchall()
print(libros)

cursor.close()
connection.close()

    
