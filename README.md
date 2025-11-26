# py_db_connection

This project contains Python scripts that demonstrate basic **MySQL database operations** using `mysql-connector-python`.  
It covers creating tables, inserting data, displaying records, updating entries, and deleting rows.

---

## 📌 Tech Used
- Python 3
- MySQL
- mysql-connector-python

---

## 📂 Scripts Included

- `create_table.py` – Create the `product1` table  
- `insert_records.py` – Insert new records  
- `display_records.py` – Display all rows  
- `display_asc.py` – Display records in ascending order  
- `display_city.py` – Filter by city  
- `display_price.py` – Filter by price  
- `select_rec.py` – Select a specific record  
- `update_rec.py` – Update a record  
- `update_all.py` – Update all records  
- `delete_rec.py` – Delete a record  

---

## ▶️ How to Run

1. Install MySQL connector:
```bash
pip install mysql-connector-python
Update DB connection details in the scripts:

mydb = c.connect(
    host="localhost",
    user="root",
    password="manager",
    database="sharvan"
)


Run any script:

python create_table.py
python insert_records.py
python display_records.py
