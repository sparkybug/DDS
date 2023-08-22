from flask import Flask
from app.app import app
import json
from flask import request, jsonify
import numpy as np
from app.app import app
from app import openai_utils
from sklearn.metrics.pairwise import cosine_similarity
from app.models import db, Symptom

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)