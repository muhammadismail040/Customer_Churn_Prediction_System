"""
Customer Churn Prediction Dashboard
-----------------------------------
Main Dashboard Page
"""

import streamlit as st

from metrics import (
    load_data,
    total_customers,
    churn_rate,
    retention_rate,
    total_segments,
    model_accuracy,
    high_risk_customers,
)

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide",
)

# =====================================================
# Load Dataset
# =====================================================

df = load_data()

# =====================================================
# Dashboard Title
# =====================================================

st.title("📊 Customer Churn Prediction Dashboard")

st.write(
    """
Business Dashboard for monitoring customer churn,
customer segmentation, and retention strategies.
"""
)

st.divider()

# =====================================================
# Business KPIs
# =====================================================

st.subheader("Business Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "👥 Total Customers",
    total_customers(df),
)

col2.metric(
    "📉 Churn Rate",
    f"{churn_rate(df)} %",
)

col3.metric(
    "❤️ Retention Rate",
    f"{retention_rate(df)} %",
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "⚠️ High-Risk Customers",
    high_risk_customers(),
)

col5.metric(
    "🎯 Model Accuracy",
    f"{model_accuracy()} %",
)

col6.metric(
    "👥 Customer Segments",
    total_segments(),
)

st.divider()

st.success("✅ Dashboard Framework Loaded Successfully")

st.info(
    """
Next Module:

• Analytics Dashboard

• Interactive Charts

• Business Insights
"""
)