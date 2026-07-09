import pandas as pd

from src.api.model_loader import (
    model,
    preprocessor,
    target_encoder,
    kmeans_model,
    scaler,
)


def generate_recommendations(data):
    """
    Generate recommendations based on customer information.
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


def predict_customer(customer):

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

    return {
        "prediction": churn,
        "probability": round(float(probability), 4),
        "cluster": cluster,
        "recommendations": recommendations,
    }