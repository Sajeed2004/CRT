# You are using MYSQL
create table sales
(
    product_id int,
    product_name varchar(100),
    quantity int,
    category varchar(200)
);

insert into sales(product_id,product_name,quantity,category) value(1,"fridge",2,"electronic");
insert into sales(product_id,product_name,quantity,category) value(2,"wc",1,"electronic");
insert into sales(product_id,product_name,quantity,category) value(3,"computer",3,"electronic");
insert into sales(product_id,product_name,quantity,category) value(4,"tv",1,"electronic");
insert into sales(product_id,product_name,quantity,category) value(5,"door",4,"wooden");
insert into sales(product_id,product_name,quantity,category) value(6,"chair",5,"wooden");


select * from sales;