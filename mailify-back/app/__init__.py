import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

def create_app():
    app = Flask(__name__)

    cors_origins = os.getenv('CORS_ALLOWED_ORIGINS', '*').split(',')
    CORS(app, resources={r"/*": {"origins": cors_origins if cors_origins != ['*'] else "*"}})
    app.config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    
    from .routes import chatgpt_bp
    app.register_blueprint(chatgpt_bp)
    
    return app
