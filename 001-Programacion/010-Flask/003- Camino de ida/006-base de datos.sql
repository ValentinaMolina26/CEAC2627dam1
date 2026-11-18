sudo mysql -u root -p

CREATE DATABASE caminodeida;

USE caminodeida;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100)
);

CREATE TABLE direccion(
	id INT PRIMARY KEY AUTO_INCREMENT,
  ciudad VARCHAR(100),
  pais VARCHAR(100),
  codigo_postal VARCHAR(100)
);

