import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"

)

mycursor=mydb.cursor()
city = input("enter city ")
# mycursor.execute("UPDATE product1 SET city=%s WHERE pid=%s", (city,1))

mycursor.execute("UPDATE product1 SET city=%s WHERE pid=%s", (city,2))
mydb.commit()