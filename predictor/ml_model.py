import pickle
import numpy as np

# Load the model once
with open('ml_models/heart_disease_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_heart_disease(features):
    """
    Predicts if heart disease is present based on user input features.
    :param features: List of user input values [age, sex, cp, trestbps, chol, fbs, restecg, thalch, exang, oldpeak]
    :return: Boolean (True = Disease detected, False = No disease)
    """
    # Convert the list to a NumPy array and reshape it to (1, -1)
    features_array = np.array(features).reshape(1, -1)
    
    # Make the prediction
    prediction = model.predict(features_array)
    
    # Return the first element of the prediction array
    return prediction[0]
