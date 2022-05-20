import pymysql.cursors , pymysql.err
import sys

test_str = "SELECT * FROM orders_from"
	
try:
	conn = pymysql.connect(host='mysql.freehostia.com',user = 'serkal42_walls', password='crybabycry',db='serkal42_walls',cursorclass=pymysql.cursors.SSCursor)
	with conn.cursor() as cursor:
		print ("connect successful!!")
		conn.autocommit(True)
		cursor.execute(test_str)
		for row in cursor:
			print(row)




except pymysql.err.OperationalError as e:
	print(e)
