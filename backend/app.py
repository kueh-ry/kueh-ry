import json
from flask import Flask

app = Flask(__name__)

@app.route('/<image>', methods=['POST'])
def predict_image(image):
    return image

@app.route('/test')
def get():
    return "Hello world!"
