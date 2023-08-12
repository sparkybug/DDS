from flask import request, jsonify
from app import app, openai_utils

@app.route('/api/embed-symptoms', methods=['POST'])
def embed_symptoms():
    user_input = request.json.get("userInput")
    embedded_input = openai_utils.embed_input(user_input)
    return jsonify({'embedded_input': embedded_input})


@app.route('/api/get-similar-symptoms/<int:disease_id>', methods=['GET'])
def get_similar_symptoms(disease_id):
    similar_symptoms = openai_utils.calculate_similarity(disease_id)
    return jsonify({'similar_symptoms': similar_symptoms})
