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

    except Exception as e:

        error_logger.exception("Prediction Error")

        raise Exception(
            f"Prediction failed: {e}"
        )