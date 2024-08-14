-- Haciendo uso de la tabla y datos de la Práctica 2, cree consultas SQL que hagan lo siguiente:
-- Seleccionar / Obtener la lista de todos los estudiantes de la tabla ‘Estudiantes’
-- Seleccionar únicamente Nombre y Edad de los estudiantes de la tabla ‘Estudiantes’
-- Seleccionar únicamente Nombre y Edad de los estudiantes de la tabla ‘Estudiantes’ pero
-- los resultados deben de estar ordenados de la persona de MAYOR edad a la de MENOR edad
-- Seleccionar únicamente Nombre y Edad de los estudiantes de la tabla ‘Estudiantes’ pero los resultados deben de estar ordenados de la persona de MENOR edad a la de MAYOR edad
-- Seleccionar únicamente Nombre y Apellidos de los estudiantes de la tabla ‘Estudiantes’
-- pero los resultados deben de estar ordenados por apellido de manera inversa al orden del

SELECT * FROM estudiantes;
SELECT estudiantes.Nombre, estudiantes.Edad from estudiantes;
SELECT estudiantes.Nombre, estudiantes.Edad from estudiantes ORDER BY Edad DESC;
SELECT estudiantes.Nombre, estudiantes.Apellido from estudiantes ORDER BY Apellido ASC;