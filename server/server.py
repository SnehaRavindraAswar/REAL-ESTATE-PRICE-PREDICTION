from flask import Flask, request, jsonify
from flask_cors import CORS
import util

# Initialize the Flask app first
app = Flask(__name__)

# Apply CORS after initializing the app
CORS(app) 

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])  
def predict_home_price():
    # Expecting JSON data in the request body
    data = request.get_json()  # Extract JSON data from the request

    # Extract fields from the JSON payload
    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    # Predict the price using the util function
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow cross-origin requests
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # Load your saved model artifacts
    app.run()
