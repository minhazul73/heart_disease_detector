import pickle
import os
import numpy as np

MODEL_PATH = os.path.join('../ml_models', 'heart_disease_model.pkl')

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

def predict_heart_disease(input_data):
    # Example: input_data = [age, gender, cholesterol, bp, diabetes]
    data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(data)
    return bool(prediction[0])
