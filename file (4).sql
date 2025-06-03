# You are using MYSQL
create database practice;
use practice;
create table student(
   roll_no int primary key,
   name varchar(150) not null,
   course_name varchar(100) not null,
   phone_no varchar(20) not null
);
   
create table details(
   roll_no int,
   address text,
   phone_no varchar(20) not null,
   foreign key (roll_no) references student(roll_no)
);   
ALTER TABLE student drop column phone_no;
insert into student(roll_no,name,course_name) values
(1,"a","aa"),
(2,"b","bb"),
(3,"c","cc"),
(4,"d","dd"),
(5,"e","ee");
select * from student;
insert into details(roll_no,address,phone_no) values
(5,"HX","123446677"),
(1,NULL,"111111111"),
(3,"HGF","6302771111"),
(4,"DEL","11111111111"),
(2,"HYD","8888888888");
select * from details;

select * from student
join details
on student.roll_no=details.roll_no;

select s.roll_no,s.name,s.course_name,d.phone_no
from student s
join details d
on s.roll_no=d.roll_no