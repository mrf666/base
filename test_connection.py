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
"id"
"order_id"
"organization_title" 
"organization_field"
"organization_status"
"country" 
"city"
)


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

'''
SELECT items.title, orders_from.customer,orders_from.find_field  
FROM orders_from, items 
WHERE orders_from.id = items.customer_id ;
'''
add_item("1","world")
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
