# test_api.py
import requests

URL = "http://127.0.0.1:8000/predict"

sample = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": 845.5,
}

try:
    r = requests.post(URL, json=sample, timeout=10)
    print("Status Code:", r.status_code)
    try:
        print("Response JSON:", r.json())
    except Exception:
        print("Response Text:", r.text)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
