"""
FastAPI Application
Customer Churn Prediction & Recommendation System
"""

from contextlib import asynccontextmanager
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from src.api.routes import router
from src.database.database import create_tables
import src.database.models
from src.utils.logger import api_logger


# ============================================================
# Create Database Tables on Startup
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Create database tables when FastAPI starts.
    """

    create_tables()

    yield


# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    lifespan=lifespan,
    title="Customer Churn Prediction & Recommendation API",
    description="""
Customer Churn Prediction & Recommendation System

A production-ready Machine Learning REST API built with FastAPI.

## Features

- Customer Churn Prediction
- Churn Probability Estimation
- Customer Segmentation
- Personalized Retention Recommendations
- API Key Authentication
- Interactive Swagger Documentation
- ReDoc Documentation

## Authentication

Click the **Authorize** button and enter your API Key.

API Key:

customer_churn_ml_api_2026
""",
    version="1.1.0",
    contact={
        "name": "Muhammad Ismail",
        "url": "https://github.com/muhammadismail040",
    },
    license_info={
        "name": "MIT License",
    },
)

# ============================================================
# CORS Configuration
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# Include API Routes
# ============================================================

app.include_router(router)

# ============================================================
# Request Logging Middleware
# ============================================================

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Log every incoming API request.
    """

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    api_logger.info(
        f"{request.method} | "
        f"{request.url.path} | "
        f"{request.client.host} | "
        f"{response.status_code} | "
        f"{process_time:.4f} sec"
    )

    return response


# ============================================================
# Custom Swagger Authentication
# ============================================================

def custom_openapi():

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "APIKeyHeader": {
            "type": "apiKey",
            "in": "header",
            "name": "x-api-key",
        }
    }

    openapi_schema["security"] = [
        {
            "APIKeyHeader": []
        }
    ]

    app.openapi_schema = openapi_schema

    return app.openapi_schema


# ============================================================
# Register Custom OpenAPI
# ============================================================

app.openapi = custom_openapi