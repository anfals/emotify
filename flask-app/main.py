import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from transformers import pipeline, AutoTokenizer
import os

app = Flask(__name__)
CORS(app)

tokenizer = AutoTokenizer.from_pretrained(
    "vinai/bertweet-base", normalization=True)
emojify = pipeline("text-classification",
                   model="./model", tokenizer=tokenizer, return_all_scores=True)
tokenizer_kwargs = {'padding': True, 'truncation': True}


@app.route('/')
def test():
    return 'Emotify Server is ON! woooooo'


@app.route('/predict', methods=['get'])
def predict():
    user_input = request.args['tweet']
    prediction = emojify([user_input], **tokenizer_kwargs)
    return jsonify(prediction[0])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
