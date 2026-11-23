CREATE USER 'simulacrosocialhub'@'localhost' IDENTIFIED BY 'Simulacrosocialhub1$';

GRANT USAGE ON *.* TO 'simulacrosocialhub'@'localhost';

ALTER USER 'simulacrosocialhub'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON socialhub20261123.* 
TO 'simulacrosocialhub'@'localhost';

FLUSH PRIVILEGES;
