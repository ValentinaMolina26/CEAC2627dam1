CREATE USER 'examenbasesdedatos'@'localhost' IDENTIFIED BY 'Simulacrobasesdedatos12$';

GRANT USAGE ON *.* TO 'examendamceac2026'@'localhost';

ALTER USER 'examenbasesdedatos'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON biblioteca20261123.* 
TO 'examenbasesdedatos'@'localhost';

FLUSH PRIVILEGES;
