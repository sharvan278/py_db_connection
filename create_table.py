import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"

)

mycursor=mydb.cursor()

mycursor.execute("create table product1(pid int primary key,pname varchar(20),price double,city varchar(20))")