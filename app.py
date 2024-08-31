from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)
filename = 'svm_Heart_Disease_model.pkl'
model = pickle.load(open(filename, 'rb'))

# Define the feature names used during training
feature_names = ['age', 'sex', 'cp', 'ca', 'exang', 'thal']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input from the web form
    age = float(request.form.get('age'))
    sex = float(request.form.get('sex'))
    cp = float(request.form.get('cp'))
    ca = float(request.form.get('ca'))
    exang = float(request.form.get('exang'))
    thal = float(request.form.get('thal'))

    # Create a DataFrame with the same feature names as used during training
    features = pd.DataFrame([[age, sex, cp, ca, exang, thal]], columns=feature_names)

    # Predict the class using the model
    prediction = model.predict(features)[0]

    # Render a new web page with the prediction
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
