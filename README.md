# Customer Churn Prediction & Recommendation System

An end-to-end Machine Learning project that predicts customer churn, segments customers into meaningful groups, generates personalized retention recommendations, exposes predictions through a REST API, and provides an interactive React Dashboard for customer churn prediction, analytics, prediction history, and business insights.

The project follows an industry-standard Machine Learning pipeline from raw data preprocessing to model deployment and is being developed as part of a **Machine Learning Engineering Internship**.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Project Objectives](#project-objectives)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Machine Learning Workflow](#machine-learning-workflow)
- [Machine Learning Models](#machine-learning-models)
- [Model Performance](#model-performance)
- [Best Model](#best-model)
- [Customer Segmentation](#customer-segmentation)
- [Recommendation Engine](#recommendation-engine)
- [REST API](#rest-api)
- [API Authentication](#api-authentication)
- [Logging & Monitoring](#logging--monitoring)
- [React Dashboard](#react-dashboard)
- [Completed Features](#completed-features)
- [Upcoming Features](#upcoming-features)
- [Project Progress](#project-progress)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Docker](#docker)
- [Postman Collection](#postman-collection)
- [Future Improvements](#future-improvements)
- [Overall Progress](#overall-progress)
- [Deliverables](#deliverables)
- [Documentation](#documentation)
- [Author](#author)
- [Acknowledgements](#acknowledgements)
- [License](#license)

---

## Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses such as telecom companies. Losing existing customers directly impacts revenue and business growth.

This project provides a complete Machine Learning solution capable of:

- Predicting customer churn
- Segmenting customers using K-Means Clustering
- Generating personalized retention recommendations
- Serving predictions through a FastAPI REST API
- Visualizing business insights using an interactive React Dashboard

The project demonstrates the complete lifecycle of a production-ready Machine Learning application.

---

## Project Objectives

- Predict customer churn using Machine Learning
- Segment customers based on behavioral patterns
- Generate personalized customer retention recommendations
- Compare multiple Machine Learning models
- Select the best-performing model
- Build a production-ready REST API using FastAPI
- Secure APIs using API Key Authentication
- Provide interactive API documentation (Swagger & ReDoc)
- Build an interactive React Dashboard
- Implement Logging & Monitoring
- Deploy the project using Docker and Cloud services

---

## Dataset

### Dataset Name
**Telco Customer Churn Dataset**

### Source
IBM Sample Dataset (Kaggle)

### Dataset Summary

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

## Technologies Used

### Frontend
- React.js
- Bootstrap 5
- Axios
- Recharts

### Backend
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

### Database
- PostgreSQL

### Containerization
- Docker
- Docker Compose

### Programming
- Python 3.12

### Data Analysis
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn
- Plotly

### Machine Learning
- Scikit-Learn
- XGBoost
- LightGBM
- CatBoost

### API Development
- FastAPI
- Uvicorn
- Pydantic

### Security
- FastAPI Security
- Python-dotenv

### Logging
- Python Logging

### Model Serialization
- Joblib

### Development Tools
- VS Code
- Jupyter Notebook
- Git
- GitHub

---

## Project Structure

```text
CUSTOMER_CHURN_PREDICTION_SYSTEM/
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── DashboardCards.jsx
│   │   │   ├── PredictionForm.jsx
│   │   │   ├── PredictionHistory.jsx
│   │   │   ├── PredictionResult.jsx
│   │   │   ├── Charts/
│   │   │   │   ├── PieChart.jsx
│   │   │   │   └── ClusterChart.jsx
│   │   │   └── common/
│   │   │       ├── Header.jsx
│   │   │       ├── Footer.jsx
│   │   │       └── Pagination.jsx
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   ├── predictionService.js
│   │   │   └── historyService.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   └── .env
│
├── backend/
│   ├── src/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── model_loader.py
│   │   │   ├── predictor.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   ├── config/
│   │   │   └── __init__.py
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── connection.py
│   │   │   └── models.py
│   │   ├── preprocessing/
│   │   │   ├── __init__.py
│   │   │   ├── data_loader.py
│   │   │   └── validator.py
│   │   ├── recommendation/
│   │   │   ├── __init__.py
│   │   │   ├── recommendation_engine.py
│   │   │   └── rules.py
│   │   ├── segmentation/
│   │   │   ├── __init__.py
│   │   │   ├── cluster_analysis.py
│   │   │   ├── kmeans_model.py
│   │   │   └── visualization.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── logger.py
│   │   └── __init__.py
│   ├── models/
│   │   ├── best_model/
│   │   │   └── churn_prediction_model.pkl
│   │   ├── preprocessors/
│   │   │   ├── preprocessing_pipeline.pkl
│   │   │   └── target_encoder.pkl
│   │   └── segmentation/
│   │       ├── kmeans_model.pkl
│   │       └── scaler.pkl
│   ├── data/
│   │   ├── final/
│   │   │   └── Customer_Churn_With_Recommendations.csv
│   │   ├── processed/
│   │   │   └── Telco_Customer_Churn_Cleaned.csv
│   │   └── raw/
│   │       └── Telco_Customer_Churn.csv
│   ├── logs/
│   │   ├── api.log
│   │   ├── error.log
│   │   └── prediction.log
│   ├── notebook/
│   │   ├── 01_data_understanding.ipynb
│   │   ├── 02_Data_Cleaning.ipynb
│   │   ├── 03_Exploratory_Data_Analysis.ipynb
│   │   ├── 04_Feature_Engineering.ipynb
│   │   ├── 05_Customer_Segmentation.ipynb
│   │   ├── 06_Model_Training.ipynb
│   │   ├── 07_Model_Evaluation.ipynb
│   │   ├── 08_Recommendation_Engine.ipynb
│   │   └── catboost_info/
│   ├── reports/
│   │   ├── Customer_Segmentation_Report.md
│   │   ├── Recommendation_Engine_Report.md
│   │   ├── Dataset_Summary.md
│   │   ├── EDA_Report.md
│   │   └── prediction_history.csv
│   ├── docs/
│   │   ├── API_Documentation.md
│   │   ├── Authentication_Documentation.md
│   │   ├── CHANGELOG.md
│   │   ├── Dashboard_Documentation.md
│   │   ├── Data_Dictionary.md
│   │   ├── Installation_Guide.md
│   │   ├── Logging_Monitoring.md
│   │   ├── Model_Documentation.md
│   │   ├── project_status.md
│   │   └── User_Guide.md
│   ├── .env
│   ├── .gitignore
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── Customer_Churn_API.postman_collection.json
├── LICENSE
├── README.md
└── ROADMAP.md
```

---

## Machine Learning Workflow

```
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
API Authentication
     │
     ▼
Logging & Monitoring
     │
     ▼
React Dashboard
     │
     ▼
Docker Deployment
     │
     ▼
Cloud Deployment
```

---

## Machine Learning Models

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

## Model Performance

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

## Best Model

### Logistic Regression

#### Why was Logistic Regression Selected?

Although Gradient Boosting achieved the highest accuracy, **Logistic Regression** was selected as the final production model because it provided the best overall balance between performance and efficiency.

#### Selection Reasons

- Highest F1 Score
- Highest Recall among the top-performing models
- Excellent Generalization
- Fast Prediction Speed
- Lightweight Model
- Easy Deployment
- Production Friendly

The trained model has been serialized using **Joblib** and is loaded directly by the FastAPI application for real-time predictions.

---

## Customer Segmentation

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

## Recommendation Engine

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

## REST API

The application exposes prediction services through a **FastAPI** REST API.

### Available Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Status |
| GET | `/health` | Health Check |
| POST | `/predict` | Customer Churn Prediction |
| GET | `/history` | Get Prediction History |
| GET | `/history/count` | Get History Count |
| GET | `/history/latest` | Get Latest Prediction |
| DELETE | `/history/{id}` | Delete Prediction |

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
- Prediction History
- JSON Responses
- Interactive API Documentation

---

## API Authentication

The REST API is protected using **API Key Authentication**.

### Protected Endpoints

| Method | Endpoint |
| ------- | -------- |
| POST | `/predict` |
| GET | `/history` |
| DELETE | `/history/{id}` |

### Required Header
```text
x-api-key
```

### Development API Key
```text
customer_churn_ml_api_2026
```

The API key is stored securely inside the `.env` file and verified before processing prediction requests.

Unauthorized requests return:
```http
401 Unauthorized
```

Swagger UI also supports API key authentication through the **Authorize** button.

---

## Logging & Monitoring

The project includes a production-ready logging system to monitor API usage and simplify debugging.

### Log Files
```text
logs/
├── api.log
├── prediction.log
└── error.log
```

### API Logger
Records:
- HTTP Method
- Endpoint
- Status Code
- Client IP
- Processing Time

### Prediction Logger
Records:
- Prediction Result
- Churn Probability
- Customer Segment
- Generated Recommendations

### Error Logger
Records:
- Runtime Errors
- Exception Messages
- Stack Traces

This logging system helps monitor API activity and troubleshoot issues efficiently.

---

## React Dashboard

The project includes an interactive **React Dashboard** designed for business users and decision-makers.

### Dashboard Features

- **Customer Prediction Form** - Input customer data for real-time predictions
- **Prediction Result** - Display prediction, probability, and recommendations
- **Dashboard Cards** - Key business KPIs (Total Customers, Churn Rate, etc.)
- **Prediction History** - View all previous predictions with pagination
- **Export CSV** - Download prediction history as CSV file
- **Delete Prediction** - Remove individual predictions
- **View Prediction** - View detailed prediction results
- **Pie Chart** - Churn distribution visualization
- **Cluster Chart** - Customer segmentation visualization
- **Pagination** - Navigate through prediction history
- **Responsive UI** - Works on desktop and mobile devices

### Dashboard Pages

#### Home Dashboard
Displays key business KPIs including:
- Total Customers
- Churn Rate
- Retention Rate
- High-Risk Customers
- Customer Segments
- Model Accuracy
- Recent Predictions

#### Analytics Dashboard
Provides interactive visualizations such as:
- Churn Distribution (Pie Chart)
- Customer Segmentation (Cluster Chart)
- Contract Type Analysis
- Monthly Charges Distribution
- Customer Tenure Analysis

#### Prediction Dashboard
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

## Completed Features

- Project Setup
- Dataset Validation
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Customer Segmentation
- Multiple ML Models
- Model Comparison
- Best Model Selection
- Recommendation Engine
- FastAPI REST API
- Interactive React Dashboard
- Prediction History
- CSV Export
- Dashboard Analytics
- Pagination
- Delete Prediction
- Prediction Statistics
- Charts & Visualization
- PostgreSQL Integration
- API Key Authentication
- API Request Logging
- Prediction Logging
- Error Logging
- Swagger Documentation
- ReDoc Documentation

---

## Upcoming Features

- Docker Containerization
- Docker Compose
- Cloud Deployment
- Final Documentation
- Final Presentation

---

## Project Progress

| Phase | Status |
| ----------------------------- | -------------- |
| Project Setup | ✅ Completed |
| Dataset Management | ✅ Completed |
| Data Cleaning & Preprocessing | ✅ Completed |
| Exploratory Data Analysis | ✅ Completed |
| Feature Engineering | ✅ Completed |
| Customer Segmentation | ✅ Completed |
| Model Training | ✅ Completed |
| Model Evaluation | ✅ Completed |
| Recommendation Engine | ✅ Completed |
| FastAPI API | ✅ Completed |
| PostgreSQL Integration | ✅ Completed |
| React Frontend | ✅ Completed |
| Prediction History | ✅ Completed |
| Dashboard Analytics | ✅ Completed |
| CSV Export | ✅ Completed |
| Authentication | ✅ Completed |
| Logging & Monitoring | ✅ Completed |
| Docker Containerization | 🟡 In Progress |
| Docker Compose | 🟡 In Progress |
| Cloud Deployment | ⏳ Pending |
| Final Documentation | 🟡 In Progress |

---

## Installation

### Clone Repository
```bash
git clone https://github.com/muhammadismail040/Customer_Churn_Prediction_System.git
```

### Move to Project Folder
```bash
cd Customer_Churn_Prediction_System
```

### Backend Setup

#### Create Virtual Environment
```bash
python -m venv .venv
```

#### Activate Virtual Environment

**Windows**
```bash
.\.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend
npm install
```

---

## Running the Project

### Backend
```bash
uvicorn src.api.routes:app --reload
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

### Frontend
```bash
cd frontend
npm run dev
```

Dashboard URL
```text
http://localhost:5173
```

### Run Jupyter Notebook
```bash
jupyter notebook
```

---

## Docker

### Build Image
```bash
docker build -t churn-backend .
```

### Run Container
```bash
docker run -d -p 8000:8000 churn-backend
```

### Docker Compose
```bash
docker compose up --build
```

This will start both the backend and PostgreSQL database containers.

---

## Postman Collection

### Import
```text
Customer_Churn_API.postman_collection.json
```

### Available APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/predict` | Make a prediction |
| GET | `/history` | Get all predictions |
| GET | `/history/count` | Get prediction count |
| GET | `/history/latest` | Get latest prediction |
| DELETE | `/history/{id}` | Delete a prediction |

All endpoints (except `/` and `/health`) require API Key Authentication.

---

## Future Improvements

The project can be further enhanced by implementing:

- Docker Containerization
- Cloud Deployment (AWS, Azure, Render)
- Explainable AI using SHAP
- LIME Model Explanations
- User Authentication
- CI/CD Pipeline
- Automatic Model Retraining
- Real-Time Prediction Pipeline
- Database Integration
- Email-Based Customer Retention Campaigns
- Advanced Business Analytics

---

## Overall Progress

```text
███████████████████████████████████░

97% Complete
```

The project has successfully completed the complete Machine Learning pipeline, including customer segmentation, model training, model evaluation, recommendation engine, REST API development, API authentication, logging and monitoring, PostgreSQL integration, and an interactive React dashboard.

The remaining work focuses on Docker containerization and cloud deployment.

---

## Deliverables

### Completed Deliverables

- Complete Source Code
- GitHub Repository
- Data Cleaning Pipeline
- Feature Engineering Pipeline
- Trained Machine Learning Models
- Customer Segmentation Model
- Recommendation Engine
- FastAPI REST API
- Interactive React Dashboard
- Prediction History
- Dashboard Analytics
- CSV Export
- PostgreSQL Integration
- API Key Authentication
- Logging & Monitoring
- Swagger Documentation
- ReDoc Documentation
- README Documentation
- ROADMAP
- Postman Collection

### Remaining Deliverables

- Docker Image
- Docker Compose
- Cloud Deployment
- Final Deployment Links

---

## Documentation

The project includes the following documentation.

| Document | Description |
|----------|-------------|
| README.md | Complete project overview |
| ROADMAP.md | Development roadmap and project timeline |
| API_Documentation.md | REST API documentation |
| Authentication_Documentation.md | API authentication guide |
| Dashboard_Documentation.md | Dashboard features and usage |
| Model_Documentation.md | Machine Learning pipeline |
| Data_Dictionary.md | Dataset feature descriptions |
| Installation_Guide.md | Installation instructions |
| User_Guide.md | Dashboard and API usage |
| Logging_Monitoring.md | Logging and monitoring guide |
| CHANGELOG.md | Project version history |
| project_status.md | Current development status |

---

## Author

### Muhammad Ismail

**Machine Learning Engineer Intern**

University of Engineering & Technology (UET) Mardan

### GitHub
https://github.com/muhammadismail040

### LinkedIn
https://www.linkedin.com/in/muhammad-ismail-913ab6322/

---

## Acknowledgements

This project was developed as part of a Machine Learning Engineering Internship to demonstrate the complete lifecycle of a production-ready Machine Learning application.

Special thanks to:

- IBM for the Telco Customer Churn Dataset
- Scikit-learn Community
- FastAPI Community
- React Community
- XGBoost, LightGBM, and CatBoost Developers
- Open Source Contributors

---

## License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project under the terms of the MIT License.

---

## ⭐ Support the Project

If you found this project useful, consider giving it a ⭐ on GitHub.

Feedback and contributions are always welcome!