from flask import Flask, request, jsonify

app = Flask(__name__)

orders_received = []

# Route to receive orders
@app.route('/order', methods=['POST'])
def receive_order():
    """
    Receives orders from BurgerOrderer and prints them.
    """
    order = request.get_json()
    print(f"New order received: {order}")
    orders_received.append(order)  # Keep track of orders received
    return jsonify({"status": "Order received by KitchenView"})

# List all orders received
@app.route('/orders', methods=['GET'])
def list_orders():
    """
    List all the orders received by KitchenView.
    """
    return jsonify({'orders_received': orders_received})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
