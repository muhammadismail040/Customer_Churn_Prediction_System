"""
Utility Functions
-----------------
Reusable helper functions for the dashboard.
"""

from pathlib import Path


def project_root():
    """
    Returns the project root directory.
    """
    return Path(__file__).resolve().parent.parent


def processed_data_path():
    """
    Returns processed dataset path.
    """
    return project_root() / "data" / "processed" / "Telco_Customer_Churn_Cleaned.csv"


def reports_path():
    """
    Returns reports folder path.
    """
    return project_root() / "reports"


def models_path():
    """
    Returns models folder path.
    """
    return project_root() / "models"