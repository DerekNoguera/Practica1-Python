# INNER JOIN

# Se utiliza para combinar filas o registros de dos o más tablas en base a una columna que relaciona
# estas tablas.

# Retorna resultados de valores presentes en ambas tablas

# Sintaxis:
# SELECT Tabla1.columna1, Tabla2.columna1, ..
# FROM Tabla1
# INNER JOIN Tabla2 ON Tabla1.columnaId = Tabla2.columnaIdDeTabla1;

# Ejemplo:
# SELECT Estudiantes.nombre, Calificaciones.calificacion
# FROM Estudiantes
# INNER JOIN Calificaciones
# ON Estudiantes.estudianteId = Calificaciones.estudianteId;
# INNER JOIN

# Resultado:
# Listamos únicamente a los estudiantes que tengan una calificación asociada a ellos
# Se utiliza para combinar TODOS los registros de la primera tabla (tabla de la izquierda) con los
# registros de la tabla de la derecha que coincidan en base a una columna que relaciona estas tablas.

# Sintaxis:
# SELECT ...
# FROM Tabla1
# LEFT JOIN Tabla2 ON Tabla1.columnaId = Tabla2.columnaIdDeTabla1;

# Ejemplo:
# SELECT Estudiantes.nombre, Clases.nombreClase
# FROM Estudiantes
# LEFT JOIN Clases ON Estudiantes.estudianteId = Clases.estudianteId;
# LEFT (OUTER) JOIN
# LEFT (OUTER) JOIN

# Resultado:

# Listamos a todos los estudiantes presentes en la tabla Estudiantes a pesar de que no todos
# estén inscritos a una clase. Para esos estudiantes, el valor en la columna “nombreClase” será
# NULL
# RIGHT (OUTER) JOIN
# Se utiliza para combinar TODOS los registros de la segunda tabla (tabla de la derecha) con los
# registros de la tabla de la izquierda que coincidan en base a una columna que relaciona estas
# tablas.

# Sintaxis:
# SELECT ...
# FROM Tabla1
# RIGHT JOIN Tabla2 ON Tabla1.columnaId = Tabla2.columnaIdDeTabla1;

# Ejemplo:
# SELECT Estudiantes.nombre, Calificaciones.calificacion
# FROM Estudiantes
# RIGHT JOIN Calificaciones ON Estudiantes.estudianteId = Calificaciones.estudianteId;
# RIGHT (OUTER) JOIN

# Resultado:
# Resultado: Listamos a todos los estudiantes presentes en la tabla Estudiantes a pesar de que
# no todos estén inscritos a una clase. Para esos estudiantes, el valor en la columna
# “nombreClase” será NULL.
# FULL (OUTER) JOIN

# Se utiliza para obtener TODOS los registros tanto de la primera como de la segunda tabla cuando
# sea que coincidan una de las columnas que relacionan a estas tablas.

# Sintaxis:
# SELECT Tabla1.columna1, Tabla2.columna1, ...
# FROM Tabla1
# FULL JOIN Tabla2 ON Tabla1.columnaId = Tabla2.columnaIdDeTabla1;

# Ejemplos:
# SELECT Estudiantes.nombre, Calificaciones.calificacion
# FROM Estudiantes
# FULL JOIN Calificaciones ON Estudiantes.estudianteId = Calificaciones.estudianteId;
# FULL (OUTER) JOIN

# Resultado:
# Resultado: Listamos a todos los estudiantes presentes en la tabla Estudiantes a pesar de que
# no todos estén inscritos a una clase Y todas las clases a pesar de que no tenga estudiantes.
# Para casos donde no haga match, el valor en la tabla de resultados será NULL.
# Hay motores de bases de datos que no soportan el FULL JOIN, como por ejemplo MySQL.
# Para estos casos se puede “emular” un FULL JOIN de la siguiente manera

# Ejemplo:
# SELECT Estudiantes.nombre, Clases.nombreClase
# FROM Estudiantes
# LEFT JOIN Clases ON Estudiantes.estudianteId = Clases.estudianteId
# UNION
# SELECT Estudiantes.nombre, Clases.nombreClase
# FROM Estudiantes
# RIGHT JOIN Clases ON Estudiantes.estudianteId = Clases.estudianteId
# WHERE Estudiantes.estudianteId IS NULL;

# Nota:

# UNION nos ayuda a remover duplicados y el WHERE a incluir registros que no
# coincidieran en el resultado del LEFT JOIN
# FULL (OUTER) JOIN
# ORDER BY
# Se utiliza para ordenar el registros o el set de resultados de forma ascendente o descendente

# Sintaxis:
# SELECT columnas
# FROM Tabla
# ORDER BY columna(s) ASC | DESC;

# Ejemplos:
# SELECT *
# FROM Calificaciones
# ORDER BY calificacion ASC;
# SELECT *
# FROM Calificaciones
# ORDER BY calificacion DESC;
# GROUP BY
# Se utiliza para agrupar registros que tienen el mismo valor en uno columna o varias columnas

# Sintaxis:
# SELECT columnas
# FROM Tabla
# WHERE condición ---> el WHERE sería opcional
# GROUP BY columna(s);

# Ejemplo:
# SELECT COUNT(id) AS 'Cantidad Calificaciones Iguales', calificacion
# FROM Calificaciones
# GROUP BY calificacion;
# HAVING
# Se utiliza para filtrar registros que son retornados basados en una condición. Es muy similar a
# WHERE pero lo que los distingue es que WHERE filtra registros individuales antes de que sean
# agrupados y retornados, HAVING filtra grupos de registros después de que han sido agrupados y
# agregados.

# Sintaxis:
# SELECT columnas
# FROM Tabla
# WHERE condición (opcional)
# GROUP BY columna(s)
# HAVING condición
# ORDER BY columna(s) (opcional);

# Ejemplo:
# SELECT COUNT(id) as 'Cantidad Calificaciones Iguales', calificacion
# FROM Calificaciones
# GROUP BY calificacion;
# HAVING

# Ejemplo:

# Obtener estudiantes con edad mayor a 18 pero donde el grupo de estudiantes sea mayor a 1
# SELECT COUNT(edad) AS 'Cantidad Estudiantes', edad
# FROM Estudiantes
# WHERE edad > 18
# GROUP BY edad
# HAVING COUNT(*) > 1;
# UNION
# Se utiliza para combinar registros de dos result-set (dos o más tablas de resultados de SELECTs)
# Para usar UNION es necesario que:
# Que cada SELECT retorne la misma cantidad de columnas
# Columnas deben de tener tipos de datos similares

# Las columnas en el SELECT deben de estar en el mismo orden
# Sintaxis:
# SELECT columnas FROM Tabla1
# UNION
# SELECT columnas FROM Tabla2;

# Ejemplo:
# SELECT Estudiantes.estudianteId, Estudiantes.nombre
# FROM Estudiantes
# UNION
# SELECT Calificaciones.estudianteId, Calificaciones.calificacion FROM Calificaciones;
# INTERSECT
# Se utiliza para encontrar valores que se encuentran en dos tablas

# Para usar INTERSECT es necesario que:
# Que cada SELECT tenga la misma cantidad de columnas
# Columnas deben de tener tipos de datos similares

# Sintaxis:
# SELECT columnas FROM Tabla1
# INTERSECT
# SELECT columnas FROM Tabla2;

# Ejemplo:
# Obtener nombre de los estudiantes top (usar tabla Estudiantes y EstudiantesTop)
# SELECT Estudiantes.nombre FROM Estudiantes
# INTERSECT
# SELECT EstudiantesTop.nombre FROM EstudiantesTop;
# Se utiliza para probar si un subquery retorna algún registro.

# Sintaxis:
# SELECT * FROM Tabla1 t
# WHERE EXISTS (SELECT 1 FROM Tabla2 t2 WHERE t2.colId1 = t1.colId1);

# Ejemplo:
# Verificar si un estudiante ya realizó la matrícula
# SELECT * FROM Estudiantes e
# WHERE EXISTS (
# SELECT 1
# FROM Matriculas m
# WHERE m.estudianteId = e.estudianteId);

# EXISTS
# Se utiliza para probar si un subquery no retorna algún registro.

# Sintaxis:
# SELECT * FROM Tabla1 t
# WHERE NOT EXISTS (SELECT * FROM Tabla2 t2 WHERE t2.colId1 = t1.colId1);

# Ejemplo:
# Obtener los estudiantes que no han realizado la matrícula aún
# SELECT * FROM Estudiantes e
# WHERE NOT EXISTS (
# SELECT *
# FROM Matriculas m
# WHERE m.estudianteId = e.estudianteId);
# NOT EXISTS

# Se utiliza seguido de WHERE para realizar una búsqueda basada en un patrón en una columna.

# Sintaxis:
# SELECT columnas
# FROM Tabla
# WHERE columna LIKE patrón;
# El patrón puede tener uno de los siguientes símbolos
# Porcentaje (%): representa 0, 1 o varios caracteres
# Guión bajo ( _ ): representa un sólo caracter
# Lista completa: https://www.w3schools.com/sql/sql_wildcards.asp
# LIKE
# Ejemplos:

# Obtener los estudiantes con nombre que inicie con ‘a’
# SELECT * FROM Estudiantes WHERE nombre LIKE ‘a%’;

# Obtener los estudiantes con nombre que termine con ‘a’
# SELECT * FROM Estudiantes WHERE nombre LIKE ‘%a’;

# Obtener los estudiantes con nombre que tenga ‘na’ en cualquier posición
# SELECT * FROM Estudiantes WHERE nombre LIKE ‘%na%’;

# Obtener los estudiantes con nombre que tenga ‘n’ en la segunda posición
# SELECT * FROM Estudiantes WHERE nombre LIKE ‘_n%’;

# Obtener los estudiantes con nombre que inicie con ‘a’ y tenga al menos 2 caracteres de largo
# SELECT * FROM Estudiantes WHERE nombre LIKE ‘a_%’;

# Obtener los estudiantes con nombre que inicie con ‘a’ y termine con ‘o’
# SELECT * FROM Estudiantes WHERE nombre LIKE ‘a%o’;

# LIKE

# Lista de funciones útiles en los SELECT
# COUNT: Retorna cantidad de registros de la tabla de resultados que cumplen con la
# condición

# SELECT COUNT(columna) FROM Tabla WHERE condición;
# AVG: Retorna el valor promedio de una columna donde el tipo de dato sea numérico

# SELECT AVG(columna) FROM Tabla WHERE condición;
# SUM: Retorna la suma total del valor una una columna donde el tipo de dato sea numérico

# SELECT SUM(columna) FROM Tabla WHERE condición;
# MIN: Retorna el valor mínimo en la columna seleccionada

# SELECT MIN(columna) FROM Tabla WHERE condición;
# MAX: Retorna el valor máximo en la columna seleccionada

# SELECT MAX(columna) FROM Tabla WHERE condición;
# TOP o LIMIT: Retorna sólo la cantidad de registros indicados (depende del motor de base
# de datos se usa uno o el otro)
# SELECT TOP número | porcentaje columna(s) FROM Tabla WHERE condición;