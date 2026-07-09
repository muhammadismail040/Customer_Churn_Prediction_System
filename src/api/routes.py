from fastapi import APIRouter

from src.api.schemas import (
    CustomerData,
    PredictionResponse,
    HealthResponse,
    HomeResponse,
)

from src.api.predictor import predict_customer

router = APIRouter()


@router.get("/", response_model=HomeResponse)
def home():
    """
    Home Endpoint
    """
    return {
        "message": "Customer Churn Prediction API Running"
    }


@router.get("/health", response_model=HealthResponse)
def health():
    """
    Health Check Endpoint
    """
    return {
        "status": "Healthy"
    }


@router.post(
    "/predict",
    response_model=PredictionResponse,
    tags=["Prediction"]
)
def predict(customer: CustomerData):
    """
    Predict customer churn, customer segment,
    and generate recommendations.
    """

    result = predict_customer(customer.model_dump())

    return result