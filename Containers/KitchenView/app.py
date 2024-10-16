from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to receive orders
@app.route('/order', methods=['POST'])
def receive_order():
    """
    Receives orders from BurgerOrderer and prints them.
    """
    order = request.get_json()
    print(f"New order received: {order}")
    return jsonify({"status": "Order received by KitchenView"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
