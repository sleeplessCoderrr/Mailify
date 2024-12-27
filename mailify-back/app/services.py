import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_chatgpt_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=300  
        )

        generated_text = response['choices'][0]['message']['content'].strip()
        return generated_text
    except Exception as e:
        raise Exception("Error communicating with OpenAI API: " + str(e))
