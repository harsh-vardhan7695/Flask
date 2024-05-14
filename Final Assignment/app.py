from flask import Flask, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model from the pickle file
with open('house_rent_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/homeplease', methods=['GET'])
def home():
    return "Welcome to the House Rent Prediction Flask Application!"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        try:
            test_data = pd.read_csv(file)
            # Preprocess the test data in the same way as the training data
            test_data = pd.get_dummies(test_data, drop_first=True)

            # Ensure all necessary columns are present (handle any missing columns)
            model_features = model.feature_names_in_
            for col in model_features:
                if col not in test_data.columns:
                    test_data[col] = 0

            test_data = test_data[model_features]

            # Make predictions
            predictions = model.predict(test_data)
            test_data['Predicted Rent'] = predictions
            return test_data.to_html()
        except Exception as e:
            return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)


