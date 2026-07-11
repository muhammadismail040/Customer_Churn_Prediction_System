import streamlit as st

import sys
from pathlib import Path

# -------------------------------------------------
# Add Project Root to Python Path
# -------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
import pandas as pd

from dashboard.prediction import predict_customer
from dashboard.gauge import probability_gauge
from dashboard.history import save_prediction

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Customer Prediction",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Customer Churn Prediction")

st.markdown(
"""
Enter the customer's information below to predict:

- Customer Churn
- Churn Probability
- Customer Segment
- Retention Recommendations
"""
)

st.divider()

# ============================================================
# Input Form
# ============================================================

with st.form("prediction_form"):

    left, right = st.columns(2)

    # ========================================================
    # LEFT
    # ========================================================

    with left:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        senior = st.selectbox(
            "Senior Citizen",
            [0, 1]
        )

        partner = st.selectbox(
            "Partner",
            ["Yes", "No"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["Yes", "No"]
        )

        tenure = st.number_input(
            "Tenure",
            min_value=0,
            max_value=100,
            value=12
        )

        phone = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        multiple = st.selectbox(
            "Multiple Lines",
            [
                "Yes",
                "No",
                "No phone service"
            ]
        )

        internet = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

        security = st.selectbox(
            "Online Security",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        backup = st.selectbox(
            "Online Backup",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

    # ========================================================
    # RIGHT
    # ========================================================

    with right:

        protection = st.selectbox(
            "Device Protection",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        support = st.selectbox(
            "Tech Support",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        tv = st.selectbox(
            "Streaming TV",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        movies = st.selectbox(
            "Streaming Movies",
            [
                "Yes",
                "No",
                "No internet service"
            ]
        )

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

        paperless = st.selectbox(
            "Paperless Billing",
            [
                "Yes",
                "No"
            ]
        )

        payment = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

        monthly = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            value=70.0
        )

        total = st.number_input(
            "Total Charges",
            min_value=0.0,
            value=850.0
        )

    submit = st.form_submit_button(
        "🚀 Predict Customer"
    )

# ============================================================
# Prediction
# ============================================================

if submit:

    customer = {

        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": security,
        "OnlineBackup": backup,
        "DeviceProtection": protection,
        "TechSupport": support,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total

    }

    with st.spinner("Predicting..."):

        result = predict_customer(customer)

    save_prediction(result)

    st.divider()

    st.header("Prediction Result")

    c1, c2, c3 = st.columns(3)

    with c1:

        if result["Prediction"] == "Yes":

            st.error("⚠ Customer is likely to Churn")

        else:

            st.success("✅ Customer is likely to Stay")

    with c2:

        st.metric(
            "Probability",
            f"{result['Probability']*100:.2f}%"
        )

    with c3:

        st.metric(
            "Customer Segment",
            f"Cluster {result['Cluster']}"
        )

    st.divider()

    left, right = st.columns([2,1])

    with left:

        fig = probability_gauge(
            result["Probability"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Prediction Summary")

        summary = pd.DataFrame({

            "Feature":[
                "Prediction",
                "Probability",
                "Cluster"
            ],

            "Value":[
                result["Prediction"],
                f"{result['Probability']*100:.2f}%",
                result["Cluster"]
            ]

        })

        st.dataframe(
            summary,
            hide_index=True,
            use_container_width=True
        )

    st.divider()

    # ============================================================
    # Risk Level
    # ============================================================

    probability = result["Probability"] * 100

    st.subheader("📊 Risk Assessment")

    if probability < 30:

        st.success("🟢 Low Risk Customer")

    elif probability < 60:

        st.warning("🟡 Medium Risk Customer")

    else:

        st.error("🔴 High Risk Customer")

    st.divider()

    # ============================================================
    # Recommendations
    # ============================================================

    st.subheader("💡 Retention Recommendations")

    recommendations = result["Recommendations"]

    if len(recommendations) == 0:

        st.success(
            "No specific recommendation required."
        )

    else:

        for recommendation in recommendations:

            st.info(f"✅ {recommendation}")

    st.divider()

    # ============================================================
    # Business Insights
    # ============================================================

    st.subheader("📈 Business Insights")

    insight_col1, insight_col2 = st.columns(2)

    with insight_col1:

        st.markdown("### Customer Profile")

        st.write(f"**Contract:** {customer['Contract']}")
        st.write(f"**Internet Service:** {customer['InternetService']}")
        st.write(f"**Tenure:** {customer['tenure']} Months")
        st.write(f"**Monthly Charges:** ${customer['MonthlyCharges']:.2f}")

    with insight_col2:

        st.markdown("### Prediction Summary")

        if result["Prediction"] == "Yes":

            st.error(
                """
This customer has a high probability of churn.

Immediate retention action is recommended.
"""
            )

        else:

            st.success(
                """
Customer is likely to remain loyal.

Continue regular customer engagement.
"""
            )

    st.divider()

    # ============================================================
    # Customer Information
    # ============================================================

    with st.expander(
        "📋 Customer Information",
        expanded=False
    ):

        customer_df = pd.DataFrame([customer])

        st.dataframe(
            customer_df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # ============================================================
    # Raw Prediction Output
    # ============================================================

    with st.expander(
        "🧠 Model Output",
        expanded=False
    ):

        st.json(result)

    st.divider()

    # ============================================================
    # Footer
    # ============================================================

    st.caption(
        """
Customer Churn Prediction & Recommendation System

Machine Learning Dashboard powered by
Logistic Regression, K-Means Clustering,
FastAPI and Streamlit.
"""
    )