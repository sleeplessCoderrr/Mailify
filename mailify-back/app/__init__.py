from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": os.getenv("CORS_ALLOWED_ORIGINS", "*")}})
    app.config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

    from .routes import chatgpt_bp
    app.register_blueprint(chatgpt_bp)

    return app

