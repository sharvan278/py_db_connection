import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"

)

mycursor=mydb.cursor()
id = input("enter product id ")
mycursor.execute("delete from product1 where pid=%s",(id,))

mydb.commit()