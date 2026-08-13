create table productos (
 id serial PRIMARY KEY,
 nombre varchar(100),
 precio decimal(10,2),
 stock integer
);

insert into productos (nombre,precio,stock)
values
('Laptop', 2500, 10),
('Mouse', 50, 30),
('Teclado', 120, 20),
('Monitor', 800, 15),
('Impresora', 650, 8);

select * from productos;