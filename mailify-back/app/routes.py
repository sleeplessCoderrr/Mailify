from flask import Blueprint, request, jsonify
from .services import generate_chatgpt_response 
from .model.request.request import Request
from .model.prompt.email_prompt import generate_email_prompt
from .model.prompt.subject_prompt import generate_subject_prompt

chatgpt_bp = Blueprint('chatgpt', __name__)

@chatgpt_bp.route('/generate-email', methods=['POST'])
def generate_email():
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid request. No data provided.'}), 400

    email_request = Request(
        data.get('purpose'),
        data.get('name'),
        data.get('receiver'),
        data.get('receiverMail'),
        data.get('goalCategories'),
        data.get('emailAbout')
    )

    try:
        email_prompt = generate_email_prompt(email_request)
        subject_prompt = generate_subject_prompt(email_request)
        
        ## Debug Purpose
        # print(data)
        # print(email_request.email_about)
        # print(email_prompt)
        # print(subject_prompt)

        generated_email = generate_chatgpt_response(email_prompt, 300)
        generated_subject = generate_chatgpt_response(subject_prompt, 20)

        return jsonify({
            "person_email": email_request.receiver_mail,
            "generated_subject": generated_subject,
            "generated_email": generated_email
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

