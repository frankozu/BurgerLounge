import sqlite3
import os

# Setting the path to the SQLite database
db_path = os.path.join(os.path.dirname(__file__), 'menu.db')

# Connect to the SQLite database
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    print(f"Connected to database at: {db_path}")

    # Function to create tables
    def create_table(table_name, fields):
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                {fields}
            )
        ''')
        print(f"{table_name.capitalize()} table created or already exists.")

    # Function to insert data if table is empty
    def insert_data_if_empty(table_name, data):
        cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
        if cursor.fetchone()[0] == 0:
            cursor.executemany(f'INSERT INTO {table_name} (name, price) VALUES (?, ?)', data)
            print(f"Inserted data into {table_name} table.")
        else:
            print(f"{table_name.capitalize()} table already has data.")

    # Create tables
    create_table('burgers', 'id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL')
    create_table('condiments', 'id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL')
    create_table('drinks', 'id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL')

    # Define initial data
    burgers = [('Cheeseburger', 4.99), ('Veggie Burger', 3.99)]
    condiments = [('Ketchup', 0.50), ('Mustard', 0.50)]
    drinks = [('Cola', 1.99), ('Water', 1.00)]

    # Insert initial data
    insert_data_if_empty('burgers', burgers)
    insert_data_if_empty('condiments', condiments)
    insert_data_if_empty('drinks', drinks)

    print("Database operations complete.")
    