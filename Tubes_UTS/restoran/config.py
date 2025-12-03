import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DB = f"sqlite:///{BASE_DIR / 'database.db'}"
# SHARED DATABASE (bisa ganti ke MySQL)
SHARED_DB = "mysql+pymysql://root:@localhost/food_delivery_db"

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'resto-dev-key')
    # Uncomment ini kalau mau pake 1 database MySQL:
    # SQLALCHEMY_DATABASE_URI = SHARED_DB
    # Atau pake environment variable:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', DEFAULT_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = int(os.getenv('PORT', 5005))
    SERVICE_NAME = os.getenv('SERVICE_NAME', 'restoran-service')
    SERVICE_URL = os.getenv('SERVICE_URL', f"http://127.0.0.1:{PORT}")