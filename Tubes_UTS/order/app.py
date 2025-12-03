from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json
from models import db, Order
import os
os.environ['FLASK_SKIP_DOTENV'] = '1'
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)


def seed_data():
   
    pass



try:
    @app.before_first_request
    def create_tables_and_seed():
        db.create_all()
        seed_data()
except Exception:
    def create_tables_and_seed():
        db.create_all()
        seed_data()


@app.route('/orders', methods=['GET'])
def list_orders():
    orders = Order.query.all()
    return jsonify([o.to_dict() for o in orders])

@app.route('/health')
def health():
    return jsonify({'status':'ok','service':'order','time': datetime.utcnow().isoformat()}), 200


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    o = Order.query.get(order_id)
    if not o:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(o.to_dict())


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json() or {}
    items = data.get('items', [])
    if not isinstance(items, list) or len(items) == 0:
        return jsonify({'error': 'items must be a non-empty list'}), 400
    try:
        total_price = int(data.get('total_price', 0))
    except Exception:
        return jsonify({'error': 'total_price must be integer'}), 400

    o = Order(items=json.dumps(items), total_price=total_price, status=data.get('status', 'pending'))
    db.session.add(o)
    db.session.commit()
    return jsonify(o.to_dict()), 201


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json() or {}

    item_id = data.get("id")
    if not item_id:
        return jsonify({"error": "id item harus dikirim"}), 400

    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    
    items = json.loads(order.items)

    updated = False

   
    for item in items:
        if item["id"] == item_id:
            if "name" in data:
                item["name"] = data["name"]
            if "price" in data:
                item["price"] = int(data["price"])
            if "qty" in data:
                item["qty"] = int(data["qty"])
            updated = True

    if not updated:
        return jsonify({"error": "Item dengan id tersebut tidak ditemukan"}), 404

  
    new_total = sum(i["price"] * i["qty"] for i in items)

    order.items = json.dumps(items)
    order.total_price = new_total

    db.session.commit()

    return jsonify(order.to_dict()), 200




@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    o = Order.query.get(order_id)
    if not o:
        return jsonify({'error': 'Order not found'}), 404
    db.session.delete(o)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(host='127.0.0.1', port=Config.PORT, debug=True)