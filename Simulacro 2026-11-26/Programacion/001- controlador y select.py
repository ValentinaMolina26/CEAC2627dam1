import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="vehículos20261125",
  password="Ceac2627DAM123$",
  database="vehículos20261125"
)

cursor = connection.cursor()                        
cursor.execute("SELECT * FROM vehiculos")

vehiculos = cursor.fetchall()
print(vehiculos)

cursor.close()
connection.close()

