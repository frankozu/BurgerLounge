from flask import Flask
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def setup_database():
    db_path = os.path.join(os.path.dirname(__file__), 'menu.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print(f"Connected to database at: {db_path}")

    # Create burgers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS burgers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )
    ''')
    print("Burgers table created or already exists.")

    # Create condiments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS condiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )
    ''')
    print("Condiments table created or already exists.")

    # Create drinks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drinks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )
    ''')
    print("Drinks table created or already exists.")

    # Insert default data into tables if empty
    cursor.execute('SELECT COUNT(*) FROM burgers')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO burgers (name, price) VALUES ('Cheeseburger', 4.99)")
        cursor.execute("INSERT INTO burgers (name, price) VALUES ('Veggie Burger', 3.99)")
        print("Inserted data into burgers table.")
    else:
        print("Burgers table already has data.")

    cursor.execute('SELECT COUNT(*) FROM condiments')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO condiments (name, price) VALUES ('Ketchup', 0.50)")
        cursor.execute("INSERT INTO condiments (name, price) VALUES ('Mustard', 0.50)")
        print("Inserted data into condiments table.")
    else:
        print("Condiments table already has data.")

    cursor.execute('SELECT COUNT(*) FROM drinks')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO drinks (name, price) VALUES ('Cola', 1.99)")
        cursor.execute("INSERT INTO drinks (name, price) VALUES ('Water', 1.00)")
        print("Inserted data into drinks table.")
    else:
        print("Drinks table already has data.")

    conn.commit()
    conn.close()
    return "Database setup complete."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
