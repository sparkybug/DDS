from flask import jsonify
from app.app import app
from app import routes, models 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/predict-disease/', methods=['POST'])
def predict_disease():
    predicted_disease = routes.predict_disease()

    return jsonify({'predicted_disease': predicted_disease}), 200

if __name__ == '__main__':
    app.run(debug=True)  