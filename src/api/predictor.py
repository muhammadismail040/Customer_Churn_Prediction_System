"""
Prediction Module

This module:

1. Predicts customer churn
2. Predicts customer segment
3. Generates personalized recommendations
"""

import pandas as pd

from src.api.model_loader import (
    model,
    preprocessor,
    target_encoder,
    kmeans_model,
    scaler,
)

from src.utils.logger import (
    prediction_logger,
    error_logger,
)


# ==========================================================
# Helpers
# ==========================================================

def _normalize_customer_keys(customer: dict) -> dict:
    """
    Normalize incoming keys so case differences
    (e.g. 'Tenure' vs 'tenure') don't break lookups.
    Maps to the exact key names the model/pipeline expects.
    """

    expected_keys = [
        "gender", "SeniorCitizen", "Partner", "Dependents",
        "tenure", "PhoneService", "MultipleLines",
        "InternetService", "OnlineSecurity", "OnlineBackup",
        "DeviceProtection", "TechSupport", "StreamingTV",
        "StreamingMovies", "Contract", "PaperlessBilling",
        "PaymentMethod", "MonthlyCharges", "TotalCharges",
    ]

    # build a lowercase lookup of whatever came in
    lower_map = {k.lower(): v for k, v in customer.items()}

    normalized = {}
    missing = []

    for key in expected_keys:
        if key.lower() in lower_map:
            normalized[key] = lower_map[key.lower()]
        else:
            missing.append(key)

    if missing:
        raise ValueError(
            f"Missing required field(s): {', '.join(missing)}"
        )

    return normalized


def _validate_and_cast(customer: dict) -> dict:
    """
    Validate and cast numeric fields.
    Raises clear, specific errors instead of
    letting pandas/sklearn throw cryptic ones.
    """

    # tenure must be a non-negative integer
    try:
        tenure = int(customer["tenure"])
    except (ValueError, TypeError):
        raise ValueError("tenure must be a whole number.")

    if tenure < 0:
        raise ValueError("tenure cannot be negative.")

    customer["tenure"] = tenure

    # MonthlyCharges must be a non-negative float
    try:
        monthly = float(customer["MonthlyCharges"])
    except (ValueError, TypeError):
        raise ValueError("MonthlyCharges must be a number.")

    if monthly < 0:
        raise ValueError("MonthlyCharges cannot be negative.")

    customer["MonthlyCharges"] = monthly

    # TotalCharges: handle empty strings / blanks gracefully
    total_raw = customer.get("TotalCharges", "")

    if isinstance(total_raw, str) and total_raw.strip() == "":
        # common real-world case: brand new customers have blank TotalCharges
        customer["TotalCharges"] = 0.0
    else:
        try:
            customer["TotalCharges"] = float(total_raw)
        except (ValueError, TypeError):
            raise ValueError("TotalCharges must be a number.")

    if customer["TotalCharges"] < 0:
        raise ValueError("TotalCharges cannot be negative.")

    return customer


# ==========================================================
# Recommendation Engine
# ==========================================================

def generate_recommendations(data):
    """
    Generate personalized recommendations
    based on customer information.
    """

    recommendations = []

    if data["Contract"] == "Month-to-month":
        recommendations.append(
            "Offer discount for yearly contract."
        )

    if data["TechSupport"] == "No":
        recommendations.append(
            "Recommend Tech Support service."
        )

    if data["OnlineSecurity"] == "No":
        recommendations.append(
            "Recommend Online Security service."
        )

    if data["tenure"] < 12:
        recommendations.append(
            "Provide loyalty offers for new customers."
        )

    if data["InternetService"] == "Fiber optic":
        recommendations.append(
            "Offer premium internet support package."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Customer is low risk. Continue current services."
        )

    return recommendations


# ==========================================================
# Customer Prediction
# ==========================================================

def predict_customer(customer):
    """
    Predict customer churn,
    customer segment,
    and generate recommendations.
    """

    try:

        # normalize + validate input before touching the model
        customer = _normalize_customer_keys(customer)
        customer = _validate_and_cast(customer)

        df = pd.DataFrame([customer])

        X = preprocessor.transform(df)

        prediction = model.predict(X)[0]

        probability = model.predict_proba(X)[0][1]

        segment_features = df[
            ["tenure", "MonthlyCharges", "TotalCharges"]
        ]

        segment_scaled = scaler.transform(segment_features)

        cluster = int(
            kmeans_model.predict(segment_scaled)[0]
        )

        churn = target_encoder.inverse_transform(
            [prediction]
        )[0]

        recommendations = generate_recommendations(customer)

        result = {
            "prediction": churn,
            "probability": round(float(probability), 4),
            "cluster": cluster,
            "recommendations": recommendations,
        }

        prediction_logger.info(
            f"""
==================== Prediction ====================

Prediction      : {result['prediction']}
Probability     : {result['probability']}
Cluster         : {result['cluster']}

Recommendations:

- {'\n- '.join(result['recommendations'])}

====================================================
"""
        )

        return result

    except ValueError as ve:
        # validation errors: safe to show the real message to the user
        error_logger.exception("Prediction Validation Error")
        raise Exception(str(ve))

    except Exception as e:
        # unexpected errors: log full traceback, still surface message
        error_logger.exception("Prediction Error")
        raise Exception(f"Prediction failed: {e}")