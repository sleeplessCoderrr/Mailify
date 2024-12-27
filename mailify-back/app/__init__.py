from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, origins=app.config['CORS_ALLOWED_ORIGINS'])

    from .routes import email_bp
    app.register_blueprint(email_bp)

    return app
