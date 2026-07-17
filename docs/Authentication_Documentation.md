# Authentication Documentation

## Overview

The Customer Churn Prediction API uses API Key Authentication to protect sensitive endpoints. Only authorized users with a valid API key can access the prediction endpoint.

---

## Authentication Method

The API uses a custom header for authentication.

Header Name:

```text
x-api-key
```

---

## API Key

During development:

```text
customer_churn_ml_api_2026
```

The API key is stored securely in the `.env` file.

Example:

```env
API_KEY=customer_churn_ml_api_2026
```

---

## Protected Endpoint

| Method | Endpoint | Authentication |
|---------|----------|----------------|
| POST | /predict | Required |

---

## Public Endpoints

| Method | Endpoint |
|---------|----------|
| GET | / |
| GET | /health |

---

## Swagger Authentication

Swagger UI supports API Key Authentication.

Steps:

1. Open Swagger Documentation

```
http://127.0.0.1:8000/docs
```

2. Click the **Authorize** button.

3. Enter the API key:

```
customer_churn_ml_api_2026
```

4. Click **Authorize**.

5. Execute protected endpoints.

---

## Success Response

```http
HTTP/1.1 200 OK
```

---

## Missing API Key

```http
HTTP/1.1 401 Unauthorized
```

Response

```json
{
    "detail": "API Key is missing."
}
```

---

## Invalid API Key

```http
HTTP/1.1 401 Unauthorized
```

Response

```json
{
    "detail": "Invalid API Key."
}
```

---

## Security Features

- API Key stored in environment variables
- Request validation using FastAPI Security
- Unauthorized requests blocked
- Swagger Authorization support
- Production-ready authentication mechanism