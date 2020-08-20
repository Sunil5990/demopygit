import mysql.connector

conn = mysql.connector.connect(host="localhost",user="Sunil",passwd="1234",database='PythonClass')
mycurser = conn.cursor()

#sql="insert into student values ('Tarun','JNV hathras')"
#mycurser.execute(sql)
#conn.commit()

#sql="delete from student where name='Tarun'"
#mycurser.execute(sql)
#conn.commit()
sql="Select * from student"
mycurser.execute(sql)
#result = mycurser.fetchall()  #Fetchall() for all records, fetchone() for 1 record

for i in mycurser:
	print (i)