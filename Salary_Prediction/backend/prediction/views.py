from django.shortcuts import render
import pickle
import numpy as np
import os
from django.conf import settings

# Construct absolute paths for model and label encoder
model_path = os.path.join(settings.BASE_DIR, "ml_model/salary_model.pkl")
encoder_path = os.path.join(settings.BASE_DIR, "ml_model/label_encoder.pkl")

# Load the saved model and LabelEncoder
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(encoder_path, "rb") as f:
    le = pickle.load(f)

def predict_salary(request):
    if request.method == "POST":
        # Get input values from the form
        years_experience = float(request.POST["experience"])
        education_level = request.POST["education"]

        # Encode education level
        education_encoded = le.transform([education_level])[0]

        # Prepare input as a 2D array
        input_features = np.array([[years_experience, education_encoded]])

        # Predict salary
        salary = model.predict(input_features)[0]

        return render(request, "index.html", {"salary": salary})
    
    return render(request, "index.html")
