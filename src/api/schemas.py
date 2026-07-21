"""
Pydantic Schemas
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict

# ==========================================================
# Customer Input Schema
# ==========================================================

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


# ==========================================================
# Prediction Response
# ==========================================================

class PredictionResponse(BaseModel):
    prediction: str
    probability: float
    cluster: int
    recommendations: list[str]


# ==========================================================
# Home Response
# ==========================================================

class HomeResponse(BaseModel):
    message: str


# ==========================================================
# Health Response
# ==========================================================

class HealthResponse(BaseModel):
    status: str


# ==========================================================
# Prediction History Response
# ==========================================================

class PredictionHistoryResponse(BaseModel):
    id: int
    prediction: str
    probability: float
    cluster: int
    recommendations: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================================
# Prediction Count Response
# ==========================================================

class PredictionCountResponse(BaseModel):
    total_predictions: int