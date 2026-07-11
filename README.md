# Customer Churn Prediction & Recommendation System

An end-to-end Machine Learning project that predicts customer churn, segments customers into meaningful groups, generates personalized retention recommendations, exposes predictions through a REST API, and provides an interactive Business Dashboard built with Streamlit.

The project follows an industry-standard Machine Learning pipeline from raw data preprocessing to model deployment and is being developed as part of a **Machine Learning Engineering Internship**.

---

# Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses such as telecom companies. Losing existing customers directly impacts revenue and business growth.

This project provides a complete Machine Learning solution capable of:

- Predicting customer churn
- Segmenting customers using K-Means Clustering
- Generating personalized retention recommendations
- Serving predictions through a FastAPI REST API
- Visualizing business insights using an interactive Streamlit Dashboard

The project demonstrates the complete lifecycle of a production-ready Machine Learning application.

---

# Project Objectives

- Predict customer churn using Machine Learning
- Perform Data Cleaning and Exploratory Data Analysis
- Engineer meaningful customer features
- Segment customers using K-Means Clustering
- Compare multiple Machine Learning algorithms
- Select the best-performing model
- Generate personalized retention recommendations
- Develop a production-ready REST API using FastAPI
- Build an interactive Business Dashboard using Streamlit
- Prepare the project for Docker deployment

---

# Dataset

## Dataset Name

**Telco Customer Churn Dataset**

## Source

IBM Sample Dataset (Kaggle)

## Dataset Summary

| Item | Value |
|------|-------|
| Total Customers | 7,043 |
| Original Features | 21 |
| Features Used | 20 |
| Target Variable | Churn |

### Target Classes

- Yes
- No

---

# Technology Stack

## Programming

- Python 3.12

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn
- Plotly

## Machine Learning

- Scikit-Learn
- XGBoost
- LightGBM
- CatBoost

## Dashboard

- Streamlit

## API Development

- FastAPI
- Uvicorn
- Pydantic

## Model Serialization

- Joblib

## Database

- PostgreSQL
- SQLAlchemy

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
│   ├── app.py
│   ├── metrics.py
│   ├── charts.py
│   ├── prediction.py
│   ├── gauge.py
│   ├── history.py
│   ├── sidebar.py
│   ├── utils.py
│   ├── assets/
│   └── pages/
│       ├── 2_Analytics.py
│       └── 3_Prediction.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
│
├── docs/
│
├── models/
│   ├── best_model/
│   ├── preprocessors/
│   └── segmentation/
│
├── notebook/
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
Business Dashboard
    │
    ▼
Docker Deployment (Upcoming)
```

---

# Machine Learning Models

The following Machine Learning algorithms were trained and evaluated to predict customer churn.

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

Each model was trained using the same preprocessed dataset and evaluated using standard classification metrics.

---

# Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|---------:|----------:|-------:|---------:|
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

### Why was Logistic Regression Selected?

Although Gradient Boosting achieved the highest accuracy, **Logistic Regression** was selected as the final production model because it provided the best overall balance between performance and efficiency.

### Selection Reasons

- Highest F1 Score
- Highest Recall among the top-performing models
- Excellent Generalization
- Fast Prediction Speed
- Lightweight Model
- Easy Deployment
- Production Friendly

The trained model has been serialized using **Joblib** and is loaded directly by the FastAPI application for real-time predictions.

---

# Customer Segmentation

Customer segmentation was performed using **K-Means Clustering** to group customers with similar behavioral patterns.

### Cluster Selection Methods

- Elbow Method
- Silhouette Score

### Final Number of Clusters

**4 Clusters**

### Customer Segments

| Cluster | Description |
|----------|-------------|
| Cluster 0 | Loyal Customers |
| Cluster 1 | High-Value Customers |
| Cluster 2 | Budget Customers |
| Cluster 3 | New Customers |

### Cluster Features

The segmentation considered important customer attributes such as:

- Tenure
- Monthly Charges
- Total Charges

The trained clustering model and scaler were saved for future predictions.

---

# Recommendation Engine

The project includes a rule-based recommendation engine that generates personalized retention strategies based on customer characteristics.

### Recommendation Factors

- Customer Segment
- Contract Type
- Internet Service
- Online Security
- Technical Support
- Paperless Billing
- Payment Method
- Monthly Charges
- Customer Tenure

### Example Recommendations

- Offer a long-term contract discount
- Recommend the Online Security package
- Provide premium technical support
- Offer free technical support for one month
- Encourage automatic payment methods
- Provide loyalty rewards
- Offer discounts on monthly charges
- Send a welcome retention package

Each prediction generates recommendations dynamically based on the customer's profile.

---

# REST API

The application exposes prediction services through a **FastAPI** REST API.

## Available Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Status |
| GET | `/health` | Health Check |
| POST | `/predict` | Customer Churn Prediction |

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

### ReDoc Documentation

```text
http://127.0.0.1:8000/redoc
```

### API Features

- Real-Time Prediction
- Churn Probability
- Customer Segmentation
- Personalized Recommendations
- JSON Responses
- Interactive API Documentation

---

# Business Dashboard

The project includes an interactive **Streamlit Business Dashboard** designed for business users and decision-makers.

## Dashboard Modules

### Home Dashboard

Displays key business KPIs including:

- Total Customers
- Churn Rate
- Retention Rate
- High-Risk Customers
- Customer Segments
- Model Accuracy

---

### Analytics Dashboard

Provides interactive visualizations such as:

- Churn Distribution
- Contract Type Analysis
- Monthly Charges Distribution
- Customer Tenure Analysis
- Customer Segmentation Analysis
- Correlation Heatmap

---

### Prediction Dashboard

Allows users to perform real-time churn prediction by entering customer information.

The dashboard displays:

- Churn Prediction
- Churn Probability
- Probability Gauge
- Customer Segment
- Risk Assessment
- Personalized Recommendations
- Business Insights
- Customer Information
- Prediction History

The dashboard communicates with the trained Machine Learning model and recommendation engine to provide instant business insights.

---

# Completed Features

The following features have been successfully implemented in the project.

## Data Processing

- Project Setup
- Dataset Collection
- Dataset Validation
- Data Cleaning
- Missing Value Handling
- Duplicate Value Checking
- Data Type Correction
- Feature Cleaning
- Data Preprocessing Pipeline

---

## Exploratory Data Analysis

- Target Variable Analysis
- Numerical Feature Analysis
- Categorical Feature Analysis
- Correlation Analysis
- Distribution Plots
- Count Plots
- Box Plots
- Churn Insights Report

---

## Feature Engineering

- Feature Selection
- Train-Test Split
- Target Encoding
- One-Hot Encoding
- Feature Scaling
- ColumnTransformer Pipeline
- Saved Preprocessing Pipeline

---

## Customer Segmentation

- K-Means Clustering
- Elbow Method
- Silhouette Score
- Customer Cluster Assignment
- Cluster Profiling
- Saved K-Means Model

---

## Model Training

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

---

## Model Evaluation

- Accuracy Comparison
- Precision Comparison
- Recall Comparison
- F1 Score Comparison
- Confusion Matrix
- Classification Report
- ROC Curve
- Best Model Selection
- Saved Production Model

---

## Recommendation Engine

- Rule-Based Recommendation System
- Personalized Retention Strategies
- Customer-Specific Recommendations
- API Integration

---

## REST API

- FastAPI Application
- Prediction Endpoint
- Health Check Endpoint
- Swagger Documentation
- ReDoc Documentation
- Request Validation
- Response Validation

---

## Business Dashboard

- Interactive Streamlit Dashboard
- Business KPI Cards
- Analytics Dashboard
- Prediction Dashboard
- Churn Probability Gauge
- Business Insights
- Customer Information
- Recommendation Display
- Prediction History

---

# Upcoming Features

The following features are planned for future releases.

- Docker Containerization
- Cloud Deployment
- User Authentication
- Logging & Monitoring
- Postman Collection
- CI/CD Pipeline
- Explainable AI (SHAP)
- LIME Explanations
- Automated Model Retraining
- Role-Based Access Control

---

# Project Progress

| Phase | Status |
|---------------------------------|----------------|
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
| Business Dashboard | ✅ Completed |
| Documentation | 🟡 In Progress |
| Docker & Deployment | ⏳ Pending |
| Final Presentation | ⏳ Pending |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/muhammadismail040/Customer_Churn_Prediction_System.git
```

## Move to Project Folder

```bash
cd Customer_Churn_Prediction_System
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

### Windows

```bash
.\.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Run Jupyter Notebook

```bash
jupyter notebook
```

---

## Run FastAPI

```bash
uvicorn src.api.app:app --reload
```

API URL

```text
http://127.0.0.1:8000
```

Swagger UI

```text
http://127.0.0.1:8000/docs
```

ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL

```text
http://localhost:8501
```

---

# Future Improvements

The project can be further enhanced by implementing:

- Docker Containerization
- Cloud Deployment (AWS, Azure, Render)
- Explainable AI using SHAP
- LIME Model Explanations
- User Authentication
- Logging & Monitoring
- CI/CD Pipeline
- Automatic Model Retraining
- Real-Time Prediction Pipeline
- Database Integration
- Email-Based Customer Retention Campaigns
- Advanced Business Analytics

---

# Overall Progress

```text
████████████████████████████░░

92% Complete
```

The project has successfully completed the complete Machine Learning pipeline, including customer segmentation, model training, model evaluation, recommendation engine, REST API development, and an interactive business dashboard.

The remaining work focuses on deployment and final documentation.

---

# Deliverables

## Completed Deliverables

- Complete Source Code
- GitHub Repository
- Data Cleaning Pipeline
- Feature Engineering Pipeline
- Customer Segmentation Model
- Trained Machine Learning Model
- Recommendation Engine
- FastAPI REST API
- Swagger API Documentation
- ReDoc Documentation
- Interactive Streamlit Business Dashboard
- Dashboard Analytics
- Real-Time Customer Prediction
- Prediction History
- README Documentation
- ROADMAP Documentation

---

## Remaining Deliverables

- Docker Configuration
- Cloud Deployment
- Logging & Monitoring
- Authentication
- Postman Collection
- Final Project Presentation

---

# Documentation

The project includes the following documentation.

| Document | Description |
|----------|-------------|
| README.md | Complete project overview |
| ROADMAP.md | Development roadmap and project timeline |
| API_Documentation.md | REST API documentation |
| Dashboard_Documentation.md | Dashboard features and usage |
| Model_Documentation.md | Machine Learning pipeline |
| Data_Dictionary.md | Dataset feature descriptions |
| Installation_Guide.md | Installation instructions |
| User_Guide.md | Dashboard and API usage |
| CHANGELOG.md | Project version history |
| project_status.md | Current development status |

---

# Repository

```text
Customer_Churn_Prediction_System
│
├── dashboard/
├── src/
├── notebook/
├── models/
├── docs/
├── reports/
├── data/
├── tests/
│
├── README.md
├── ROADMAP.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# Author

## Muhammad Ismail

**Machine Learning Engineer Intern**

University of Engineering & Technology (UET) Mardan

---

### GitHub

https://github.com/muhammadismail040

---

### LinkedIn

https://www.linkedin.com/in/muhammad-ismail-913ab6322/

---

# Acknowledgements

This project was developed as part of a Machine Learning Engineering Internship to demonstrate the complete lifecycle of a production-ready Machine Learning application.

Special thanks to:

- IBM for the Telco Customer Churn Dataset
- Scikit-learn Community
- FastAPI Community
- Streamlit Community
- XGBoost, LightGBM, and CatBoost Developers
- Open Source Contributors

---

# License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project under the terms of the MIT License.

---

## ⭐ Support the Project

If you found this project useful, consider giving it a ⭐ on GitHub.

Feedback and contributions are always welcome!