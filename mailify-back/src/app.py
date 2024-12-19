from flask import Flask, request, jsonify
from email_generator import generate_job_application_email

app = Flask(__name__)

@app.route('/generate-email', methods=['POST'])
def generate_email():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request. No data provided.'}), 400
        sender_name = data.get('sender_name', 'Your Name')
        receiver_name = data.get('receiver_name', 'Recipient')
        main_point = data.get('main_point', 'I would like to apply for a job at your company.')
        max_length = data.get('max_length', 150)
        
        generated_email = generate_job_application_email(sender_name, receiver_name, main_point, max_length)
        return jsonify({'generated_email': generated_email}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
