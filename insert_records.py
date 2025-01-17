import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"

)

mycursor=mydb.cursor()

products = [
    (1, 'Laptop', 899.99, 'New York'),
    (2, 'Smartphone', 499.99, 'Los Angeles'),
    (3, 'Headphones', 199.99, 'Chicago'),
    (4, 'Keyboard', 49.99, 'San Francisco'),
    (5, 'Mouse', 29.99, 'Boston')
]

mycursor.executemany("INSERT INTO product1 (pid, pname, price, city) VALUES (%s, %s, %s, %s)", products)

mydb.commit()