para practicar

CREATE DATABASE tratamiento;

USE tratamiento;

CREATE TABLE usuarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100),
   usuario VARCHAR(100),
   seguidores VARCHAR(100)
);

DESCRIBE usuarios;

SELECT * FROM usuarios; 
