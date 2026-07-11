import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import joblib
import pandas as pd

from src.recommendation.recommendation_engine import recommend

"""
Prediction Module
-----------------
Loads trained models and performs:
1. Churn Prediction
2. Churn Probability
3. Customer Segmentation
4. Recommendation Generation
"""

from pathlib import Path
import joblib
import pandas as pd

from src.recommendation.recommendation_engine import recommend

# ============================================================
# Project Root
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ============================================================
# Load Models
# ============================================================

MODEL = joblib.load(
    PROJECT_ROOT / "models" / "best_model" / "churn_prediction_model.pkl"
)

PREPROCESSOR = joblib.load(
    PROJECT_ROOT / "models" / "preprocessors" / "preprocessing_pipeline.pkl"
)

KMEANS = joblib.load(
    PROJECT_ROOT / "models" / "segmentation" / "kmeans_model.pkl"
)

SCALER = joblib.load(
    PROJECT_ROOT / "models" / "segmentation" / "scaler.pkl"
)

# ============================================================
# Prediction Function
# ============================================================

def predict_customer(customer: dict):

    """
    Parameters
    ----------
    customer : dict

    Returns
    -------
    dict
    """

    df = pd.DataFrame([customer])

    # -------------------------------
    # Churn Prediction
    # -------------------------------

    X = PREPROCESSOR.transform(df)

    prediction = MODEL.predict(X)[0]

    probability = MODEL.predict_proba(X)[0][1]

    prediction_label = "Yes" if prediction == 1 else "No"

    # -------------------------------
    # Customer Segmentation
    # -------------------------------

    segmentation_features = df[
        [
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
        ]
    ]

    segmentation_scaled = SCALER.transform(segmentation_features)

    cluster = int(KMEANS.predict(segmentation_scaled)[0])

    # -------------------------------
    # Recommendation Engine
    # -------------------------------

    if prediction_label == "Yes":

        recommendations = recommend(customer)

    else:

        recommendations = [
            "Customer is currently low risk.",
            "Maintain regular engagement.",
            "Continue providing quality service."
        ]

    # -------------------------------
    # Output
    # -------------------------------

    return {

        "Prediction": prediction_label,

        "Probability": round(float(probability), 4),

        "Cluster": cluster,

        "Recommendations": recommendations

    }