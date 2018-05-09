#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    
                     user="root",         
                     passwd="root",      
                     db="sunil")
cursor = db.cursor()

name = raw_input("enter the name of person to display data : ")
cursor.execute("SELECT * FROM userdata2 where user_name like '%"+name+"%';")
data = cursor.fetchall()
if  data== None:
	print "Not Valid User"
else:
	print data
