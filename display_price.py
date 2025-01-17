import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"

)

mycursor=mydb.cursor()
min = input("enter minimum amount ")
max = input("enter maximum amount ")
mycursor.execute(f"select *from product1 where price between {min} and {max}")
products = mycursor.fetchall()

for p in products:
    print(p)
