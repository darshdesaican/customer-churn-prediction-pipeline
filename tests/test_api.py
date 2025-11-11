# tests/test_train.py
import os
import joblib
import pandas as pd
import pytest
from sklearn.pipeline import Pipeline

MODEL_PATH = "models/churn_pipeline.pkl"


def test_pipeline_exists():
    assert os.path.exists(MODEL_PATH), "Run `python train.py` to create the pipeline."


def test_pipeline_loads():
    pipeline = joblib.load(MODEL_PATH)
    assert isinstance(pipeline, Pipeline)


def test_pipeline_predict_shape():
    pipeline = joblib.load(MODEL_PATH)
    # prepare a synthetic sample that matches expected columns by training data
    # Here we attempt to build a sample with typical values; adjust if your dataset differs
    sample = pd.DataFrame(
        [
            {
                "gender": "Female",
                "SeniorCitizen": 0,
                "Partner": "No",
                "Dependents": "No",
                "tenure": 1,
                "PhoneService": "Yes",
                "MultipleLines": "No",
                "InternetService": "DSL",
                "OnlineSecurity": "No",
                "OnlineBackup": "No",
                "DeviceProtection": "No",
                "TechSupport": "No",
                "StreamingTV": "No",
                "StreamingMovies": "No",
                "Contract": "Month-to-month",
                "PaperlessBilling": "Yes",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 29.85,
                "TotalCharges": 29.85,
            }
        ]
    )
    pred = pipeline.predict(sample)
    assert pred.shape == (1,)
