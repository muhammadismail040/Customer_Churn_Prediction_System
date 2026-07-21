"""
API Routes
"""

from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from src.api.auth import verify_api_key
from src.api.schemas import (
    CustomerData,
    PredictionResponse,
    HealthResponse,
    HomeResponse,
    PredictionHistoryResponse,
    PredictionCountResponse,
)
from src.api.predictor import predict_customer

from src.database.database import get_db
from src.database.crud import (
    save_prediction,
    get_predictions,
    get_prediction_by_id,
    get_latest_prediction,
    get_prediction_count,
    delete_prediction,
)

router = APIRouter()

# ==========================================================
# Home Endpoint
# ==========================================================

@router.get(
    "/",
    response_model=HomeResponse,
    tags=["General"],
)
def home():
    """
    Home Endpoint
    """
    return {
        "message": "Customer Churn Prediction API Running"
    }


# ==========================================================
# Health Endpoint
# ==========================================================

@router.get(
    "/health",
    response_model=HealthResponse,
    tags=["General"],
)
def health():
    """
    Health Check Endpoint
    """
    return {
        "status": "Healthy"
    }


# ==========================================================
# Prediction Endpoint
# ==========================================================

@router.post(
    "/predict",
    response_model=PredictionResponse,
    tags=["Prediction"],
)
def predict(
    customer: CustomerData,
    db: Session = Depends(get_db),
    _: str = Depends(verify_api_key),
):
    """
    Predict customer churn, customer segment,
    and generate personalized recommendations.
    """

    try:

        result = predict_customer(
            customer.model_dump()
        )

        save_prediction(
            db=db,
            customer=customer.model_dump(),
            result=result,
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================================================
# Get All Predictions
# ==========================================================

@router.get(
    "/predictions",
    response_model=List[PredictionHistoryResponse],
    tags=["Prediction History"],
)
def all_predictions(
    db: Session = Depends(get_db),
):
    """
    Get all prediction history.
    """
    return get_predictions(db)


# ==========================================================
# Get Latest Prediction
# ==========================================================

@router.get(
    "/predictions/latest",
    response_model=PredictionHistoryResponse,
    tags=["Prediction History"],
)
def latest_prediction(
    db: Session = Depends(get_db),
):
    """
    Get latest prediction.
    """

    prediction = get_latest_prediction(db)

    if prediction is None:
        raise HTTPException(
            status_code=404,
            detail="No prediction history found.",
        )

    return prediction


# ==========================================================
# Prediction Count
# ==========================================================

@router.get(
    "/predictions/count",
    response_model=PredictionCountResponse,
    tags=["Prediction History"],
)
def prediction_count(
    db: Session = Depends(get_db),
):
    """
    Get total number of predictions.
    """

    return {
        "total_predictions": get_prediction_count(db)
    }


# ==========================================================
# Get Prediction By ID
# ==========================================================

@router.get(
    "/predictions/{prediction_id}",
    response_model=PredictionHistoryResponse,
    tags=["Prediction History"],
)
def prediction_by_id(
    prediction_id: int,
    db: Session = Depends(get_db),
):
    """
    Get prediction by ID.
    """

    prediction = get_prediction_by_id(
        db,
        prediction_id,
    )

    if prediction is None:
        raise HTTPException(
            status_code=404,
            detail="Prediction not found.",
        )

    return prediction


# ==========================================================
# Delete Prediction
# ==========================================================

@router.delete(
    "/predictions/{prediction_id}",
    tags=["Prediction History"],
)
def remove_prediction(
    prediction_id: int,
    db: Session = Depends(get_db),
):
    """
    Delete prediction by ID.
    """

    prediction = delete_prediction(
        db,
        prediction_id,
    )

    if prediction is None:
        raise HTTPException(
            status_code=404,
            detail="Prediction not found.",
        )

    return {
        "message": "Prediction deleted successfully."
    }