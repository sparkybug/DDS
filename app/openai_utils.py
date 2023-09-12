import json
from flask import Flask, jsonify, request
import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.models import Symptom

openai.api_key = ''

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
        "The symptoms you've described align with those of a common cold, which is a viral infection that affects the upper respiratory system. Symptoms often include a runny or stuffy nose, sneezing, coughing, mild fatigue, and a scratchy throat. While a cold can be uncomfortable, the good news is that it's usually a mild and self-limiting condition. Here are a few steps you can take to manage your symptoms and support your recovery. Rest: Getting plenty of rest allows your body to focus on fighting off the virus and helps you recover more quickly. Stay Hydrated: Drink fluids like water, herbal tea, and clear broths to stay hydrated and soothe your throat. Over-the-Counter Remedies: You might consider using over-the-counter cold remedies, such as decongestants or throat lozenges, to relieve specific symptoms. Remember to follow the dosing instructions. Warm Saline Gargles: Gargling with warm saline water can help ease a sore throat and reduce irritation. Avoid Spreading the Virus: Since the common cold is contagious, it's a good idea to practice good hygiene, such as washing your hands frequently and covering your mouth and nose when you cough or sneeze. Monitor Your Symptoms: While a cold typically improves within a week, it's important to monitor your symptoms. If they worsen or if you develop a high fever, difficulty breathing, or other concerning symptoms, it's a good idea to consult a healthcare professional.",
        "Your symptoms align with hypoglycemia, which is low blood sugar. This can cause shakiness, sweating, dizziness, and confusion. To manage this, aim for regular meals and snacks, and avoid long gaps between eating. Keep glucose tablets or fast-acting carbs on hand for emergencies. Please consult your healthcare provider for a personalized plan.",
        "I hope you're doing as well as possible under the circumstances. Your symptoms suggest malaria, a mosquito-borne illness. High fever, chills, body aches, and fatigue are common. Immediate medical attention is crucial. Antimalarial medications will be prescribed to treat the infection. Rest and hydration are important too. Reach out to your healthcare provider for guidance tailored to your situation. Wishing you a speedy recovery.",
        "Your symptoms point towards peptic ulcer disease, which involves stomach or duodenal ulcers. These can cause abdominal pain, often described as burning or gnawing, sometimes relieved by eating. Your healthcare provider will guide you through managing this condition. Medications to reduce stomach acid and lifestyle changes can help. Please follow their recommendations closely and don't hesitate to reach out with any questions. Wishing you relief and recovery.",
        "The symptoms you described align with those of typhoid fever. Typhoid is caused by a bacterial infection and can lead to fever, weakness, stomach pain, and a range of other uncomfortable symptoms. It's important to address this condition promptly to ensure your recovery. The good news is that typhoid can be treated with appropriate medical care. Your healthcare provider will likely prescribe antibiotics to target the bacteria causing the infection. It's crucial to follow their instructions diligently and complete the full course of medication, even if you start feeling better. Additionally, staying hydrated and consuming a balanced diet can aid in your recovery process. Rest is also essential to help your body regain its strength. Please remember that recovery from typhoid takes time, and it's completely normal to feel fatigued during this period. If you experience any concerns or if your symptoms worsen, don't hesitate to reach out to your healthcare provider. They are there to address your questions and monitor your progress.",
        "I hope you're coping well. Your symptoms indicate a urinary tract infection (UTI), a common issue. Symptoms like frequent urination, burning sensation, and discomfort are typical. Swift treatment is essential. Your healthcare provider will prescribe antibiotics. Drinking water and maintaining hygiene can aid recovery. Feel free to ask any questions or concerns you have. Wishing you comfort and healing.",
        "I'm here to support you. Your symptoms align with depression, a challenging condition. Feelings of sadness, low energy, changes in sleep or appetite are common. Please know that help is available. Your healthcare provider can discuss therapy and possibly medication options. Reach out to them and consider involving loved ones in your journey to healing. Wishing you brighter days ahead."
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