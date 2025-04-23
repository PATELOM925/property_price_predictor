from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load models
scaler = joblib.load('models/scaler.pkl')
label_encoders = joblib.load('models/label_encoders.pkl')
rf_model = joblib.load('models/rf_model.pkl')

@app.route('/') 
def index():
    locations = list(label_encoders['Location'].classes_)
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    area = float(data['area']) 
    bedrooms = int(data['bedrooms'])
    bathrooms = int(data['bathrooms'])
    location = data['location']
    years_ahead = int(data['years_ahead'])

    # Encode and scale the input
    encoded_location = label_encoders['Location'].transform([location])[0]
    input_data = np.array([[area, bedrooms, bathrooms, encoded_location]])
    input_data_scaled = scaler.transform(input_data)

    # Predict the price
    current_price = rf_model.predict(input_data_scaled)[0]
    appreciation_rate = 0.07
    future_price = current_price * ((1 + appreciation_rate) ** years_ahead)

    return jsonify({
        'current_price': f"₹{current_price:,.2f}",
        'future_price': f"₹{future_price:,.2f}"
    })

if __name__ == '__main__':
    app.run(debug=True)
