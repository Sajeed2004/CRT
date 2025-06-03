# You are using MYSQL
create table student
(
    id int,
    name varchar(100),
    age int,
    email varchar(200)
);

insert into student(id,name,age,email) value(2,"sajeed",20,"abc@email");
insert into student(id,name,age,email) value(1,"umesh",30,"djw@email");
select * from student;