import mysql.connector

mysql = mysql.connector.connect(host="localhost",user="",passwd="",database="Databasse_name")

mycursor = mydb.cursor()

mycursor.execute("select * from Databasse_name")

# result = mycursor.fetchall()
result = mycursor.fetchone()

for i in result:
    print(i)

