"""
Business Metrics
----------------
All dashboard KPI calculations.
"""

import pandas as pd

from utils import processed_data_path


# =====================================================
# Load Dataset
# =====================================================

def load_data():

    df = pd.read_csv(processed_data_path())

    return df


# =====================================================
# KPI Functions
# =====================================================

def total_customers(df):

    return len(df)


def churn_rate(df):

    churn = (df["Churn"] == "Yes").mean() * 100

    return round(churn, 2)


def retention_rate(df):

    retain = (df["Churn"] == "No").mean() * 100

    return round(retain, 2)


def total_segments():

    return 4


def model_accuracy():

    return 80.62


def high_risk_customers():
    """
    Placeholder.

    We will calculate this
    after integrating the model.
    """

    return "--"