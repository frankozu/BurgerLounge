from flask import Flask, jsonify, request
import sqlite3
import os
import requests  # Import requests to forward the order to KitchenView
import pdb  # Importing pdb for debugging purposes

app = Flask(__name__)

# Function to connect to SQLite database
def get_db_connection():
    """
    Establish a connection to the SQLite database.
    """
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'menu.db')
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        app.logger.error(f"Database connection failed: {str(e)}")
        return None

# Root route to show a welcome message
@app.route('/')
def home():
    """
    Root path to display a welcome message.
    """
    return "Welcome to BurgerLounge! Use /menu to view the menu."

# Route to get all the menu items
@app.route('/menu', methods=['GET'])
def get_menu():
    """
    Getting all items from the menu.
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    burgers = conn.execute('SELECT * FROM burgers').fetchall()
    condiments = conn.execute('SELECT * FROM condiments').fetchall()
    drinks = conn.execute('SELECT * FROM drinks').fetchall()
    
    conn.close()
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
    Search for items in the menu by name.
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

# List for all current orders
orders = []

# Place an order and forward to KitchenView
@app.route('/order', methods=['POST'])
def place_order():
    """
    Place a new order and forward it to KitchenView.
    """

    
    app.logger.info(f"Raw request data: {request.data}")
    try:
        order_data = request.get_json()
        orders.append(order_data)  # Add order to the list
        app.logger.info(f"Parsed order data: {order_data}")
        
        # Forward the order to KitchenView
        kitchen_view_url = "http://kitchenview:5001/order"
        response = requests.post(kitchen_view_url, json=order_data)
        
        if response.status_code == 200:
            app.logger.info("Order successfully forwarded to KitchenView.")
            return jsonify({'status': 'Order received and forwarded', 'order': order_data})
        else:
            app.logger.error(f"Failed to forward order to KitchenView: {response.status_code}")
            return jsonify({'error': 'Failed to forward order to KitchenView'}), 500
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

# Customize order items before sending to KitchenView
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
