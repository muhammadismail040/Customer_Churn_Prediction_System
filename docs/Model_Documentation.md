# Model Documentation

Dataset

Data Cleaning

EDA

Feature Engineering

Customer Segmentation

Models Trained

Model Comparison

Best Model
# Model Documentation

# Customer Churn Prediction & Recommendation System

---

# Table of Contents

1. Project Overview
2. Dataset Information
3. Problem Statement
4. Data Preprocessing
5. Feature Engineering
6. Customer Segmentation
7. Machine Learning Models
8. Model Evaluation
9. Best Model Selection
10. Recommendation Engine
11. Project Pipeline
12. Future Improvements

---

# 1. Project Overview

The Customer Churn Prediction & Recommendation System predicts whether a customer is likely to leave the company (churn), estimates the probability of churn, segments customers into behavioral groups, and generates personalized retention recommendations.

The project combines supervised machine learning with customer segmentation techniques to support business decision-making.

---

# 2. Dataset Information

Dataset:

IBM Telco Customer Churn Dataset

Source:

Kaggle

Number of Records

7043

Number of Features

20

Target Variable

```
Churn
```

Target Classes

- Yes
- No

---

# 3. Features Used

### Customer Information

- gender
- SeniorCitizen
- Partner
- Dependents

### Account Information

- tenure
- Contract
- PaperlessBilling
- PaymentMethod

### Services

- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies

### Billing

- MonthlyCharges
- TotalCharges

---

# 4. Data Preprocessing

The preprocessing pipeline consists of:

## Missing Value Handling

- TotalCharges converted to numeric
- Invalid values replaced
- Missing values removed

## Duplicate Removal

Duplicate records were checked and removed.

## Feature Selection

CustomerID was removed because it does not contribute to prediction.

## Encoding

Categorical variables were transformed using One-Hot Encoding.

## Scaling

Numerical variables were standardized using StandardScaler.

---

# 5. Feature Engineering

The preprocessing pipeline uses:

- OneHotEncoder
- StandardScaler
- ColumnTransformer
- Pipeline

This ensures identical preprocessing during both training and inference.

---

# 6. Customer Segmentation

Customer segmentation is performed using K-Means Clustering.

Purpose

- Group similar customers
- Improve recommendation quality
- Business analytics

The optimal number of clusters was selected using:

- Elbow Method
- Silhouette Score

Each prediction also returns the customer's cluster.

---

# 7. Machine Learning Models Evaluated

The following algorithms were trained and evaluated.

| Model |
|---------|
| Logistic Regression |
| Decision Tree |
| Random Forest |
| Gradient Boosting |
| XGBoost |
| LightGBM |
| CatBoost |

Each model was evaluated on the same train-test split.

---

# 8. Evaluation Metrics

Models were compared using:

- Accuracy
- Precision
- Recall
- F1 Score

These metrics were used to identify the best-performing model.

---

# 9. Best Model

The final deployed model is the one that achieved the highest overall performance during evaluation.

The trained model is serialized and stored using Joblib.

```
models/
```

contains

- trained model
- preprocessing pipeline

---

# 10. Prediction Output

The API returns:

```
Prediction
```

Possible values

```
Yes
No
```

Probability

```
0.0 – 1.0
```

Cluster Number

```
0
1
2
...
```

Personalized Recommendations

Example

```
Customer is low risk.

Continue current services.
```

or

```
Offer loyalty discount.

Provide premium customer support.

Recommend annual contract.
```

---

# 11. Project Pipeline

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
EDA
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
Best Model
      │
      ▼
FastAPI
      │
      ▼
React Dashboard
```

---

# 12. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Joblib
- FastAPI
- PostgreSQL
- React
- Docker

---

# Future Improvements

Potential enhancements include:

- Deep Learning models
- AutoML
- Real-time streaming predictions
- Explainable AI (SHAP/LIME)
- Continuous model retraining
- Cloud-native deployment
- Model monitoring and drift detection

---

# Author

Muhammad Ismail

BS Computer Science

University of Engineering & Technology (UET) Mardan

Machine Learning Engineer Intern

---

# License

This project is released under the MIT License.
Saved Models

Prediction Pipeline

Recommendation Engine

Performance Metrics