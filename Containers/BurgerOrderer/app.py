from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)

# This function will connect to the SQLite database for MenuStore
def get_db_connection():
    """
    This will establish a connection to the SQLite database
    """
    try:
        db_path = os.path.join(os.path.dirname(__file__), '../MenuStore/menu.db')
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        app.logger.error(f"Database connection failed: {str(e)}")
        return None

# Root path to show a welcome message
@app.route('/')
def home():
    """
    Root path to display a welcome message
    """
    return "Welcome to BurgerLounge! Use /menu to view the menu."

# Getting all the menu items
@app.route('/menu', methods=['GET'])
def get_menu():
    """
    Getting all the items that are in the menu
    """
    conn = get_db_connection()
    
    burgers = conn.execute('SELECT * FROM burgers').fetchall()
    condiments = conn.execute('SELECT * FROM condiments').fetchall()
    drinks = conn.execute('SELECT * FROM drinks').fetchall()
    
    conn.close()
# Prepare menu as JSON response
    menu = {
        'burgers': [dict(row) for row in burgers],
        'condiments': [dict(row) for row in condiments],
        'drinks': [dict(row) for row in drinks]
    }
    
    return jsonify(menu)

# Place an order
@app.route('/order', methods=['POST'])
def place_order():
    """
    This will help by placing an order
    """
    app.logger.info(f"Raw request data: {request.data}")
    try:
        order_data = request.get_json()
        app.logger.info(f"Parsed order data: {order_data}")
        return jsonify({'status': 'Order received', 'order': order_data})
    except Exception as e:
        app.logger.error(f"Error parsing JSON: {str(e)}")
        return jsonify({'error': 'Invalid JSON'}), 400

# Test route for POST requests
@app.route('/test', methods=['POST'])
def test_post():
    """
    Will show the test route for POST requests
    """
    return jsonify({'message': 'POST request successful!'})

# This starts the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
