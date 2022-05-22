import pymysql.cursors , pymysql.err
import sys

test_str = "SELECT * FROM orders_from"
conn = pymysql.connect(host='mysql.freehostia.com',user = 'serkal42_walls', password='crybabycry',db='serkal42_walls',cursorclass=pymysql.cursors.SSCursor)


class database_obj:
	obj_list = list()
	"""docstring for database_obj"""
	def __init__(self, dictonary):
		self.dictonary = dictonary
		obj_list.append(self.dictonary)
		


orders = (
"id",
"customer",
"find_field"
)

#что то лишнее
items = (
"id",
"customer_id",
"title", 
)

organization_status = (
"id",
"status"
)


organization = (
"id",
"order_id",
"organization_title" ,
"organization_field",
"organization_status",
"site",
"country" ,
"city"
)
print(len(organization))

contact_person_post = (
"id",
"place"
)




contact_database = (
"id",
"organization_id",
"order_id" ,
"name",
"place_id" ,
"number",
"email",
"status_id"
)

def add_item(customer_id,item):
	try:
		with conn.cursor() as cursor:
			conn.autocommit(True)
			print("connect")
			add_item = f"insert into items({items[1]},{items[2]})VALUES(%s,%s)"
			print(add_item)
			cursor.execute(add_item,(str(customer_id),item))
	except pymysql.err.OperationalError as e:
		print(e)

def add_organization(org_str,organization_title,organization_field,city,site,organization_status="1",country="RU",order_id="1"):
	try:
		with conn.cursor() as cursor:
			conn.autocommit(True)

			add_org = f"insert into organization({org_str}) VALUES(%s,%s,%s,%s,%s,%s,%s)"
			print(add_org)
			cursor.execute(add_org,(order_id,organization_title,organization_field,organization_status,country,site,city))
			print(add_org)
	except pymysql.err.OperationalError as e:
		print(e)
			
	print(order_id,organization_title,organization_field,organization_status,country,city)


def add_contact(contact_str ,name,place_id ,number,email,order_id = "1",organization_id="2",status_id="1"):
	print(organization_id,order_id,name,place_id,number,email,status_id)

	with conn.cursor() as cursor:
		conn.autocommit(True)

		add_con = f"insert into contact_database({contact_str}) VALUES(%s,%s,%s,%s,%s,%s,%s)"
		print(add_con)
		cursor.execute(add_con,(str(organization_id), str(order_id), name,str(place_id),number,email,str(status_id)))
		#cursor.execute(add_contact,(order_id,organization_title,organization_field,organization_status,country,site,city))

org_str = ",".join(organization[1:8])
print(org_str)
#add_organization(org_str,input("Enter organization title:\n"),input("ENter organization field:\n"),input("ENter site:\n"),input("ENter CITY"))

contact_str = ",".join(contact_database[1:8])
print(contact_str)
print(contact_database[1:8])
#add_contact(contact_str, "Илья Маковецкий","3","8 800 333-96-05","management-msk@elevel.ru")
#add_contact(contact_str, "Наталья Кудрик","3","8 800 333-96-05","management-spb@elevel.ru")
add_contact(contact_str, input("Enter name:\n"),"3",input("Enter phone:\n"),input("ENter email:\n"))
'''
SELECT items.title, orders_from.customer,orders_from.find_field  
FROM orders_from, items 
WHERE orders_from.id = items.customer_id ;
'''
#add_item("1","world")
temp_list = list()

try:
	conn = pymysql.connect(host='mysql.freehostia.com',user = 'serkal42_walls', password='crybabycry',db='serkal42_walls',cursorclass=pymysql.cursors.SSCursor)
	with conn.cursor() as cursor:
		print ("connect successful!!")
		conn.autocommit(True)
		cursor.execute(test_str)
		for row in cursor:
			temp_list.append(dict(zip(orders, row)))
			print(temp_list)
#
#		for values in temp_list:
#			new_dict = dict(zip(orders, temp_list))
#			print(new_dict)


except pymysql.err.OperationalError as e:
	print(e)
