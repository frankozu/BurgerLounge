from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)

# This function will connect to the SQLite database for MenuStore
def get_db_connection():
    """
    Establish a connection to the SQLite database.
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
    Root path to display a welcome message.
    """
    return "Welcome to BurgerLounge! Use /menu to view the menu."

# Getting all the menu items
@app.route('/menu', methods=['GET'])
def get_menu():
    """
    Getting all the items that are in the menu.
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

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

# Searchable database
@app.route('/search', methods=['GET'])
def search_menu():
    """
    Search items in the menu by name.
    """
    query = request.args.get('q', '')
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    results = conn.execute('SELECT * FROM burgers WHERE name LIKE ?', ('%' + query + '%',)).fetchall()
    conn.close()

    if not results:
        return jsonify({'message': 'No items found matching your search.'}), 404
    
    return jsonify({'burgers': [dict(row) for row in results]})

# Order management - create, modify
orders = []  # Keep track of current orders

# Place an order
@app.route('/order', methods=['POST'])
def place_order():
    """
    Place a new order.
    """
    app.logger.info(f"Raw request data: {request.data}")
    try:
        order_data = request.get_json()
        orders.append(order_data)  # Add order to the list
        app.logger.info(f"Parsed order data: {order_data}")
        return jsonify({'status': 'Order received', 'order': order_data})
    except Exception as e:
        app.logger.error(f"Error parsing JSON: {str(e)}")
        return jsonify({'error': 'Invalid JSON'}), 400

# Adjust (remove) items from the order before it's sent
@app.route('/order/remove', methods=['POST'])
def remove_item_from_order():
    """
    Remove an item from an existing order.
    """
    try:
        data = request.get_json()
        order_index = int(data.get('order_index'))
        item_to_remove = data.get('item')

        if order_index >= len(orders):
            return jsonify({'error': 'Order not found'}), 404

        order = orders[order_index]
        if item_to_remove in order.values():
            order.pop(item_to_remove, None)
            app.logger.info(f"Updated order: {order}")
            return jsonify({'status': 'Item removed', 'updated_order': order})
        else:
            return jsonify({'error': 'Item not found in order'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Tailor (customize) order items before it's sent
@app.route('/order/customize', methods=['POST'])
def customize_order():
    """
    Customize order items before sending.
    """
    try:
        data = request.get_json()
        order_index = int(data.get('order_index'))
        customizations = data.get('customizations', {})

        if order_index >= len(orders):
            return jsonify({'error': 'Order not found'}), 404

        order = orders[order_index]
        for item, custom in customizations.items():
            if item in order:
                order[item] = custom  # Modify the item in the order
        app.logger.info(f"Updated order: {order}")
        return jsonify({'status': 'Order customized', 'updated_order': order})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
