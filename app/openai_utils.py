import json
from flask import Flask, jsonify, request
import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.models import Symptom

openai.api_key = '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'

def embed_input(user_input: list):
    combined_input = ' '.join(user_input)
    embeddings_dict = openai.Embedding.create(
        input=combined_input, 
        model="text-embedding-ada-002")["data"]
        
    return embeddings_dict[0]['embedding']
    
def predict_disease_from_similarities(similarities):
    threshold_value = 0.8  # Setting threshold value

    sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

    for symptom_index, similarity in enumerate(sorted_similarities):
        if similarity > threshold_value:
            predicted_disease = get_disease_from_symptom_index(symptom_index)
            return predicted_disease

    return "Unknown Disease"

def ranker(similarities):
    threshold_value = 0.7  # Setting threshold value
    symptoms =[
        "Common Cold",
        "Hypoglycemia",
        "Malaria",
        "peptic ulcer disease",
        "Typhoid",
        "Urinary tract infection",
        "Depression"
    ]
    idx = np.argpartition(similarities[0], -5, )[-5:]
    indices = idx[np.argsort((-similarities[0])[idx])]
    highest_similarity = similarities[0][indices[0]]
    if highest_similarity < threshold_value:
        return "Not enough symptoms"
    similar_symptoms_list = []
    similar_symptoms_list_1=[]

    for index in indices:
        #print(f'THE CLOSEST QUESTION IS {questions[index]}')
        similar_symptoms_list.append(symptoms[index])
        similar_symptoms_list_1.append(symptoms[index])
    similar_symptoms_list=list(dict.fromkeys(similar_symptoms_list))
    rank_list =[]
    for item in similar_symptoms_list:
        indx=similar_symptoms_list_1.index(item)
        #similar_answers_list = list(dict.fromkeys(similar_answers_list))
        rank_list.append(similar_symptoms_list[indx])
        
    return rank_list[0]

def get_disease_from_symptom_index(symptom_index):
    # mapping logic
    mapping = {
        1: "Common Cold",
        2: "Hypoglycemia",
        3: "Malaria",
        4: "peptic ulcer disease",
        5: "Typhoid",
        6: "Urinary tract infection",
        7: "Depression"
    }
    return mapping.get(symptom_index, "Unknown Disease")