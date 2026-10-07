-- Creo un usuario tiendaestetoscopios
CREATE USER 'subconsultas'@'localhost' IDENTIFIED BY 'Subconsultas123$';

-- A ese usuario le pemito acceder a todo en el servidor
GRANT USAGE ON *.* TO 'subconsultas'@'localhost';

-- A ese usuario le quito limites para que pueda hacer de todo
ALTER USER 'subconsultas'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- Garantizo privilegios al usuario en su base de datos
GRANT ALL PRIVILEGES ON subconsultas.* 
TO 'subconsultas'@'localhost';

-- Recargo la tabla de privilegios
FLUSH PRIVILEGES;

