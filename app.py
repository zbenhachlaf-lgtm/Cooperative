from flask import Flask, session, g
from flask_login import LoginManager
from config import Config
from models import db, Utilisateur
from services.email_service import mail
import json
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    mail.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'admin.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Utilisateur.query.get(int(user_id))

    # Translation system
    translations_cache = {}

    def load_translations(lang):
        if lang not in translations_cache:
            path = os.path.join(app.root_path, 'translations', lang, 'messages.json')
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    translations_cache[lang] = json.load(f)
            else:
                translations_cache[lang] = {}
        return translations_cache[lang]

    @app.before_request
    def before_request():
        g.lang = session.get('lang', app.config['DEFAULT_LANGUAGE'])
        g.translations = load_translations(g.lang)
        g.is_rtl = (g.lang == 'ar')

    @app.context_processor
    def inject_translations():
        def t(key):
            return g.translations.get(key, key)
        cart = session.get('cart', {})
        cart_count = sum(cart.values()) if cart else 0
        return {
            't': t,
            'lang': g.lang,
            'is_rtl': g.is_rtl,
            'cart_count': cart_count,
            'supported_languages': app.config['SUPPORTED_LANGUAGES']
        }

    # Register blueprints
    from routes.client import client_bp
    from routes.admin import admin_bp
    app.register_blueprint(client_bp)
    app.register_blueprint(admin_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
