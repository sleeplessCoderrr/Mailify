from flask import Blueprint, request, jsonify
from ..services.email_generator import Request

email_bp = Blueprint('email', __name__)

@email_bp.route('/generate-email', methods=['POST'])
def generate_email():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid request. No data provided.'}), 400

        purpose = data.get('purpose')
        name = data.get('name')
        receiver = data.get('receiver')
        receiver_mail = data.get('receiverMail')
        goal_categories = data.get('goalCategories')
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
