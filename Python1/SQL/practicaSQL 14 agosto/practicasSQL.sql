create database Practica14Agosto;
use Practica14Agosto;
CREATE TABLE Students (
id INTEGER PRIMARY KEY AUTO_INCREMENT not NULL,
name VARCHAR(50),
grade INT
);

insert into Students (name, grade)
VALUES ("Juan", 85),
("María", 75),
("Pedro", 90),
("Ana", 95),
("Luis", 0),
("Rodrigo", 0),
("Marta", 90),
("Mario", 0),
("Alejandra", 85);

CREATE TABLE Courses(
    id INTEGER PRIMARY Key AUTO_INCREMENT not NULL,
    studentID INT,
    code Varchar(50)
);
insert into Courses(studentID, code)
Values(1,"ING001"),
(2, "INF002"),
(10,"ALM003"),
(3, "FIS004"),
(4, "MAT005"),
(8, "MNV006"),
(5, "MNV006");

CREATE TABLE Teachers (
id INTEGER PRIMARY KEY AUTO_INCREMENT not null,
name VARCHAR(50)
);
insert Into teachers(id, name)
Values(1,"Bryan"),
(2,"Arturo"),
(3,"Rodrigo"),
(4,"Raul"),
(5,"Alejandra"),
(6,"Roberto");

-- 1) Una consulta usando un INNER JOIN entre las tablas "Students" y "Courses" para obtener el
-- nombre del estudiante y el código del curso para todos los registros.
SELECT Students.name, courses.code
From Students
INNER JOIN courses
ON Students.id = courses.id;

-- 2) Una consulta usando un LEFT JOIN entre las tablas "Students" y "Courses" para saber cuales
-- estudiantes tienen ya una nota asignada. Se debe mostrar el nombre del estudiante, calificación y
-- el código del curso.
SELECT students.name, students.grade, courses.code
From students
LEFT JOIN courses ON students.id = courses.`studentID`;
-- 3) Una consulta usando un RIGHT JOIN entre las tablas "Students" y "Courses" para saber cuáles
-- cursos tiene estudiantes que ya no existen. Se debe mostrar el nombre del estudiante y el código
-- del curso.
SELECT students.name, courses.code FROM students
RIGHT JOIN courses ON students.id = courses.`studentID`

-- 4) Una consulta usando un GROUP BY y COUNT en la tabla "Students" para saber la cantidad
-- de estudiantes con la misma nota. Se debe mostrar la nota y la cantidad de estudiantes (se puede
-- poner nombre a la columna del resultado del count).

SELECT COUNT(id) AS "Misma nota cantidad", students.grade
from students
GROUP BY grade

-- 5) Una consulta usando HAVING, GROUP BY y COUNT en la tabla "Students" para saber la
-- cantidad de estudiantes con la misma nota pero donde sólo donde la cantidad de estudiantes sea
-- mayor a 1 . Se debe mostrar la nota y la cantidad de estudiantes (se puede poner nombre a la
-- columna del resultado del count).
SELECT COUNT(id) AS "Resultado del count", students.grade
from students
-- WHERE grade > 1
GROUP BY grade
HAVING COUNT(*) > 1;

-- 6) Una consulta usando UNION entre las tabla "Students" y "Teachers" para saber el nombre de
-- los profesores y estudiantes

SELECT students.id, students.name from students
UNION
SELECT teachers.id, teachers.name from teachers;

-- 7) Una consulta usando EXISTS entre las tabla "Students" y "Teachers" para obtener toda la
-- información de los estudiantes que tengan el mismo nombre que el de un profesor

SELECT * from students WHERE EXISTS(select 1 from teachers Where students.name= teachers.name)

-- 8) Una consulta usando NOT EXISTS entre las tabla "Students" y "Teachers" para obtener toda
-- la información de los estudiantes que no tengan el mismo nombre que el de un profesor
select * from students where not EXISTS (SELECT 1 from teachers where students.name = teachers.name)

-- 9) Una consulta usando LIKE en la tabla "Students" para obtener el nombre de los estudiantes
-- que inician con la letra ‘M’
select students.name from students
WHERE students.name LIKE "M%";

-- 10) Una consulta usando LIKE en la tabla "Students" para obtener el nombre de los estudiantes
-- que finalizan con la letra ‘o’
select students.name from students
where students.name Like '%o';

-- 11) Una consulta usando LIKE en la tabla "Teachers" para obtener el nombre de los profesores
-- que incian con la letra ‘R’ y finalizan con la letra ‘o’

select teachers.name from teachers
where teachers.name like 'R%o';

-- 12) Una consulta usando LIKE en la tabla "Students" para obtener el nombre de los estudiantes
-- que tengan ‘ar’ en su nombre

select students.name from students
where students.name like '%ar%';

-- 13) Una consulta en la tabla "Students" para obtener el promedio de las notas de los estudiantes

select AVG(grade) as promedio
from students;

-- 14) Una consulta en la tabla "Students" para obtener la cantidad total de estudiantes en la tabla

select count(students.name) from students;

-- 15) Una consulta en la tabla "Students" para obtener nota más alta de los estudiantes

select MAX(students.grade) from students;

-- 16) Una consulta en la tabla "Students" para obtener el estudiante con la nota más alta (mostrar
-- nombre y nota)
select name,grade
from students
where grade = (SELECT MAX(grade) from students);

-- 17) Una consulta en la tabla "Students" para obtener nota más baja de los estudiantes

select min(students.grade) from students

-- 18) Una consulta en la tabla "Students" para obtener el estudiante con la nota más baja (mostrar
-- nombre y nota)

select name,grade from students
where grade = (SELECT min(grade) from students)

-- 19) Una consulta en la tabla "Students" para obtener los 3 estudiantes con la nota más alta (usando
-- LIMIT)

select name,grade from students ORDER BY grade DESC LIMIT 3;

-- 20) Una consulta en la tabla "Students" para obtener los 3 estudiantes con la nota más baja (usando

select name,grade from students ORDER BY grade asc limit 3;


-- https://stackoverflow.com/questions/12759596/validate-email-addresses-in-mysql regexp