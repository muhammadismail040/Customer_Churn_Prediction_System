# Postman Guide

# Customer Churn Prediction & Recommendation System

---

# Authentication

Header

```
x-api-key
```

Value

```
customer_churn_ml_api_2026
```

---

# Available Endpoints

## GET /

Home endpoint

---

## GET /health

Health check

---

## POST /predict

Predict customer churn.

---

## GET /predictions

Returns prediction history.

---

## GET /predictions/latest

Returns latest prediction.

---

## GET /predictions/count

Returns total predictions.

---

## GET /predictions/{id}

Returns prediction by ID.

---

## DELETE /predictions/{id}

Deletes prediction.

---

# Import Collection

Open Postman

Import

Select

```
Customer_Churn_API.postman_collection.json
```

---

# Test API

Use Swagger

```
http://127.0.0.1:8000/docs
```