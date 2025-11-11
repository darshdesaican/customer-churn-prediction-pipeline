# app_pipeline.py
# run the command " uvicorn app:app --reload " in powershell to start the server
import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

MODEL_PATH = os.path.join("models", "churn_pipeline.pkl")

# Load pipeline (raises error if missing)
pipeline = None
if os.path.exists(MODEL_PATH):
    pipeline = joblib.load(MODEL_PATH)
    print("✅ Loaded pipeline:", MODEL_PATH)
else:
    print("⚠️ Pipeline not found; run train.py first to create models/churn_pipeline.pkl")

app = FastAPI(title="Customer Churn Prediction API", version="1.0")


class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def read_root():
    return {"message": "Customer Churn Prediction API is running."}


@app.post("/predict")
def predict(data: CustomerData):
    if pipeline is None:
        raise HTTPException(
            status_code=500, detail="Model pipeline not found. Run train.py first."
        )
    try:
        df = pd.DataFrame([data.dict()])
        # pipeline handles encoding + scaling + predict_proba
        prob = pipeline.predict_proba(df)[0][1]
        pred = "Yes" if prob >= 0.5 else "No"
        return {"churn_prediction": pred, "churn_probability": round(float(prob), 4)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")