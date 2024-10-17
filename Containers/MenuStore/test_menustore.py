import sqlite3
import os

def test_database_setup():
    """Test that the database tables are set up correctly"""
    db_path = os.path.join(os.path.dirname(__file__), 'menu.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if tables exist
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='burgers'")
    assert cursor.fetchone() is not None

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='condiments'")
    assert cursor.fetchone() is not None

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='drinks'")
    assert cursor.fetchone() is not None

    conn.close()
