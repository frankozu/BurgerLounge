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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS burgers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS condiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drinks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()
    return "Database setup complete."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
