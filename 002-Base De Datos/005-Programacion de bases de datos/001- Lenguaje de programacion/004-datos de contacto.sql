CREATE TABLE datos_contacto(
	id INT PRIMARY KEY AUTO_INCREMENT,
  id_usuario INT,
  email VARCHAR(100),
  telefono VARCHAR(100)
);

INSERT INTO datos_contacto VALUES(
	NULL,
  1,
  'vr261112@gmail.com',
  '663129339'
);

SELECT * FROM datos_contacto;
