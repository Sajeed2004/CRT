# You are using MYSQL
create table employee
(
    id int,
    name varchar(100),
    department varchar(150),
    salary int
);

insert into employee(id,name,department,salary) value(25,"sajeed","ece",59999);

select * from employee;