from flask import Flask, jsonify, request
import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.models import Symptom

openai.api_key = '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'

def embed_input(user_input):
    response = openai.Embedding.create(model="text-davinci-003", data=[user_input])

    return response.choices[0].text.strip()

def calculate_similarity(disease_id):
    data = request.get_json()

    user_input = data.get('user_input', '')

    # embed user-text
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        prompt=user_input,
    )

    user_input_embedding = response.choices[0].text

    symptoms = Symptom.query.all()
    embedded_symptoms = [np.fromstring(symptom.embedded_description[1:-1], sep=', ') for symptom in symptoms]

    similarities = [cosine_similarity([user_input_embedding], [symptom_embedding])[0][0]
                    for symptom_embedding in embedded_symptoms]
    
    return jsonify({'similarities': similarities}), 200