import sqlite3
connection = sqlite3.connect('accounting.db')
cursor = connection.cursor()
sql_command = """ 
CREATE TABLE employees(
  id INTEGER PRIMARY KEY ,
  first_name VARCHAR (20),
  last_name VARCHAR (20),
  gender CHAR (1),
  joining_date DATE
);
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO employees VALUES (001, "John", "Doe", "M", "2000-04-24")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO employees VALUES (002, "Sarah", "Jones", "F", "1999-12-03")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO employees VALUES (003, "Sarah", "Day", "F", "1995-10-07")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO employees VALUES (004, "Noah", "David", "M", "2001-12-03")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO employees VALUES (005, "Joel", "Miller", "M", "1972-05-03")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO employees VALUES (006, "Mira", "Antoine", "F", "1977-10-30")
"""
cursor.execute(sql_command)

# Saving changes using commit () method
connection.commit()

# Closing the connection
connection.close()
