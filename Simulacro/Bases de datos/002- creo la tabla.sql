CREATE TABLE publicaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    plataforma VARCHAR(50) NOT NULL,
    tipo_contenido VARCHAR(50),
    descripcion TEXT,
    fecha_publicacion DATE,
    estado VARCHAR(30),
    presupuesto DECIMAL(10,2),
    enlace VARCHAR(255)
);
