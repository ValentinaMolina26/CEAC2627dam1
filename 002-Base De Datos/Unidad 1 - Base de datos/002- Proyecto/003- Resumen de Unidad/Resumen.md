# Resumen de la Unidad 1 

En esta unidad aprendimos los conceptos básicos relacionados con el almacenamiento y la gestión de la información, como los ficheros y los sistemas gestores de bases de datos

#1. Tipos de ficheros

Primero trabajamos con diferentes tipos de ficheros para almacenar información

Los ficheros planos , como los archivos ".txt", permiten guardar información de una forma mas sencilla. Por ejemplo, podemos guardar una lista de nombres o una agenda con nombres y teléfonos. son fáciles de crear y leer, pero tienen el problema de que (no tienen una estructura definida). Esto puede provocar problemas cuando los datos contienen espacios o cuando necesitamos separar correctamente cada dato.

Después hemos visto los archivos CSV (Comma-Separated Values). Estos archivos tienen una estructura más organizada, ya que los datos se separan normalmente mediante comas. como en el ejemplo:

id,nombre,telefono,email

Con esta estructura podemos organizar los datos en registros y columnas. También aprendimos la importancia de utilizar un identificador único, ya que cada registro debe poder diferenciarse de los demás.

# 2. Bases de datos organizadas en carpetas

También vimos cómo podemos organizar una pequeña base de datos utilizando carpetas y archivos CSV.

Como ejemplo, podemos tener diferentes empresas y dentro de cada una guardar sus datos:

Empresa 1

 -clientes.csv
 -productos.csv
 
Empresa 2

  -clientes.csv
  -productos.csv

Asi cada archivo puede representar una tabla con información diferente. En los ejemplos que vimos en clase utilizamos datos de clientes, como nombre, apellidos, email, teléfono y ciudad, y datos de productos, como nombre, categoría, precio y stock.

Esta organización permite trabajar con una cantidad mayor de información de una manera más ordenada.

# 3. Sistemas gestores de bases de datos

Cuando las bases de datos son más grandes o necesitan ser utilizadas por varias personas, podemos utilizar un Sistema Gestor de Bases de Datos (SGBD).

Un SGBD es un programa que se encarga de gestionar y proteger los datos. En lugar de trabajar directamente con la base de datos, hacemos peticiones al sistema gestor y este decide cómo acceder a la información.

Sus funciones son:

-Proteger los datos.
-Controlar quién puede acceder.
-Gestionar la información.
-Mejorar el rendimiento de las consultas.
-Permitir que varios usuarios trabajen con los datos.

También vimos el problema de la (concurrencia), que pasa cuando varios usuarios intentan modificar o escribir información al mismo tiempo. El sistema gestor organiza estos accesos para evitar problemas con los datos.

# 4. SQL

Para comunicarnos con una base de datos necesitamos utilizar un lenguaje de consultas. El lenguaje más utilizado es SQL, que permite realizar peticiones y buscar información dentro de las bases de datos

# 5. Instalación de MySQL

Por ultimo aprendidos a instalar un sistema gestor de bases de datos utilizando MySQL en Ubuntu

Primero debemos actualizar los paquetes del sistema con:

# sudo apt update

Después instalamos MySQL Server con:

# sudo apt install mysql-server

El comando utiliza (sudo) para ejecutar la acción con permisos de administrador, (apt) como gestor de paquetes e (install) para indicar que queremos instalar un paquete.

Después de instalarlo, vimos la configuración inicial mediante:

# sudo mysql_secure_installation

Y finalmente podemos acceder a MySQL utilizando:

# sudo mysql -u root -p

Con esto podemos comprobar que MySQL está instalado y preparado para empezar a trabajar con bases de datos.


