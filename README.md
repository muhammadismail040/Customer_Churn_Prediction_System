# Customer Churn Prediction & Recommendation System

An end-to-end Machine Learning project that predicts customer churn, segments customers into meaningful groups, and generates personalized retention recommendations. The project follows a production-ready workflow from data preprocessing to deployment using FastAPI and Docker.

---

# Project Overview

Customer churn is a major challenge for subscription-based businesses such as telecom companies. Predicting which customers are likely to leave enables organizations to take proactive actions that improve customer retention.

This project aims to:

- Predict customer churn using Machine Learning
- Segment customers based on their behavior
- Generate personalized retention recommendations
- Expose predictions through a REST API
- Build an interactive dashboard
- Deploy the solution using Docker

---

# Objectives

- Build an end-to-end Machine Learning pipeline
- Perform Data Cleaning and Exploratory Data Analysis
- Engineer meaningful features
- Segment customers using K-Means Clustering
- Train and compare multiple Machine Learning models
- Select the best-performing model
- Develop a Recommendation Engine
- Build REST APIs using FastAPI
- Create an interactive Dashboard
- Containerize the project using Docker
- Deploy the complete application

---

# Dataset

**Dataset Name**

Telco Customer Churn Dataset

**Source**

IBM Sample Dataset (Kaggle)

**Dataset Size**

- 7,043 Customers
- 21 Original Features
- Binary Target Variable (Churn)

**Target Variable**

```
Churn
```

- Yes
- No

---

# Technologies Used

## Programming Language

- Python 3.12

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn
- Plotly

## Machine Learning

- Scikit-learn
- XGBoost
- LightGBM
- CatBoost

## API Development

- FastAPI
- Uvicorn

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

```
Customer_Churn_Prediction_System/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
│
├── notebook/
│
├── src/
│   ├── preprocessing/
│   ├── segmentation/
│   ├── models/
│   ├── recommendation/
│   ├── api/
│   └── utils/
│
├── dashboard/
│
├── models/
│   ├── preprocessing/
│   ├── clustering/
│   └── trained_models/
│
├── reports/
├── docs/
├── tests/
│
├── requirements.txt
├── Dockerfile
├── README.md
└── LICENSE
```

---

# Machine Learning Workflow

```
Dataset
    │
    ▼
Dataset Understanding
    │
    ▼
Data Cleaning & Preprocessing
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

The following algorithms were trained and evaluated:

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
|--------|---------:|----------:|--------:|----------:|
| Gradient Boosting | 0.8062 | 0.6735 | 0.5241 | 0.5895 |
| Logistic Regression | 0.8055 | 0.6572 | 0.5588 | **0.6040** |
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
- Easy to Deploy in Production

---

# Features

## Completed

- Dataset Validation
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Customer Segmentation (K-Means)
- Multiple Machine Learning Models
- Model Comparison
- Best Model Selection
- Model Serialization
- Rule-Based Recommendation Engine
- Personalized Customer Retention Recommendations
- API-Ready Project Structure

## Upcoming

- FastAPI REST API
- Authentication & Authorization
- Logging & Monitoring
- Interactive Dashboard
- Docker Containerization
- Cloud Deployment
- API Documentation
- Final Presentation

---

# Project Progress

## Phase 1 — Project Setup

- Project Structure
- Virtual Environment
- Required Libraries
- GitHub Repository
- Dataset Collection

---

## Phase 2 — Dataset Management

- Data Loading
- Dataset Validation
- Dataset Summary
- Dataset Understanding
- Data Dictionary

---

## Phase 3 — Data Cleaning & Preprocessing

- Missing Value Handling
- Duplicate Checking
- Data Type Correction
- Feature Cleaning
- Removed CustomerID
- Converted TotalCharges to Numeric
- Saved Clean Dataset

---

## Phase 4 — Exploratory Data Analysis

- Numerical Analysis
- Categorical Analysis
- Correlation Analysis
- Distribution Plots
- Count Plots
- Box Plots
- Churn Insights

---

## Phase 5 — Feature Engineering

- Feature Selection
- Train-Test Split
- Label Encoding
- One-Hot Encoding
- Feature Scaling
- ColumnTransformer Pipeline
- Saved Preprocessing Pipeline

---

## Phase 6 — Customer Segmentation

- K-Means Clustering
- Elbow Method
- Silhouette Score
- Customer Cluster Assignment
- Cluster Profiling
- Saved K-Means Model

---

## Phase 7 — Model Training

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

---

## Phase 8 — Model Evaluation

- Model Comparison
- Confusion Matrix
- Classification Report
- ROC Curve
- ROC-AUC Score
- Best Model Selection
- Saved Final Model

---

## Phase 9 — Recommendation Engine

- Rule-Based Recommendation System
- Personalized Customer Retention Strategies
- Recommendation Report
- Recommendation Dataset
- API-Ready Recommendation Module

---

## Upcoming Phases

- Phase 10 — REST API Development
- Phase 11 — Dashboard Development
- Phase 12 — Authentication
- Phase 13 — Logging & Monitoring
- Phase 14 — Docker & Deployment
- Phase 15 — Documentation
- Phase 16 — Cloud Deployment
- Phase 17 — Final Presentation

---

# Current Status

| Phase | Status |
|------------------------------|--------------|
| Project Setup | ✅ Completed |
| Dataset Management | ✅ Completed |
| Data Cleaning & Preprocessing | ✅ Completed |
| Exploratory Data Analysis | ✅ Completed |
| Feature Engineering | ✅ Completed |
| Customer Segmentation | ✅ Completed |
| Model Training | ✅ Completed |
| Model Evaluation | ✅ Completed |
| Recommendation Engine | ✅ Completed |
| REST API Development | ⏳ Pending |
| Dashboard Development | ⏳ Pending |
| Authentication | ⏳ Pending |
| Logging & Monitoring | ⏳ Pending |
| Docker & Deployment | ⏳ Pending |
| Documentation | ⏳ Pending |
| Cloud Deployment | ⏳ Pending |
| Final Presentation | ⏳ Pending |

---

# Installation

```bash
git clone https://github.com/muhammadismail040/Customer_Churn_Prediction_System.git

cd Customer_Churn_Prediction_System

python -m venv .venv

source .venv/Scripts/activate

pip install -r requirements.txt
```

---

# Running the Project

### Launch Jupyter Notebook

```bash
jupyter notebook
```

### Run FastAPI (Coming Soon)

```bash
uvicorn app:app --reload
```

---

# Future Improvements

- Explainable AI (SHAP/LIME)
- Deep Learning Models
- Real-Time Prediction
- CI/CD Pipeline
- Automated Model Retraining
- Cloud-Based Monitoring
- Stream Processing

---

# Overall Progress

```
███████████████████░░░░░░░░

72% Complete
```

---

# Deliverables

The completed project will include:

- Complete Source Code
- GitHub Repository
- Trained Machine Learning Models
- Recommendation Engine
- REST API
- Dashboard
- Docker Configuration
- API Documentation
- Postman Collection
- Deployment Link
- README Documentation
- Final Presentation

---

# Author

**Muhammad Ismail**

Machine Learning Engineer Intern

**GitHub**

https://github.com/muhammadismail040

**LinkedIn**

https://www.linkedin.com/in/muhammad-ismail-913ab6322/

---

# License

This project is licensed under the MIT License.