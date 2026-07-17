# Customer Churn Prediction API Documentation

## Overview

The Customer Churn Prediction API is built using FastAPI and provides secure endpoints for predicting customer churn, customer segmentation, and personalized retention recommendations.

**Base URL**

```
http://127.0.0.1:8000
```

---

# Authentication

The `/predict` endpoint is protected using API Key Authentication.

## Header

| Header | Value |
|---------|-------|
| x-api-key | customer_churn_ml_api_2026 |

Example:

```http
x-api-key: customer_churn_ml_api_2026
```

If the API Key is missing or invalid, the API returns:

```json
{
    "detail": "Invalid API Key."
}
```

Status Code:

```
401 Unauthorized
```

---

# Endpoints

## Home

### GET /

Returns API status.

Response

```json
{
    "message": "Customer Churn Prediction API Running"
}
```

---

## Health Check

### GET /health

Response

```json
{
    "status": "Healthy"
}
```

---

## Predict Customer

### POST /predict

Headers

```http
x-api-key: customer_churn_ml_api_2026
Content-Type: application/json
```

Request Body

```json
{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.5,
    "TotalCharges": 427.5
}
```

Successful Response

```json
{
    "prediction": "Yes",
    "probability": 0.91,
    "cluster": 2,
    "recommendations": [
        "Offer discount for yearly contract.",
        "Recommend Tech Support service."
    ]
}
```

---

# Response Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 401 | Invalid or Missing API Key |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# Interactive Documentation

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# Version

Current Version

```
v1.1.0
```