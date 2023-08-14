import json
from flask import Flask, jsonify, request
import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.models import Symptom

openai.api_key = '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'

def embed_input(user_input: list):
    embeddings_dict = openai.Embedding.create(
        input=user_input, 
        model="text-embedding-ada-002")["data"]
    
    embeddings = []

    for embedding in embeddings_dict:
        embeddings.append(embedding["embedding"])

    # return jsonify(embeddings)
    return json.dumps(embeddings)
    
    # return response.choices[0].text.strip()

# def calculate_similarity(disease_id):
#     data = request.get_json()

#     user_input = data.get('user_input', '')

#     # embed user-text
#     embeddings = openai.Embedding.create(
#         model="text-embedding-ada-002",
#         prompt=user_input
#     )

#     user_input_embedding = embeddings

#     symptoms = Symptom.query.all()
#     embedded_symptoms = [np.fromstring(symptom.embedded_description[1:-1], sep=', ') for symptom in symptoms]

#     similarities = [cosine_similarity([user_input_embedding], [symptom_embedding])[0][0]
#                     for symptom_embedding in embedded_symptoms]
    
#     return jsonify({'similarities': similarities}), 200

def predict_disease_from_similarities(similarities):
    threshold_value = 0.8  # Setting threshold value

    sorted_similarities = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)

    for symptom_index, similarity in sorted_similarities:
        if similarity > threshold_value:
            predicted_disease = get_disease_from_symptom_index(symptom_index)
            return predicted_disease

    return "Unknown Disease"

def get_disease_from_symptom_index(symptom_index):
    # mapping logic
    mapping = {
        0: "Common Cold",
        1: "Hypoglycemia",
        2: "Malaria",
        3: "peptic ulcer disease",
        4: "Typhoid",
        5: "Urinary tract infection",
        6: "Depression"
    }
    return mapping.get(symptom_index, "Unknown Disease")