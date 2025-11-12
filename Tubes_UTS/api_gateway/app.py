from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'dev-secret-key'

# Sample data
SAMPLE_ITEMS = [
    {'id': 1, 'name': 'Nasi Goreng', 'price': '25000', 'description': 'Nasi goreng spesial dengan telur', 'image_url': '/static/img/nasi-goreng.jpg'},
    {'id': 2, 'name': 'Soto Ayam', 'price': '18000', 'description': 'Soto ayam tradisional', 'image_url': '/static/img/soto-ayam.jpg'},
    {'id': 3, 'name': 'Gado-gado', 'price': '15000', 'description': 'Gado-gado saus kacang', 'image_url': '/static/img/gado-gado.jpg'},
    {'id': 4, 'name': 'Satay Ayam', 'price': '20000', 'description': 'Sate ayam dengan bumbu kacang', 'image_url': '/static/img/satay.jpg'},
]

SAMPLE_RESTAURANTS = [
    {'id': 1, 'name': 'Warung Asri', 'address': 'Jl. Merdeka 123, Jakarta'},
    {'id': 2, 'name': 'Restoran Tiga Rasa', 'address': 'Jl. Sudirman 456, Jakarta'},
    {'id': 3, 'name': 'Kedai Semarang', 'address': 'Jl. Ahmad Yani 789, Semarang'},
]

@app.context_processor
def inject_now():
    return {'current_year': datetime.now().year}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', items=SAMPLE_ITEMS)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        # Process order (in production, save to database)
        print(f"Order received: {data}")
        return jsonify({'status': 'ok', 'message': 'Pesanan berhasil dibuat'}), 200
    return render_template('order.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        # Process payment (in production, integrate with payment gateway)
        print(f"Payment received: {data}")
        return jsonify({'status': 'ok', 'message': 'Pembayaran berhasil'}), 200
    return render_template('payment.html')

@app.route('/restoran')
def restoran():
    return render_template('restoran.html', restaurants=SAMPLE_RESTAURANTS)

@app.route('/user')
def user():
    # In production, fetch user session
    user_data = {'name': 'John Doe', 'email': 'john@example.com'}
    return render_template('user.html', user=user_data)

@app.errorhandler(404)
def not_found(e):
    return '<h1>404 - Page Not Found</h1><p><a href="/">Kembali ke Home</a></p>', 404

@app.errorhandler(500)
def server_error(e):
    return '<h1>500 - Server Error</h1><p>' + str(e) + '</p>', 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
