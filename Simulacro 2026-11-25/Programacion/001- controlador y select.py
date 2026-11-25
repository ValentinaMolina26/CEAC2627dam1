import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="videojuegos20261125",
  password="CEAC2627dam123$",
  database="videojuegos20261125"
)

cursor = connection.cursor()                        
cursor.execute("SELECT * FROM videojuegos")

videojuegos = cursor.fetchall()
print(videojuegos)

cursor.close()
connection.close()

