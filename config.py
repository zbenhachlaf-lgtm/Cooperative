import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'argan-tamnat-secret-key-2024')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'argan_shop.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'zakariabenhachlaf44@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'ztop aonh wpel flzv')  # App password
    MAIL_DEFAULT_SENDER = 'zakariabenhachlaf44@gmail.com'

    # Order recipient
    ORDER_RECIPIENT_EMAIL = 'zakariabenhachlaf44@gmail.com'

    # Upload
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'images', 'products')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    # Default language
    DEFAULT_LANGUAGE = 'fr'
    SUPPORTED_LANGUAGES = ['fr', 'en', 'ar']
