-- Usando la tabla de ejemplo presente en este sandbox:
-- https://codehs.com/sandbox/id/6116-6117-practica-2-KiZiC1
-- Inserte 5 Estudiantes en la tabla
-- Deben de tener edades distintas
-- Tome el primer estudiante de la tabla y cambie la edad
-- Elimine el estudiante donde el valor en la columna ‘IdEstudiante’ sea 3

INSERT into estudiantes(Nombre, Apellido, Edad) VALUES ("Alexa", "Alvarez", "22");
update estudiantes set `Edad` = 15 WHERE id = 1;
DELETE FROM estudiantes WHERE id = 2;