from flask import jsonify
from app.app import app
from app import openai_utils
from app import routes, models

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/predict-disease', methods=['POST'])
def predict_disease(similarities):
    # predicted_disease = routes.predict_diseases()
    # Predict disease based on similarities
    similarities = routes.predict_diseases()
    predicted_disease = openai_utils.ranker(similarities)
        
    return jsonify({'predicted_disease': predicted_disease}), 200
    # return routes.predict_diseases()

if __name__ == '__main__':
    app.run(debug=True)  