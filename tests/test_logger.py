from src.utils.logger import (
    api_logger,
    prediction_logger,
    error_logger,
)

api_logger.info("API logger is working.")

prediction_logger.info(
    "Prediction logger is working."
)

error_logger.error(
    "Error logger is working."
)

print("Logging completed successfully.")