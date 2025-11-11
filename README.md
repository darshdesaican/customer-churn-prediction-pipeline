# 📊 Customer Churn Prediction (End-to-End ML Project)

![CI](https://github.com/darshadesaican/customer-churn-prediction/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/darshdesaican/customer-churn-prediction/branch/main/graph/badge.svg)](https://codecov.io/gh/darshdesaican/customer-churn-prediction)
![Security](https://img.shields.io/badge/security-scanned-brightgreen)



This project demonstrates an end-to-end machine learning pipeline for predicting customer churn.  
It includes data preprocessing, model training, REST API deployment with FastAPI, automated testing, Jupyter demo, and Docker packaging for easy deployment.

---

## 🚀 Features
- End-to-end **ML pipeline** in one file (`churn_pipeline.pkl`)  
- REST API with **FastAPI**  
- Automated testing using **pytest**  
- Interactive Jupyter demo notebook (`demo.ipynb`)  
- **Dockerized deployment** with `Dockerfile` + `docker-compose.yml`  
- Ready for deployment to **cloud platforms** (AWS, GCP, Azure, Render, Railway, etc.)

---

## 📂 Project Structure
```
customer-churn-prediction/
│── app.py                 # FastAPI app for predictions
│── train.py               # Trains and saves churn_pipeline.pkl
│── test_api.py            # Manual request test script
│── requirements.txt       # Python dependencies
│── README.md              # Documentation
│── demo.ipynb             # Jupyter demo
│── models/
│   └── churn_pipeline.pkl # Single pipeline (preprocessing + model)
│── tests/
    └── test_api.py        # pytest API tests
│── Dockerfile             # Docker build instructions
│── docker-compose.yml     # Docker compose config
```

---

## 📝 17 Steps (with Execution Instructions)

### **Step 1. Set up environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### **Step 2. Dataset preparation**
Place the dataset (`Telco-Customer-Churn.csv`) in your project root or `data/` folder.

### **Step 3. Explore the dataset (EDA)**
```bash
jupyter notebook demo.ipynb
```

### **Step 4. Train-test split**
Handled in `train.py` (splits data into training & testing sets).

### **Step 5. Preprocessing**
- `OneHotEncoder` for categorical features
- `StandardScaler` for numeric features

### **Step 6. Build pipeline**
Combine preprocessing + model into one **Pipeline**.

### **Step 7. Train pipeline**
```bash
python train.py
```
Saves model to `models/churn_pipeline.pkl`.

### **Step 8. Evaluate model**
Classification report printed during training.

### **Step 9. Save model**
Uses `joblib.dump` to save pipeline.

### **Step 10. Build API**
`app.py` loads `churn_pipeline.pkl` and exposes `/predict` endpoint.

### **Step 11. Run API**
```bash
uvicorn app:app --reload
```
Docs:  
- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  

### **Step 12. Example request**
POST `/predict` with JSON:
```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 5,
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
  "TotalCharges": 350.5
}
```

Response:
```json
{
  "prediction": "Yes",
  "probability": 0.83
}
```

### **Step 13. Test API manually**
```bash
python test_api.py
```

### **Step 14. Automated tests with pytest**
```bash
pytest -v -s
```

### **Step 15. Jupyter demo**
```bash
jupyter notebook demo.ipynb
```

### **Step 16. Docker build**
```bash
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

### **Step 17. Docker Compose**
```bash
docker-compose up --build
```

---

## 🐳 Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🐳 docker-compose.yml
```yaml
version: "3.9"
services:
  churn-api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    restart: always
```

---

## 📌 Requirements
- Python 3.8+
- FastAPI
- scikit-learn
- joblib
- pandas, numpy, matplotlib
- requests
- pytest
- uvicorn
- docker (for containerization)

---

## ☁️ Cloud Deployment
This project is containerized → can be deployed to:
- AWS ECS / EKS / App Runner  
- GCP Cloud Run  
- Azure App Service  
- Render / Railway / Hugging Face Spaces  

---
