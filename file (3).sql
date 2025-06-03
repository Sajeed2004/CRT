# You are using MYSQL
create table sales
(
    product_id int,
    product_name varchar(100),
    quantity int,
    category varchar(200)
);
insert into sales(product_id,product_name,quantity,category) 
value
(1,"fridge",2,"electronic"),
(2,"wc",1,"electronic"),
(3,"computer",3,"electronic"),
(4,"tv",1,"electronic"),
(5,"door",4,"wooden"),
(6,"chair",5,"wooden");

UPDATE sales
SET quantity=20
WHERE category='electronic';


SELECT*
from sales;
