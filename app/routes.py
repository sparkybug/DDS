import json
from flask import request, jsonify
import numpy as np
from app.app import app
from app import openai_utils
from sklearn.metrics.pairwise import cosine_similarity
from app.models import db, Symptom

@app.route('/api/embed-symptoms/', methods=['POST'])
def embed_symptoms():
    user_input = request.json.get("userInput")
    embedded_input = openai_utils.embed_input(user_input)
    return jsonify({'embedded_input': embedded_input})

# @app.route('/api/predict-disease/', methods=['POST'])
def predict_diseases():
    data = request.get_json()
    user_input = data.get("userInput", "")

    # Embed user input
    user_input_embedding = openai_utils.embed_input(user_input)

    with app.app_context():
        # Fetch symptoms and their embeddings
        symptoms = Symptom.query.all()
        embedded_symptoms =[] 
        [embedded_symptoms.append(np.array(json.loads(symptom.embedded_description))) for symptom in symptoms]

        # Calculate similarities
        similarities = cosine_similarity(np.array([user_input_embedding]), np.array(embedded_symptoms))

        # Predict disease based on similarities
        predicted_disease = openai_utils.ranker(similarities)
        
        return jsonify({'predicted_disease': predicted_disease}), 200
    
        # print(similarities)
        # return jsonify({'similarities': similarities[0]})
