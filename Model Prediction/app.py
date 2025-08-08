from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)


model = joblib.load('AGRISOL_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = int(request.form['area'])
        item = int(request.form['item'])
        year = int(request.form['year'])
        rainfall = float(request.form['rainfall'])
        pesticides = float(request.form['pesticides'])
        temperature = float(request.form['temperature'])

        features = np.array([[area, item, year, rainfall, pesticides, temperature]])
        prediction = model.predict(features)[0]

        return render_template('result.html', prediction=round(prediction, 2))

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
