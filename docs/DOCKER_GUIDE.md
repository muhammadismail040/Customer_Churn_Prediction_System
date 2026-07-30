# Docker Guide

# Customer Churn Prediction & Recommendation System

---

# Build Docker Image

```bash
docker build -t churn-backend .
```

---

# Run Container

```bash
docker run -d -p 8000:8000 --name churn-api churn-backend
```

---

# Docker Compose

```bash
docker compose up --build
```

---

# Stop Container

```bash
docker stop churn-api
```

---

# Remove Container

```bash
docker rm churn-api
```

---

# List Containers

```bash
docker ps
```

---

# View Logs

```bash
docker logs churn-api
```

---

# Verify Docker

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI should load successfully.

---

# Technologies Used

- Docker
- Docker Compose
- Python 3.12
- FastAPI
- PostgreSQL