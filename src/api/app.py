from fastapi import FastAPI

from src.api.routes import router

app = FastAPI(
    title="Customer Churn Prediction API",
    description="""
Customer Churn Prediction and Recommendation System API.

Features:
- Customer Churn Prediction
- Customer Segmentation
- Personalized Recommendation Engine
""",
    version="1.0.0",
)

app.include_router(router)