CREATE DATABASE modulo_asistencia;
USE modulo_asistencia;

CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(6) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    UNIQUE KEY unique_codigo (codigo)
);

CREATE TABLE asistencias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT NOT NULL,
    fecha DATE NOT NULL,
    asistio BOOLEAN NOT NULL DEFAULT 0,
    justificado BOOLEAN NOT NULL DEFAULT 0,

    CONSTRAINT fk_estudiante
        FOREIGN KEY (estudiante_id) 
        REFERENCES estudiantes(id)
        ON DELETE CASCADE -- para manejar integridad
        ON UPDATE CASCADE,

    UNIQUE KEY unique_asistencia (estudiante_id, fecha)
);
