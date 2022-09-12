import sqlite3

# Be careful not to create the database twice! Run the process only once.

connection = sqlite3.connect('customer_database.db')

cursor_db = connection.cursor()

cursor_db.execute('''CREATE TABLE customer (
    first_name text,
    last_name text,
    email text,
    phone text
    )
''')

connection.commit()
connection.close()
