from flask import request, jsonify
import numpy as np
from app.app import app
from app import openai_utils
from sklearn.metrics.pairwise import cosine_similarity
from app.models import db, Symptom

@app.route('/api/embed-symptoms', methods=['POST'])
def embed_symptoms():
    user_input = request.json.get("userInput")
    embedded_input = openai_utils.embed_input(user_input)
    return jsonify({'embedded_input': embedded_input})


# @app.route('/api/get-similar-symptoms/<int:disease_id>', methods=['GET'])
# def get_similar_symptoms(disease_id):
#     similar_symptoms = openai_utils.calculate_similarity(disease_id)
#     return jsonify({'similar_symptoms': similar_symptoms})

@app.route('/api/predict-disease', methods=['POST'])
def predict_disease():
    data = request.get_json()
    user_input = data.get('user_input', '')

    # Embed user input
    embeddings = openai_utils.embed_input(user_input)
    user_input_embedding = embeddings

    with app.app_context():
        # Fetch symptoms and their embeddings
        symptoms = Symptom.query.all()
        embedded_symptoms = [np.fromstring(symptom.embedded_description[1:-1], sep=', ') for symptom in symptoms]

        # Calculate similarities
        similarities = [cosine_similarity([user_input_embedding], [symptom_embedding])[0][0]
                        for symptom_embedding in embedded_symptoms]

        # Predict disease based on similarities
        predicted_disease = openai_utils.predict_disease_from_similarities(similarities)
        
        return jsonify({'predicted_disease': predicted_disease}), 200
