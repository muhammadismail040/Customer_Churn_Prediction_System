# Customer Churn Prediction API Documentation

## Overview

This REST API provides customer churn prediction using the trained Gradient Boosting model.

It also performs customer segmentation and generates personalized retention recommendations.

---

# Base URL

```
http://127.0.0.1:8000
```

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

# Endpoints

## GET /

Returns API status.

Response

```json
{
    "message":"Customer Churn Prediction API Running"
}
```

---

## GET /health

Checks API health.

```json
{
    "status":"Healthy"
}
```

---

## POST /predict

Predict customer churn.

### Request

```json
{
  "gender":"Female",
  "SeniorCitizen":0,
  "Partner":"Yes",
  "Dependents":"No",
  "tenure":12,
  "PhoneService":"Yes",
  "MultipleLines":"No",
  "InternetService":"Fiber optic",
  "OnlineSecurity":"No",
  "OnlineBackup":"Yes",
  "DeviceProtection":"No",
  "TechSupport":"No",
  "StreamingTV":"Yes",
  "StreamingMovies":"Yes",
  "Contract":"Month-to-month",
  "PaperlessBilling":"Yes",
  "PaymentMethod":"Electronic check",
  "MonthlyCharges":79.5,
  "TotalCharges":954
}
```

### Response

```json
{
  "prediction":"Yes",
  "probability":0.85,
  "cluster":2,
  "recommendations":[
      "Provide loyalty offers for new customers."
  ]
}
```

---

# Response Fields

| Field | Description |
|--------|-------------|
| prediction | Customer churn prediction |
| probability | Model confidence |
| cluster | Customer segment |
| recommendations | Personalized retention suggestions |

---

# Technologies

- FastAPI
- Pydantic
- Scikit-Learn
- Joblib

---