from pathlib import Path
import joblib

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Models directory
MODELS_DIR = BASE_DIR / "models"

# Load Churn Prediction Model
model = joblib.load(MODELS_DIR / "best_model" / "churn_prediction_model.pkl")

# Load Preprocessing Pipeline
preprocessor = joblib.load(
    MODELS_DIR / "preprocessors" / "preprocessing_pipeline.pkl"
)

# Load Target Encoder
target_encoder = joblib.load(
    MODELS_DIR / "preprocessors" / "target_encoder.pkl"
)

# Load Customer Segmentation Model
kmeans_model = joblib.load(
    MODELS_DIR / "segmentation" / "kmeans_model.pkl"
)

# Load Scaler
scaler = joblib.load(
    MODELS_DIR / "segmentation" / "scaler.pkl"
)