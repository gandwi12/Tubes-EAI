import os
os.environ['FLASK_SKIP_DOTENV'] = '1'

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'dev-secret-key'

# User data storage (in-memory)
user_storage = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'phone': '08123456789'
}

# Sample data
SAMPLE_ITEMS = [
    {'id': 1, 'name': 'Nasi Goreng', 'price': '25000', 'description': 'Nasi goreng spesial dengan telur', 'image_url': 'https://cdn-brn1.b-cdn.net/v/P/cb1e8c3e20114c7691bb03fa3d85c6ff-s-w1200-q80.jpg'},
    {'id': 2, 'name': 'Soto Ayam', 'price': '18000', 'description': 'Soto ayam tradisional', 'image_url': 'https://cdn-brn1.b-cdn.net/v/P/8eb6e2a1e6c245888baee1a56cc5e9bc-s-w1200-q80.jpg'},
    {'id': 3, 'name': 'Gado-gado', 'price': '15000', 'description': 'Gado-gado saus kacang', 'image_url': 'https://cdn-brn1.b-cdn.net/v/P/5c6e8f2a3d4b1e9c7f2a5d8e3c1b4a9f-s-w1200-q80.jpg'},
    {'id': 4, 'name': 'Satay Ayam', 'price': '20000', 'description': 'Sate ayam dengan bumbu kacang', 'image_url': 'https://cdn-brn1.b-cdn.net/v/P/9f2a3b1c4d5e6f7a8b9c0d1e2f3a4b5c-s-w1200-q80.jpg'},
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
    # Fetch user data dari storage
    return render_template('user.html', user=user_storage)

@app.route('/user/edit', methods=['GET', 'POST'])
def user_edit():
    global user_storage
    
    if request.method == 'POST':
        data = request.get_json() if request.is_json else request.form
        # Update user storage
        user_storage['name'] = data.get('name', user_storage['name'])
        user_storage['email'] = data.get('email', user_storage['email'])
        user_storage['phone'] = data.get('phone', user_storage['phone'])
        
        print(f"User profile updated: {user_storage}")
        return jsonify({'status': 'ok', 'message': 'Profil berhasil diperbarui'}), 200
    
    # Get current user data from storage
    return render_template('user_edit.html', user=user_storage)

@app.errorhandler(404)
def not_found(e):
    return '<h1>404 - Page Not Found</h1><p><a href="/">Kembali ke Home</a></p>', 404

@app.errorhandler(500)
def server_error(e):
    return '<h1>500 - Server Error</h1><p>' + str(e) + '</p>', 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
