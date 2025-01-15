from django.shortcuts import render
from .ml_model import predict_heart_disease

def predict_view(request):
    result = None  # Initialize result as None for GET requests

    if request.method == 'POST':
        # Get the user inputs from the form
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        cp = int(request.POST.get('cp'))
        trestbps = int(request.POST.get('trestbps'))
        chol = int(request.POST.get('chol'))
        fbs = int(request.POST.get('fbs'))
        restecg = int(request.POST.get('restecg'))
        thalch = int(request.POST.get('thalch'))
        exang = int(request.POST.get('exang'))
        oldpeak = float(request.POST.get('oldpeak'))

        # Prepare the data for prediction
        features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalch, exang, oldpeak]]

        # Make prediction
        result = predict_heart_disease(features)

    # Render the page with the result (if any)
    return render(request, 'index.html', {'result': result})
