"""
Database CRUD Operations
"""

from sqlalchemy.orm import Session

from src.database.models import PredictionHistory


# ==========================================================
# Save Prediction
# ==========================================================

def save_prediction(
    db: Session,
    customer: dict,
    result: dict,
):
    """
    Save prediction history into PostgreSQL.
    """

    prediction = PredictionHistory(

        gender=customer["gender"],
        senior_citizen=customer["SeniorCitizen"],
        partner=customer["Partner"],
        dependents=customer["Dependents"],

        tenure=customer["tenure"],

        phone_service=customer["PhoneService"],
        multiple_lines=customer["MultipleLines"],

        internet_service=customer["InternetService"],

        online_security=customer["OnlineSecurity"],
        online_backup=customer["OnlineBackup"],
        device_protection=customer["DeviceProtection"],
        tech_support=customer["TechSupport"],

        streaming_tv=customer["StreamingTV"],
        streaming_movies=customer["StreamingMovies"],

        contract=customer["Contract"],

        paperless_billing=customer["PaperlessBilling"],

        payment_method=customer["PaymentMethod"],

        monthly_charges=customer["MonthlyCharges"],
        total_charges=customer["TotalCharges"],

        prediction=result["prediction"],
        probability=result["probability"],
        cluster=result["cluster"],

        recommendations="\n".join(
            result["recommendations"]
        ),
    )

    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction


# ==========================================================
# Get All Predictions
# ==========================================================

def get_predictions(
    db: Session,
):
    """
    Get all prediction history.
    """

    return (
        db.query(PredictionHistory)
        .order_by(PredictionHistory.id.desc())
        .all()
    )


# ==========================================================
# Get Prediction By ID
# ==========================================================

def get_prediction_by_id(
    db: Session,
    prediction_id: int,
):
    """
    Get prediction by ID.
    """

    return (
        db.query(PredictionHistory)
        .filter(
            PredictionHistory.id == prediction_id
        )
        .first()
    )


# ==========================================================
# Get Latest Prediction
# ==========================================================

def get_latest_prediction(
    db: Session,
):
    """
    Get latest prediction.
    """

    return (
        db.query(PredictionHistory)
        .order_by(
            PredictionHistory.id.desc()
        )
        .first()
    )


# ==========================================================
# Get Prediction Count
# ==========================================================

def get_prediction_count(
    db: Session,
):
    """
    Get total prediction count.
    """

    return db.query(PredictionHistory).count()


# ==========================================================
# Delete Prediction
# ==========================================================

def delete_prediction(
    db: Session,
    prediction_id: int,
):
    """
    Delete prediction by ID.
    """

    prediction = (
        db.query(PredictionHistory)
        .filter(
            PredictionHistory.id == prediction_id
        )
        .first()
    )

    if prediction is None:
        return None

    db.delete(prediction)
    db.commit()

    return prediction