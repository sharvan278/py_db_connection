import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"
)

mycursor = mydb.cursor()

id = input("Enter product id: ")

mycursor.execute("SELECT * FROM product1 WHERE pid=%s", (id,))
result = mycursor.fetchone()

if result:
    print("Current record:", result)
else:
    print("No record found with that product id.")

mycursor.close()
mydb.close()
