import json
from flask import Flask, jsonify, request
from transformers import pipeline, AutoTokenizer
import os
app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained(
    "vinai/bertweet-base", normalization=True)
emojify = pipeline("text-classification",
                   model="./model", tokenizer=tokenizer)
tokenizer_kwargs = {'padding': True, 'truncation': True}


@app.route('/')
def test():
    return 'Emotify Server is ON! woooooo'


@app.route('/predict', methods=['get'])
def predict():
    user_input = request.args['tweet']
    prediction = emojify([user_input], **tokenizer_kwargs)
    print(prediction)
    print(prediction[0])
    print(jsonify(prediction))
    print(jsonify(prediction[0]))
    return prediction[0]


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
