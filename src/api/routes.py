"""
API Routes
"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from src.api.auth import verify_api_key

from src.api.schemas import (
    CustomerData,
    PredictionResponse,
    HealthResponse,
    HomeResponse,
)

from src.api.predictor import predict_customer

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

    print("✅ Home endpoint called")

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

    print("✅ Health endpoint called")

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
    _: str = Depends(verify_api_key),
):
    """
    Predict customer churn,
    customer segment,
    and generate personalized retention recommendations.
    """

    print("=" * 60)
    print("✅ PREDICT ENDPOINT EXECUTED")
    print("Customer Data:")
    print(customer.model_dump())
    print("=" * 60)

    try:

        result = predict_customer(
            customer.model_dump()
        )

        print("=" * 60)
        print("Prediction Result:")
        print(result)
        print("=" * 60)

        return result

    except Exception as e:

        print("=" * 60)
        print("❌ Prediction Error")
        print(e)
        print("=" * 60)

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )