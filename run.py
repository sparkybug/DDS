from app.app import app
from app import routes, models 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/predict-disease/', methods=['POST'])
def predict_disease():
    predicted_disease = routes.predict_diseases()

    return predicted_disease

if __name__ == '__main__':
    app.run(debug=True)  