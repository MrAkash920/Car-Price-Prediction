from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib  # For loading your trained model

app = Flask(__name__)

# Load your trained model and scaler
model = joblib.load('model.pkl')  # Load your trained model here
scaler = joblib.load('scaler.pkl')  # Load your scaler here

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input from the form
        year = int(request.form['year'])
        present_price = float(request.form['present_price'])
        kms_driven = int(request.form['kms_driven'])
        fuel_type = int(request.form['fuel_type'])  # Encode the fuel type as 0, 1, or 2
        seller_type = int(request.form['seller_type'])  # Encode the seller type as 0 or 1
        transmission = int(request.form['transmission'])  # Encode the transmission type as 0 or 1
        owner = int(request.form['owner'])

        # Create a numpy array with user input data
        input_data = np.array([[year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]])

        # Scale the input data using the scaler
        input_data = scaler.transform(input_data)

        # Make a prediction using the model
        predicted_price = model.predict(input_data)

        return render_template('index.html', prediction=f'Predicted Price: {predicted_price[0]:.2f}')

if __name__ == "__main__":
    app.run(debug =False, host='0.0.0.0', port=8080)

