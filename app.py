from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

# Initialize Flask app
app = Flask(__name__)

# Load models, scalers, and encoders
with open("ensemble_model1.pkl", "rb") as diabetes_model_file:
    diabetes_model = pickle.load(diabetes_model_file)

with open("random_forest_model.pkl", "rb") as mental_model_file:
    mental_model = pickle.load(mental_model_file)

with open("ensemble_model.pkl", "rb") as cardio_model_file:
    cardio_model = pickle.load(cardio_model_file)

with open("scaler2.pkl", "rb") as diabetes_scaler_file:
    diabetes_scaler = pickle.load(diabetes_scaler_file)

with open("scaler1.pkl", "rb") as mental_scaler_file:
    mental_scaler = pickle.load(mental_scaler_file)

with open("scaler.pkl", "rb") as cardio_scaler_file:
    cardio_scaler = pickle.load(cardio_scaler_file)

with open("label_encoders.pkl", "rb") as label_encoder_file:
    label_encoders = pickle.load(label_encoder_file)

with open("target_encoder.pkl", "rb") as target_encoder_file:
    target_encoder = pickle.load(target_encoder_file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

@app.route("/mentalillness")
def mentalillness():
    return render_template("mentalillness.html")

@app.route("/cardiovascular")
def cardiovascular():
    return render_template("cardiovascular.html")

@app.route("/respiratory")
def respiratory():
    return render_template("respiratory.html")

@app.route("/predict/diabetes", methods=["POST"])
def predict_diabetes():
    # Collect patient data for diabetes
    patient_data = [
        int(request.form["pregnancies"]),
        float(request.form["glucose"]),
        float(request.form["bloodpressure"]),
        float(request.form["skinthickness"]),
        float(request.form["insulin"]),
        float(request.form["bmi"]),
        float(request.form["diabetespedigreefunction"]),
        int(request.form["age"]),
    ]

    # Scale and predict
    patient_data_scaled = diabetes_scaler.transform([patient_data])
    probability = diabetes_model.predict_proba(patient_data_scaled)[0][1]
    prediction = diabetes_model.predict(patient_data_scaled)[0]

    result = "likely to have diabetes" if prediction == 1 else "unlikely to have diabetes"
    features = [
        "Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness", "Insulin", 
        "BMI", "Diabetes Pedigree Function", "Age"
    ]

    plot_url = create_bar_plot(features, patient_data, f"Patient Data - {result} ({probability * 100:.2f}% probability)")
    return render_template("diabetes_result.html", result=result, probability=probability * 100, plot_url=plot_url)

@app.route("/predict/mentalillness", methods=["POST"])
def predict_mentalillness():
    feature_mapping = {
        "Age": "Age",
        "Marital_Status": "Marital_Status",
        "Education_Level": "Education_Level",
        "Number_of_Children": "Number_of_Children",
        "Smoking_Status": "Smoking_Status",
        "Physical_Activity_Level": "Physical_Activity_Level",
        "Employment_Status": "Employment_Status",
        "Income": "Income",
        "Alcohol_Consumption": "Alcohol_Consumption",
        "Dietary_Habits": "Dietary_Habits",
        "Sleep_Patterns": "Sleep_Patterns",
        "History_of_Substance_Abuse": "History_of_Substance_Abuse",
        "Family_History_of_Depression": "Family_History_of_Depression",
        "Chronic_Medical_Conditions": "Chronic_Medical_Conditions"
    }

    patient_data = {}
    for form_field, model_field in feature_mapping.items():
        value = request.form.get(form_field)
        patient_data[model_field] = int(value) if value and value.isdigit() else float(value) if value else 0

    patient_data_df = pd.DataFrame([patient_data])
    patient_data_scaled = mental_scaler.transform(patient_data_df)
    prediction = mental_model.predict(patient_data_scaled)
    prediction_label = target_encoder.inverse_transform(prediction)[0]
    probability = mental_model.predict_proba(patient_data_scaled)[0][1]

    result = (
        f"likely to have a mental health condition ({probability * 100:.2f}%)"
        if prediction_label == 1
        else f"unlikely to have a mental health condition ({(1 - probability) * 100:.2f}%)"
    )

    values = list(patient_data.values())
    plot_url = create_bar_plot(list(patient_data.keys()), values, f"Patient Data - {result}")

    return render_template("mental_result.html", result=result, plot_url=plot_url)

@app.route("/predict/cardiovascular", methods=["POST"])
def predict_cardiovascular():
    patient_data = [
        int(request.form["age"]),
        int(request.form["sex"]),
        int(request.form["cp"]),
        int(request.form["trestbps"]),
        int(request.form["chol"]),
        int(request.form["fbs"]),
        int(request.form["restecg"]),
        int(request.form["thalach"]),
        int(request.form["exang"]),
        float(request.form["oldpeak"]),
        int(request.form["slope"]),
        int(request.form["ca"]),
        int(request.form["thal"]),
    ]

    patient_data_scaled = cardio_scaler.transform([patient_data])
    prediction = cardio_model.predict(patient_data_scaled)[0]
    probability = cardio_model.predict_proba(patient_data_scaled)[0][1]

    result = "likely to have heart disease" if prediction == 1 else "unlikely to have heart disease"

    features = [
        "Age", "Sex", "Chest Pain Type", "Resting BP", "Cholesterol", "Fasting Blood Sugar",
        "Resting ECG", "Max Heart Rate", "Exercise Induced Angina", "ST Depression", 
        "Slope", "Major Vessels", "Thal"
    ]
    plot_url = create_bar_plot(features, patient_data, f"Patient Data - {result} ({probability * 100:.2f}% probability)")

    return render_template("cardiovascular_result.html", result=result, probability=probability * 100, plot_url=plot_url)

def create_bar_plot(features, values, title):
    plt.figure(figsize=(12, 8))
    sns.barplot(x=features, y=values, palette="coolwarm", edgecolor="black")
    plt.title(title, fontsize=16, weight="bold")
    plt.xlabel("Patient Features")
    plt.ylabel("Values")
    plt.xticks(rotation=45, ha="right")

    for i, value in enumerate(values):
        plt.text(i, value + 0.05, round(value, 2), ha="center", va="bottom", fontsize=10)

    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return plot_url

if __name__ == "__main__":
    app.run(debug=True)
