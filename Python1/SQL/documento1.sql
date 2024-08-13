create database clase default character set = 'utf8mb4';
drop database clase;
use clase;
create table estudiante(
    id int primary key auto_increment,
    names varchar(50) not null,
    edad varchar(50) not null
);
alter table estudiante add column apellido varchar(50) not null;
alter table estudiante modify column edad int;
alter table estudiante change column names name varchar(50) not null;
alter table estudiante drop column edad;
drop table estudiante;
insert into estudiante (name, apellido) values ('Wilfredo', 'Aguilar');
insert into estudiante (apellido, name) values ('Moreno', 'Franco');
insert into estudiante values 'Monica', 'Barrios';
select * from estudiante;
select * from estudiante where name = 'Wilfredo';
select * from estudiante where not name = 'Franco';
select * from estudiante order by name asc;
select * from estudiante order by name desc;

update estudiante set name = 'Keylor', apellido = 'Navas' where name = 'Wilfredo';

delete from estudiante where name = 'Keylor';