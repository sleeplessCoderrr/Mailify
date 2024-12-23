from flask import Flask, request, jsonify
from flask_cors import CORS  
from email_generator import Request, Result, request_invoker

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
        receiver_mail = data.get('receiverMail')
        goal_categories= data.get('goalCategories')
        email_about = data.get('emailAbout')
        
        email_request = Request(purpose, name, receiver, receiver_mail, goal_categories, email_about)
        result = email_request.generate()
        return jsonify({
            'person_mail': result.person_mail, 
            'generated_mail': result.generated_mail, 
            'email_subject': result.email_subject
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
