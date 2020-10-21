import sqlite3
connection = sqlite3.connect('accounting.db')
# Update a record
connection.execute(
    "UPDATE employees SET first_name='Isaac' WHERE last_name = 'David'")
cursor = connection.cursor()

# Insert a record
sql_command = """
INSERT INTO employees VALUES (007, "Robin", "Pit", "M", "1991-04-24")
"""
cursor.execute(sql_command)

connection.commit()
print('Total number of rows updated:', connection.total_changes)
table = connection.execute('SELECT * from employees')
for record in table:
    print(record)
connection.close()
