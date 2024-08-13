-- Práctica 1 - Manipulación de tablas
-- Crear una tabla llamada ‘Estudiantes’ con las siguientes columnas

-- IdEstudiante:
-- Debe ser el PRIMARY KEY de la tabla
-- Debe almacenar un número entero
-- No puede ser “null” (esta columna no puede estar vacía en la tabla)
-- Debe se autoincrementable
-- Nombre:
-- Debe almacenar información como texto
-- Test:
-- Debe almacenar información como texto
-- Editar la tabla ‘Estudiantes’ para
-- Agregar una columna nueva llamada ‘Edad’ que almacenará un número entero
-- Renombrar columna ‘Test’ y poner el nombre de ‘Apellidos’
-- Eliminar tabla ‘Estudiantes’
USE clase;
create Table estudiantes(
    id int PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) not NULL,
    Test VARCHAR(50) not null,
);
ALTER Table estudiantes add COLUMN Edad INT;
ALTER Table estudiantes change COLUMN Test Apellido VARCHAR(50) not null;