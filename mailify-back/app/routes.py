from flask import Blueprint, request, jsonify
from .services import generate_chatgpt_response 

chatgpt_bp = Blueprint('chatgpt', __name__)

@chatgpt_bp.route('/generate-email', methods=['POST'])
def generate_email():
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid request. No data provided.'}), 400

    purpose = data.get('purpose')
    name = data.get('name')
    receiver = data.get('receiver')
    receiver_mail = data.get('receiverMail')
    goal_categories = data.get('goalCategories')
    email_about = data.get('emailAbout')

    try:
        message = (f"Generate an email for {purpose}. The sender is {name}, and the receiver is {receiver}. "
                   f"The receiver's email is {receiver_mail}. The goal categories are {', '.join(goal_categories)}. "
                   f"The email's subject should be about: {email_about}. Please generate a professional email.")

        generated_email = generate_chatgpt_response(message)
        email_subject = f"{purpose}: {email_about}"  

        return jsonify({
            "person_email": receiver_mail,
            "email_subject": email_subject,
            "generated_email": generated_email
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

