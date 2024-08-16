create database practicaDay16;
use practicaDay16;
-- drop DATABASE practicaDay16;
create Table Empleados(
id INTEGER PRIMARY KEY AUTO_INCREMENT not NULL,
nombre VARCHAR(50),
mesesTrabajados INT
);
create Table Salarios(
id INTEGER PRIMARY KEY AUTO_INCREMENT not NULL,
Salario INTEGER,
empleadoID INT
);
create Table VentasMesAnterior(
id INTEGER PRIMARY KEY AUTO_INCREMENT not NULL,
ventas INTEGER,
empleadoId INT
);
insert into empleados(nombre, mesesTrabajados)
 VALUES ('Juan Fernandez', 10),
 ('Calor Solis', 14),
 ('Ana Marin', 13),
 ('Luis Alfaro', 12);

insert into Salarios(Salario, empleadoId)
 VALUES (500, 1),
 (650,2),
 (400,3),
 (450,4);

insert into VentasMesAnterior(ventas, empleadoId)
 VALUES (20, 1),
 (60,2),
 (50,3),
 (45,4);

-- Cree un query para cada uno de los siguientes casos:
-- Una consulta SELECT donde obtenga la información de los empleados que hayan realizado
-- más de 50 ventas en el mes anterior

select * from empleados where id IN (select id from ventasmesanterior where ventasmesanterior.ventas > 50 )


-- Una consulta SELECT donde obtenga la información de los empleados que tengan un
-- salario menor a 500 dólares y lleven más de 12 meses trabajando

select * from empleados where id In (
    select `empleadoID` from salarios where salarios.Salario < 500 and empleados.`mesesTrabajados` > 12)

-- Un UPDATE en la tabla SALARIOS donde aumentemos el salario 100 dólares a aquellos
-- empleados que hayan trabajado más de 12 meses

UPDATE salarios set Salario = salario + 100 where id in (select id from empleados where empleados.`mesesTrabajados` > 12 )

-- Un DELETE en la tabla EMPLEADOS donde removamos a aquellos empleados cuyas
-- ventas hayan sido menores a 50
delete from empleados where id in(select id from ventasmesanterior where ventasmesanterior.ventas < 50);