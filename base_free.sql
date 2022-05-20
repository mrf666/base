DROP TABLE items;
DROP TABLE orders_from;
DROP TABLE organization;
DROP TABLE contact_database;

CREATE Table orders_from(
`id` int(5) auto_increment NOT NULL primary key,
`customer` varchar(100) NOT NULL,
`find_field` varchar(100) NOT NULL
);

CREATE TABLE items(
`id` int(5) auto_increment NOT NULL primary key,
`customer_id` int(5) NOT NULL,
`title` varchar(100) NOT NULL,
FOREIGN KEY(`customer_id`) REFERENCES orders_from(`id`)
);

CREATE TABLE organization(
`id` int(5) auto_increment NOT NULL primary key,
`item_id` int(5) NOT NULL,
`organization_title` varchar(100) NOT NULL,
`organization_field`varchar(100) NOT NULL,
`country` varchar(100) NOT NULL,
`city` varchar(20) NOT NULL,
FOREIGN KEY(`item_id`) REFERENCES items(`id`)
);


CREATE TABLE contact_database(
`id` int(5) auto_increment NOT NULL primary key,
`organization_id`int(5) NOT NULL,
`item_id` int(5) NOT NULL,
`number` varchar(25),
`email` varchar(25),
FOREIGN KEY(`organization_id`) REFERENCES organization(`id`),
FOREIGN KEY(`item_id`) REFERENCES items(`id`)
);


insert into `orders_from`(`customer`,`find_field`) VALUES ('Подшибники', 'Фирмы по электрощитовому оборудованию');
insert into `orders_from`(`customer`,`find_field`) VALUES ('Siemens','Склады и машиностроительные заводы');
insert into `orders_from`(`customer`,`find_field`) VALUES ('petrol, oil and lubricants','Пленочные производства');


insert into `items`(`customer_id`,`title`) VALUES(2,'Test');
insert into `items`(`customer_id`,`title`) VALUES(1,'Test');
insert into `items`(`customer_id`,`title`) VALUES(3,'Завод');


SELECT items.title, orders_from.customer,orders_from.find_field  
FROM orders_from, items 
WHERE orders_from.id = items.customer_id ;


select * from orders_from;
select * from items;
select * from contact_database;
