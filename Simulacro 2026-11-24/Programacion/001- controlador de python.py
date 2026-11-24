import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="videoteca20261124",
  password="CEAC2627DAm123$$",
  database="videoteca20261124"
)

cursor = connection.cursor()                        
cursor.execute("SELECT * FROM peliculas")

peliculas = cursor.fetchall()
print(peliculas)

cursor.close()
connection.close()

