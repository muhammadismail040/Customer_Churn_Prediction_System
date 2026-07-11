"""
Prediction History
------------------
Stores every dashboard prediction into a CSV file.
"""

from pathlib import Path
import pandas as pd


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

REPORTS_DIR = PROJECT_ROOT / "reports"

HISTORY_FILE = REPORTS_DIR / "prediction_history.csv"


# ==========================================================
# Create Reports Folder
# ==========================================================

REPORTS_DIR.mkdir(exist_ok=True)


# ==========================================================
# Create History File
# ==========================================================

def initialize_history():

    """
    Creates prediction_history.csv if it doesn't exist.
    """

    if not HISTORY_FILE.exists():

        columns = [

            "Prediction",

            "Probability",

            "Cluster",

            "Timestamp"

        ]

        df = pd.DataFrame(columns=columns)

        df.to_csv(HISTORY_FILE, index=False)


# ==========================================================
# Save Prediction
# ==========================================================

def save_prediction(result):

    """
    Save one prediction into history.
    """

    initialize_history()

    history = pd.read_csv(HISTORY_FILE)

    new_row = {

        "Prediction": result["Prediction"],

        "Probability": round(result["Probability"], 4),

        "Cluster": result["Cluster"],

        "Timestamp": pd.Timestamp.now()

    }

    history.loc[len(history)] = new_row

    history.to_csv(HISTORY_FILE, index=False)


# ==========================================================
# Load Prediction History
# ==========================================================

def load_history():

    initialize_history()

    return pd.read_csv(HISTORY_FILE)


# ==========================================================
# Total Predictions
# ==========================================================

def total_predictions():

    history = load_history()

    return len(history)


# ==========================================================
# Churn Predictions
# ==========================================================

def churn_predictions():

    history = load_history()

    return len(

        history[history["Prediction"] == "Yes"]

    )


# ==========================================================
# Safe Predictions
# ==========================================================

def safe_predictions():

    history = load_history()

    return len(

        history[history["Prediction"] == "No"]

    )