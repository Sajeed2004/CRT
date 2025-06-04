create database expenses_tracker;
use expenses_tracker;
create table expenses(
	serial_num int primary key,
    category varchar(500),
    item varchar(500),
    cost varchar(100)
    );