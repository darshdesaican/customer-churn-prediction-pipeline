import pandas as pd
import joblib
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import os

DATA_PATH = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "churn_pipeline.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)

# 1. Load data
df = pd.read_csv(DATA_PATH)

# 2. Basic cleaning
df = df.drop(columns=["customerID"], errors="ignore")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

# 3. Features & target
X = df.drop("Churn", axis=1)
y = df["Churn"].map({"Yes": 1, "No": 0})

# 4. Column types
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
numerical_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

# 5. Preprocessors
sklearn_version = tuple(int(x) for x in sklearn.__version__.split(".")[:2])
if sklearn_version >= (1, 2):
    categorical_transformer = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
else:
    categorical_transformer = OneHotEncoder(handle_unknown="ignore", sparse=False)
    
numerical_transformer = StandardScaler()

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", categorical_transformer, categorical_cols),
        ("num", numerical_transformer, numerical_cols),
    ]
)

# 6. Pipeline (preprocessor + model)
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("clf", RandomForestClassifier(n_estimators=200, random_state=42)),
    ]
)

# 7. Train/test split and fit
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

pipeline.fit(X_train, y_train)

# 8. Evaluation (simple)
acc = pipeline.score(X_test, y_test)
print(f"✅ Trained pipeline. Test accuracy: {acc:.4f}")

# 9. Save pipeline
joblib.dump(pipeline, MODEL_PATH)
print(f"💾 Saved pipeline to: {MODEL_PATH}")