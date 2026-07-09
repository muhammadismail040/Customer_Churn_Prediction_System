# Customer Churn Prediction & Recommendation System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow)

---

# Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses such as telecom companies. This project develops an end-to-end Machine Learning solution capable of predicting customer churn, segmenting customers into meaningful groups, generating personalized retention recommendations, and exposing predictions through a production-ready REST API.

The project follows a complete Machine Learning workflow from raw data preprocessing to model deployment and is being developed as part of a **Machine Learning Engineering Internship**.

---

# Project Objectives

- Predict customer churn using Machine Learning
- Segment customers based on behavioral patterns
- Generate personalized customer retention recommendations
- Compare multiple Machine Learning models
- Select the best-performing model
- Build a production-ready REST API using FastAPI
- Provide interactive API documentation
- Build an interactive dashboard
- Deploy the project using Docker and Cloud services

---

# Dataset

### Dataset Name

**Telco Customer Churn Dataset**

### Source

IBM Sample Dataset (Kaggle)

### Dataset Summary

- Total Customers: **7,043**
- Original Features: **21**
- Features Used: **20**
- Target Variable: **Churn**

Target Classes

- Yes
- No

---

# Technologies Used

## Programming

- Python 3.12

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn
- Plotly

## Machine Learning

- Scikit-Learn
- XGBoost
- LightGBM
- CatBoost

## API Development

- FastAPI
- Uvicorn
- Pydantic

## Model Serialization

- Joblib

## Database

- PostgreSQL
- SQLAlchemy

## Deployment

- Docker

## Development Tools

- VS Code
- Jupyter Notebook
- Git
- GitHub

---

# Project Structure

```text
Customer_Churn_Prediction_System/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── API_Documentation.md
│   └── EDA_Report.md
│
├── models/
│   ├── best_model/
│   │   └── churn_prediction_model.pkl
│   │
│   ├── preprocessors/
│   │   ├── preprocessing_pipeline.pkl
│   │   └── target_encoder.pkl
│   │
│   └── segmentation/
│       ├── kmeans_model.pkl
│       └── scaler.pkl
│
├── notebook/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Customer_Segmentation.ipynb
│   ├── 06_Model_Training.ipynb
│   ├── 07_Model_Evaluation.ipynb
│   └── 08_Recommendation_Engine.ipynb
│
├── reports/
│
├── src/
│   ├── api/
│   ├── preprocessing/
│   ├── segmentation/
│   ├── recommendation/
│   ├── training/
│   ├── evaluation/
│   ├── visualization/
│   └── utils/
│
├── tests/
│
├── README.md
├── ROADMAP.md
├── requirements.txt
└── LICENSE
```

---

# Machine Learning Workflow

```text
Dataset
     │
     ▼
Data Understanding
     │
     ▼
Data Cleaning
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Feature Engineering
     │
     ▼
Customer Segmentation
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Recommendation Engine
     │
     ▼
REST API
     │
     ▼
Dashboard
     │
     ▼
Docker Deployment
```

---

# Machine Learning Models

The following algorithms were trained and evaluated.

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

---

# Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|--------|---------:|----------:|--------:|---------:|
| Gradient Boosting | **0.8062** | **0.6735** | 0.5241 | 0.5895 |
| Logistic Regression | 0.8055 | 0.6572 | **0.5588** | **0.6040** |
| LightGBM | 0.7977 | 0.6395 | 0.5455 | 0.5887 |
| CatBoost | 0.7970 | 0.6429 | 0.5294 | 0.5806 |
| XGBoost | 0.7842 | 0.6054 | 0.5374 | 0.5694 |
| Random Forest | 0.7779 | 0.6034 | 0.4759 | 0.5321 |
| Decision Tree | 0.7289 | 0.4896 | 0.5053 | 0.4974 |

---

# Best Model

## Logistic Regression

### Why was it selected?

- Highest F1 Score
- Highest Recall among top-performing models
- Excellent Generalization
- Fast Prediction
- Lightweight
- Production Friendly

> **Note:** Update this section if you decide to deploy a different trained model.

---

# Customer Segmentation

Customer segmentation was performed using **K-Means Clustering**.

### Cluster Selection

- Elbow Method
- Silhouette Score

### Final Number of Clusters

**4**

Customer Groups

- High Value Customers
- Premium Customers
- Budget Customers
- New Customers

---

# Recommendation Engine

The project includes a rule-based recommendation engine that generates personalized retention strategies based on:

- Customer Segment
- Contract Type
- Monthly Charges
- Churn Probability

Example Recommendations

- Offer Loyalty Discounts
- Upgrade Internet Plan
- Free Technical Support
- Premium Security Package
- Personalized Customer Support

---

# REST API

The project provides REST APIs using **FastAPI**.

### Available Endpoints

| Method | Endpoint | Description |
|----------|----------|------------|
| GET | `/` | API Status |
| GET | `/health` | Health Check |
| POST | `/predict` | Customer Churn Prediction |

---

### Swagger Documentation

```
http://127.0.0.1:8000/docs
```

### ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# Completed Features

- Project Setup
- Dataset Validation
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Customer Segmentation
- Multiple ML Models
- Model Comparison
- Best Model Selection
- Model Serialization
- Recommendation Engine
- FastAPI REST API
- Swagger Documentation
- ReDoc Documentation

---

# Upcoming Features

- Streamlit Dashboard
- Authentication
- Logging & Monitoring
- Docker Containerization
- Cloud Deployment
- Postman Collection
- Final Presentation Video

---

# Project Progress

| Phase | Status |
|-------------------------------|----------------|
| Project Setup | ✅ Completed |
| Dataset Management | ✅ Completed |
| Data Cleaning & Preprocessing | ✅ Completed |
| Exploratory Data Analysis | ✅ Completed |
| Feature Engineering | ✅ Completed |
| Customer Segmentation | ✅ Completed |
| Model Training | ✅ Completed |
| Model Evaluation | ✅ Completed |
| Recommendation Engine | ✅ Completed |
| REST API Development | ✅ Completed |
| Dashboard Development | ⏳ Pending |
| Authentication | ⏳ Pending |
| Logging & Monitoring | ⏳ Pending |
| Docker & Deployment | ⏳ Pending |
| Documentation | 🟡 In Progress |
| Cloud Deployment | ⏳ Pending |
| Final Presentation | ⏳ Pending |

---

# Installation

```bash
git clone https://github.com/muhammadismail040/Customer_Churn_Prediction_System.git

cd Customer_Churn_Prediction_System

python -m venv .venv

.\.venv\Scripts\activate

pip install -r requirements.txt
```

---

# Running the Project

## Run Jupyter Notebook

```bash
jupyter notebook
```

## Run FastAPI

```bash
uvicorn src.api.app:app --reload
```

---

# Future Improvements

- Explainable AI (SHAP)
- LIME Explanations
- Deep Learning Models
- Real-Time Prediction
- CI/CD Pipeline
- Automated Model Retraining
- Cloud Monitoring
- User Authentication
- Role-Based Access Control

---

# Overall Progress

```text
█████████████████████████░░░░░

85% Complete
```

---

# Deliverables

### Completed

- Complete Source Code
- GitHub Repository
- Data Cleaning Pipeline
- Feature Engineering Pipeline
- Trained Machine Learning Models
- Customer Segmentation Model
- Recommendation Engine
- REST API
- API Documentation
- README Documentation
- Roadmap

### Remaining

- Dashboard
- Docker Configuration
- Authentication
- Logging & Monitoring
- Postman Collection
- Cloud Deployment
- Final Presentation

---

# Author

## Muhammad Ismail

**Machine Learning Engineer Intern**

### GitHub

https://github.com/muhammadismail040

### LinkedIn

https://www.linkedin.com/in/muhammad-ismail-913ab6322/

---

# License

This project is licensed under the **MIT License**.