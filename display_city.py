import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"

)

mycursor=mydb.cursor()
city = input("enter city to get products ")

mycursor.execute("select *from product1 where city=%s",(city,))
products = mycursor.fetchall()

for p in products:
    print(p)
