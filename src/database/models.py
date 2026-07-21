"""
Database Models
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from src.database.database import Base


class PredictionHistory(Base):
    """
    Prediction History Table
    """

    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)

    gender = Column(String)
    senior_citizen = Column(Integer)
    partner = Column(String)
    dependents = Column(String)

    tenure = Column(Integer)

    phone_service = Column(String)
    multiple_lines = Column(String)

    internet_service = Column(String)

    online_security = Column(String)
    online_backup = Column(String)
    device_protection = Column(String)
    tech_support = Column(String)

    streaming_tv = Column(String)
    streaming_movies = Column(String)

    contract = Column(String)

    paperless_billing = Column(String)

    payment_method = Column(String)

    monthly_charges = Column(Float)
    total_charges = Column(Float)

    prediction = Column(String)

    probability = Column(Float)

    cluster = Column(Integer)

    recommendations = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )