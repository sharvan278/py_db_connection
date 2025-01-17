import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"
)

mycursor = mydb.cursor()

# Take user inputs
id = input("Enter product id: ")
name = input("Enter product name: ")
price = int(input("Enter product price: "))  # Converts input to an integer
city = input("Enter city: ")

# Perform the update operation using %s for all placeholders
mycursor.execute("UPDATE product1 SET pname=%s, price=%s, city=%s WHERE pid=%s", (name, price, city, id))

# Commit the changes to the database
mydb.commit()

print("Product updated successfully.")
