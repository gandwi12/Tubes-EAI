# Food Delivery System Overview
Sistem delivery makanan berbasis Flask dengan frontend interaktif menggunakan Jinja2, HTML, CSS, dan JavaScript.

## Technologies Used:
- **Backend**: Flask 3.0.0, Python
- **Frontend**: HTML5, CSS3 (Responsive), JavaScript (ES6)
- **Database**: MySQL (with mysqlclient)
- **Tools**: Flask-SQLAlchemy, Flask-Migrate, python-dotenv

---

## Installation
1. **Clone repository**:
    ```bash
    git clone https://github.com/gandwi12/Tubes-EAI.git
    cd Tubes-EAI/Tubes_UTS
    ```

2. **Create virtual environment** (optional):
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

---

## Run the Application
- **Method 1**: From the `Tubes_UTS` folder:
    ```powershell
    python api_gateway/app.py
    ```

- **Method 2**: Using Flask CLI:
    ```powershell
    $env:FLASK_APP = 'api_gateway.app'
    python -m flask run --host=127.0.0.1 --port=5000
    ```

---

## Struktur Folder
```
Tubes_UTS/
├── api_gateway/
│   └── app.py              # Flask app utama dengan routes
├── menu/
│   ├── app.py
│   ├── config.py
│   └── models.py
├── order/
│   ├── app.py
│   ├── config.py
│   └── models.py
├── payment/
│   ├── app.py
│   ├── config.py
│   └── models.py
├── restoran/
│   ├── app.py
│   ├── config.py
│   └── models.py
├── User/
│   ├── app.py
│   ├── config.py
│   └── models.py
├── static/
│   ├── style.css           # Styling responsif
│   └── app.js              # Interaktivitas (cart, form handling)
├── templates/
│   ├── base.html           # Template dasar (base layout)
│   ├── index.html          # Halaman utama
│   ├── menu.html           # Halaman menu
│   ├── order.html          # Halaman keranjang & form pengiriman
│   ├── payment.html        # Halaman pembayaran
│   ├── restoran.html       # Halaman daftar restoran
│   └── user.html           # Halaman profil pengguna
├── requirements.txt        # Python dependencies
└── Readme.md               # File ini
```


---

## Core Features

1. **Homepage**: Displays hero section and feature buttons.
2. **Menu**: Shows food items with "Add to Cart" buttons.
3. **Order**: Users can review cart, adjust quantities, and submit orders.
4. **Payment**: Users choose payment methods (COD, Bank Transfer, E-Wallet).
5. **Restaurant**: Displays available restaurants with menu links.
6. **User Profile**: Displays user profile and edit option.

---

## Frontend Features
- **Real-time Cart**: Cart is saved in `localStorage`, updated with actions like adding, removing, or changing quantity.
- **Form Validation**: Ensures name and address are filled before submission.

---

## Running Backend API
1. **Test Post Order**:
    ```bash
    curl -X POST http://127.0.0.1:5000/order \
        -H "Content-Type: application/json" \
        -d '{"cart":[{"id":1,"name":"Nasi Goreng","price":"25000","qty":2}],"name":"Joni","address":"Jl Merdeka"}'
    ```

2. **Test Post Payment**:
    ```bash
    curl -X POST http://127.0.0.1:5000/payment \
        -H "Content-Type: application/json" \
        -d '{"method":"cod"}'
    ```

---

## Customization
- **Change Brand Name**: Edit `templates/base.html`.
    ```html
    <a class="brand" href="/">FoodDelivery</a>  <!-- Change text here -->
    ```

- **Add Menu Item**: Edit `api_gateway/app.py` in `SAMPLE_ITEMS`.
    ```python
    SAMPLE_ITEMS = [
        {'id': 5, 'name': 'Bakso Sapi', 'price': '22000', 'description': 'Bakso daging sapi premium', 'image_url': '/static/img/bakso.jpg'},
        # ... add more items
    ]
    ```

---

## Development Steps
1. Define models for **User**, **Restaurant**, **Menu**, **Order**, **Payment**.
2. Implement **Authentication** using Flask-Login or JWT.
3. Extend routes for **CRUD** operations and **Payment Gateway** integration.

---

## Troubleshooting
- **Port 5000 already in use**: Change port in `api_gateway/app.py`:
    ```python
    app.run(host='127.0.0.1', port=5001, debug=True)
    ```

- **Module not found**: Ensure correct MySQL driver is installed, or use SQLite for development:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fooddelivery.db'
    ```

- **Template not found error**: Ensure folder structure is correct.

---
### **Gambar Postman**:
1. **Update Payment Data (PUT Request)**  
   ![Update Payment](sandbox:/mnt/data/WhatsApp%20Image%202025-11-14%20at%2001.01.12_8fd1437c.jpg)

2. **Post Food Item Data (POST Request)**  
   ![Post Food Item](sandbox:/mnt/data/WhatsApp%20Image%202025-11-14%20at%2001.01.15_68e94b5c.jpg)

3. **Get Order Data (GET Request)**  
   ![Get Order](sandbox:/mnt/data/WhatsApp%20Image%202025-11-14%20at%2001.01.18_9f0d641c.jpg)

4. **Update Order Data (PUT Request)**  
   ![Update Order](sandbox:/mnt/data/WhatsApp%20Image%202025-11-14%20at%2001.01.18_856980c4.jpg)

5. **Get User Data (GET Request)**  
   ![Get User](sandbox:/mnt/data/WhatsApp%20Image%202025-11-14%20at%2001.01.22_64ce09ff.jpg)

6. **Post User Data (POST Request)**  
   ![Post User](sandbox:/mnt/data/WhatsApp%20Image%202025-11-14%20at%2001.01.22_64ce09ff.jpg)

---

**Note**: I have added the images directly to the documentation for reference. Let me know if you need any further adjustments!

### Module not found: mysqlclient error
Pastikan sudah install MySQL driver yang tepat untuk sistem Anda, atau gunakan SQLite untuk development:
```python
# Di api_gateway/app.py, ubah config jika perlu SQLite:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fooddelivery.db'
```

### Template not found error
Pastikan struktur folder benar:
- `api_gateway/app.py` berada di subfolder `api_gateway/`
- `templates/` dan `static/` berada di parent folder (Tubes_UTS)
- Flask app di-initialize dengan `template_folder='../templates'` dan `static_folder='../static'`

## Next Steps (Backend Integration)
Untuk integrasi lengkap dengan backend:
1. **Database Models**: Gunakan SQLAlchemy untuk define User, Restaurant, Menu, Order, Payment models
2. **Authentication**: Implementasikan login/register dengan Flask-Login atau JWT
3. **API Routes**: Extend routes untuk CRUD operations
4. **Payment Gateway**: Integrasi dengan Midtrans, Stripe, atau provider lain
5. **Email Notifications**: Kirim email konfirmasi order dan status delivery
6. **Real-time Updates**: Gunakan WebSocket atau polling untuk tracking pesanan

## License
MIT

## Author
Tubes EAI - Food Delivery System  
Repository: https://github.com/gandwi12/Tubes-EAI
