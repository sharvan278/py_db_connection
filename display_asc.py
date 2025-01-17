import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"

)

mycursor=mydb.cursor()

mycursor.execute("select *from product1 order by pname asc")
products = mycursor.fetchall()

for p in products:
    print(p)
