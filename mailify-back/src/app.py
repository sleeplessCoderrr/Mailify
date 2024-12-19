from flask import Flask, request, jsonify
from email_generator import generate_job_application_email

app = Flask(__name__)

@app.route('/generate-email', methods=['POST'])
def generate_email():
    """
    API endpoint to generate a job application email.
    Expects a JSON payload with 'sender_name', 'receiver_name', and 'main_point'.
    """
    try:
        data = request.json
        sender_name = data.get("sender_name", "John Doe")
        receiver_name = data.get("receiver_name", "Ms. Jane Smith")
        main_point = data.get("main_point", "I am writing to express my interest in the Software Engineer position at your company.")

        generated_email = generate_job_application_email(sender_name, receiver_name, main_point)
        return jsonify({"email": generated_email}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
