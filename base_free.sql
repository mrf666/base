DROP TABLE items;
DROP TABLE orders_from;
DROP TABLE organization;
DROP TABLE contact_database;
DROP TABLE organization_status;
DROP TABLE contact_person_post;

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

CREATE TABLE organization_status(
`id` int(5) auto_increment NOT NULL primary key,
`status` varchar(12) NOT NULL
);


CREATE TABLE organization(
`id` int(5) auto_increment NOT NULL primary key,
`order_id` int(5) NOT NULL,
`organization_title` varchar(100) NOT NULL,
`organization_field`varchar(100) NOT NULL,
`organization_status` int(1) NOT NULL,
`country` varchar(100) NOT NULL,
`city` varchar(20) NOT NULL,
FOREIGN KEY(`order_id`) REFERENCES orders_from(`id`),
FOREIGN KEY(`organization_status`) REFERENCES organization_status(`id`)
);


CREATE TABLE contact_person_post(
`id` int(5) auto_increment NOT NULL primary key,
`place` varchar(30) NOT NULL
);

insert into contact_person_post(`place`) VALUES("Генеральный директор");
insert into contact_person_post(`place`) VALUES("Менеджер");
insert into contact_person_post(`place`) VALUES("Другое");


CREATE TABLE contact_status(
`id` int(5) auto_increment NOT NULL primary key,
`status` varchar(17) NOT NULL
);

insert into contact_status(`status`) VALUES("Холодный");
insert into contact_status(`status`) VALUES("Первичный контакт");
insert into contact_status(`status`) VALUES("Ожидает звонка");
insert into contact_status(`status`) VALUES("Ожидает КП");




CREATE TABLE contact_database(
`id` int(5) auto_increment NOT NULL primary key,
`organization_id`int(5) NOT NULL,
`order_id` int(5) NOT NULL,
`name` varchar(30) NOT NULL,
`place_id` int(5) NOT NULL,
`number` varchar(25),
`email` varchar(25),
`status_id` int(5),
FOREIGN KEY(`organization_id`) REFERENCES organization(`id`),
FOREIGN KEY(`order_id`) REFERENCES orders_from(`id`)
FOREIGN KEY(`place_id`) REFERENCES contact_person_post(`id`),
FOREIGN KEY(`status_id`) REFERENCES contact_status(`id`)
);

insert into `orders_from`(`customer`,`find_field`) VALUES ('Подшибники', 'Фирмы по электрощитовому оборудованию');
insert into `orders_from`(`customer`,`find_field`) VALUES ('Siemens','Склады и машиностроительные заводы');
insert into `orders_from`(`customer`,`find_field`) VALUES ('petrol, oil and lubricants','Пленочные производства');


insert into `organization_status`( `status`) VALUES('Неизвестно');
insert into `organization_status`( `status`) VALUES('Не работает');
insert into `organization_status`( `status`) VALUES('Работает');


insert into `items`(`customer_id`,`title`) VALUES(2,'Test');
insert into `items`(`customer_id`,`title`) VALUES(1,'Test');
insert into `items`(`customer_id`,`title`) VALUES(3,'Завод');


SELECT items.title, orders_from.customer,orders_from.find_field  
FROM orders_from, items 
WHERE orders_from.id = items.customer_id ;


select * from orders_from;
select * from items;
select * from contact_database;
