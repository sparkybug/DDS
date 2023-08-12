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

    return embeddings
    
    # return response.choices[0].text.strip()

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