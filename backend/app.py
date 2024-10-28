from flask import Flask, request, jsonify
import numpy as np
import random
from tensorflow.keras.models import load_model
from nltk.tokenize import RegexpTokenizer
import pickle

# Load model and tokenizer
model = load_model("./model/text_gen_model2.h5")
history = pickle.load(open("./model/history2.p", "rb"))

# Prepare tokenizer and index mapping
tokenizer = RegexpTokenizer(r"\w+")
unique_tokens = history['unique_tokens']
unique_token_index = {token: idx for idx, token in enumerate(unique_tokens)}
n_words = 10

# Initialize Flask app
app = Flask(__name__)

# Prediction function
def predict_next_word(input_text, n_best=5):
    X = np.zeros((1, n_words, len(unique_tokens)))
    words = input_text.lower().split()
    
    for i, word in enumerate(words[-n_words:]):  
        if word in unique_token_index:
            X[0, i, unique_token_index[word]] = 1
    
    predictions = model.predict(X)[0]
    indices = np.argpartition(predictions, -n_best)[-n_best:]
    return [unique_tokens[idx] for idx in indices]

# Route for text generation
@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    input_text = data.get("input_text", "")
    num_words = data.get("num_words", 20)  
    creativity = data.get("creativity", 3)
    
    word_sequence = input_text.split()
    for _ in range(num_words):
        sub_sequence = " ".join(word_sequence[-n_words:])
        try:
            next_word = random.choice(predict_next_word(sub_sequence, creativity))
        except:
            next_word = random.choice(unique_tokens)
        word_sequence.append(next_word)
    
    generated_text = " ".join(word_sequence)
    return jsonify({"generated_text": generated_text})

if __name__ == '__main__':
    app.run(debug=True)
