from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

@app.route('/generate-email', methods=['POST'])
def generate_email():
    """
    API endpoint to generate an email using OpenAI's GPT-3.
    Expects a JSON payload with 'user_prompt' and 'start'.
    """
    try:
        data = request.json
        user_prompt = data.get("user_prompt", "Write me a professionally sounding email")
        start = data.get("start", "Dear")

        response = openai.Completion.create(
            engine="davinci",
            prompt=user_prompt + "\n\n" + start,
            temperature=0.71,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.36,
            presence_penalty=0.75
        )
        email = response.get("choices")[0]["text"]
        return jsonify({"email": email}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
