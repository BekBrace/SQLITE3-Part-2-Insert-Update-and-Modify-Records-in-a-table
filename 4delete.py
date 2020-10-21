import sqlite3
connection = sqlite3.connect('accounting.db')
connection.execute('DELETE from employees WHERE id = 1')
connection.commit()
print('Total number of rows deleted: ', connection.total_changes)
cursor = connection.execute('SELECT * FROM employees')
for record in cursor:
    print(record)

connection.close()
