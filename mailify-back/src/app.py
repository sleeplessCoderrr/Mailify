from flask import Flask, request, jsonify
from flask_cors import CORS  
from email_generator import generate_job_application_email, Request

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

@app.route('/generate-email', methods=['POST'])
def generate_email():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request. No data provided.'}), 400
        
        purpose = data.get('purpose')
        name = data.get('name')
        receiver = data.get('receiver')
        goalCategories = data.get('goalCategories')
        emailAbout = data.get('emailAbout')
        
        request = Request(purpose, name, receiver, goalCategories, emailAbout)
        generated_email = generate_email(request)
        return jsonify({'generated_email': generated_email}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
