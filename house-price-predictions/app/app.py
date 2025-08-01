from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__, template_folder='templates')

# Get base dir of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct paths to model and features
MODEL_PATH = os.path.join(BASE_DIR, 'house_price_model.pkl')
FEATURES_PATH = os.path.join(BASE_DIR, 'selected_features.pkl')

# Load model and selected features
model = joblib.load(MODEL_PATH)
selected_features = joblib.load(FEATURES_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)
        print("Expected features:", selected_features)
        input_values = [float(data[feature]) for feature in selected_features]
        input_array = np.array(input_values).reshape(1, -1)
        predicted_price = model.predict(input_array)[0]
        return jsonify({'predicted_price': round(predicted_price, 2)})
    except Exception as e:
        print("Prediction error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
