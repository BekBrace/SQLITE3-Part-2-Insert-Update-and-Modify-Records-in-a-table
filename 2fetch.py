import sqlite3
connection = sqlite3.connect('accounting.db')

cursor = connection.cursor()

# Fetch all data from the table emp
cursor.execute(
    "SELECT * FROM employees")

# Store all the fectched data in the data variable
# data = cursor.fetchall()
# print(data)
for record in cursor:
    print(record)
