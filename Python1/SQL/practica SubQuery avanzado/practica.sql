create database Subquery;
use Subquery;
drop database Subquery;
-- Asumiendo que contamos con una tabla llamada estudiantes con las columnas: id (int), nombre
-- (varchar), calificacion (int) y aprobado (boolean - con false como valor default)
create table estudiantes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    calificacion INT,
    aprobado BOOLEAN DEFAULT FALSE
);

insert into estudiantes(nombre, calificacion)
    VALUES ('Messi  ', 85),
    ('Scam', 90),
    ('Glory ', 75),
    ('Stake ', 60),
    ('Dance 5', 80);

-- Crear una vista que muestre la información de los estudiantes que aprobaron el examen final
-- con una calificación superior a 80.
create view Calificacion_superior as 
select * from estudiantes
where estudiantes.calificacion > 80


-- Crear un stored procedure que recibe como parámetros el id y nuevo_nombre de un
-- estudiante y actualice su información de nombre en la tabla de estudiantes.
create procedure Actualizar_estudiantes(id int , nuevo_nombre VARCHAR(50))
begin 
    UPDATE estudiantes
    SET nombre = nuevo_nombre
    WHERE estudiantes.id = id;
end;
CALL actualizar_estudiantes(1,"Derek");
-- Crear un trigger que se active después de cambiar la calificación de un estudiante y la
-- columna aprobado con un valor de true únicamente si el valor de calificacion es mayor a
-- 80.

DELIMITER //
CREATE TRIGGER ChangeState
BEFORE UPDATE ON estudiantes
FOR EACH ROW
BEGIN
    if New.calificacion > 80 THEN
        set New.aprobado = True;
    End IF; 
END //
DELIMITER;
-- Nota: Incluir comentarios en el SQL que expliquen lo que está haciendo cada parte del código.