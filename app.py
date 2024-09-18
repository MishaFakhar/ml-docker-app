from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, jsonify

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Train a basic model
model = RandomForestClassifier()
model.fit(X, y)

# Create a Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json['data']
    prediction = model.predict([input_data]).tolist()
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
