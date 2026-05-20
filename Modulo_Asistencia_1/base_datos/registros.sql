INSERT INTO estudiantes (codigo, nombre, apellido) VALUES
('E00001', 'Juan', 'Pérez'),
('E00002', 'María', 'Gómez'),
('E00003', 'Carlos', 'Ramírez'),
('E00004', 'Lucía', 'Fernández'),
('E00005', 'Pedro', 'Sánchez'),
('E00006', 'Ana', 'Paula'),
('E00007', 'Luis', 'Vargas'),
('E00008', 'Sofía', 'Castro'),
('E00009', 'Diego', 'Rojas'),
('E00010', 'Elena', 'Mendoza');
-- ESTUDIANTES QUE NO ASISTIRAN
INSERT INTO estudiantes (codigo, nombre, apellido) VALUES
('E00011', 'Miguel', 'Torres'),
('E00012', 'Valeria', 'Quispe'),
('E00013', 'Jorge', 'Huamán'),
('E00014', 'Camila', 'Flores'),
('E00015', 'Andrés', 'Vega');




INSERT INTO asistencias (estudiante_id, fecha, asistio, justificado) VALUES
(1, '2026-05-01', 1, 0),
(2, '2026-05-01', 0, 1),
(3, '2026-05-01', 1, 0),
(4, '2026-05-01', 1, 0),
(5, '2026-05-01', 0, 0),
(6, '2026-05-01', 1, 0),
(7, '2026-05-01', 1, 0),
(8, '2026-05-01', 1, 0),
(9, '2026-05-01', 1, 0),
(10, '2026-05-01', 1, 0);
-- ESTUDIANTES QUE NO ASISTIERON;
INSERT INTO asistencias (estudiante_id, fecha, asistio, justificado) VALUES
(11, '2026-05-01', 0, 0),
(12, '2026-05-01', 0, 0),
(13, '2026-05-01', 0, 0),
(14, '2026-05-01', 0, 0),
(15, '2026-05-01', 0, 0);


INSERT INTO asistencias (estudiante_id, fecha, asistio, justificado) VALUES
(1, '2026-05-02', 1, 0),
(2, '2026-05-02', 0, 1),
(3, '2026-05-02', 1, 0),
(4, '2026-05-02', 1, 0),
(5, '2026-05-02', 0, 0),
(6, '2026-05-02', 1, 0),
(7, '2026-05-02', 1, 0),
(8, '2026-05-02', 1, 0),
(9, '2026-05-02', 1, 0),
(10, '2026-05-02', 1, 0);
-- ESTUDIANTES QUE NO ASISTIERON
INSERT INTO asistencias (estudiante_id, fecha, asistio, justificado) VALUES
(11, '2026-05-02', 0, 0),
(12, '2026-05-02', 0, 0),
(13, '2026-05-02', 0, 0),
(14, '2026-05-02', 0, 0),
(15, '2026-05-02', 0, 0);