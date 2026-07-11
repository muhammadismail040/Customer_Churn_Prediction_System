"""
Analytics Charts
----------------
Interactive Plotly visualizations for the dashboard.
"""

import plotly.express as px


# ==============================
# Churn Distribution
# ==============================

def churn_distribution(df):

    churn_counts = df["Churn"].value_counts().reset_index()
    churn_counts.columns = ["Churn", "Count"]

    fig = px.pie(
        churn_counts,
        names="Churn",
        values="Count",
        title="Customer Churn Distribution",
        hole=0.45,
    )

    fig.update_layout(title_x=0.5)

    return fig


# ==============================
# Contract Distribution
# ==============================

def contract_distribution(df):

    fig = px.histogram(
        df,
        x="Contract",
        color="Churn",
        barmode="group",
        title="Contract Type Distribution",
    )

    fig.update_layout(title_x=0.5)

    return fig


# ==============================
# Internet Service Distribution
# ==============================

def internet_distribution(df):

    fig = px.histogram(
        df,
        x="InternetService",
        color="Churn",
        barmode="group",
        title="Internet Service Distribution",
    )

    fig.update_layout(title_x=0.5)

    return fig


# ==============================
# Payment Method
# ==============================

def payment_distribution(df):

    fig = px.histogram(
        df,
        x="PaymentMethod",
        color="Churn",
        title="Payment Method Distribution",
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_tickangle=-20,
    )

    return fig


# ==============================
# Monthly Charges
# ==============================

def monthly_charge_distribution(df):

    fig = px.histogram(
        df,
        x="MonthlyCharges",
        nbins=40,
        color="Churn",
        title="Monthly Charges Distribution",
    )

    fig.update_layout(title_x=0.5)

    return fig


# ==============================
# Tenure Distribution
# ==============================

def tenure_distribution(df):

    fig = px.histogram(
        df,
        x="tenure",
        nbins=35,
        color="Churn",
        title="Customer Tenure Distribution",
    )

    fig.update_layout(title_x=0.5)

    return fig


# ==============================
# Monthly Charges vs Tenure
# ==============================

def tenure_vs_charge(df):

    fig = px.scatter(
        df,
        x="tenure",
        y="MonthlyCharges",
        color="Churn",
        title="Monthly Charges vs Tenure",
    )

    fig.update_layout(title_x=0.5)

    return fig