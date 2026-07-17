"""
Central Logging Configuration

This module creates and manages loggers for:
1. API Requests
2. Predictions
3. Errors
"""

import logging
from pathlib import Path

# ==========================================================
# Create Logs Directory
# ==========================================================

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


# ==========================================================
# Logger Factory
# ==========================================================

def create_logger(name: str, filename: str, level=logging.INFO):
    """
    Create and configure a logger.

    Parameters
    ----------
    name : str
        Logger name.
    filename : str
        Log file name.
    level : int
        Logging level.

    Returns
    -------
    logging.Logger
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate logs
    logger.propagate = False

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            LOG_DIR / filename,
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger


# ==========================================================
# API Logger
# ==========================================================

api_logger = create_logger(
    "api_logger",
    "api.log"
)

# ==========================================================
# Prediction Logger
# ==========================================================

prediction_logger = create_logger(
    "prediction_logger",
    "prediction.log"
)

# ==========================================================
# Error Logger
# ==========================================================

error_logger = create_logger(
    "error_logger",
    "error.log",
    level=logging.ERROR
)