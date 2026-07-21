"""
Database Configuration
"""
from contextlib import asynccontextmanager
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Load .env variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL not found in .env")

# SQLAlchemy Engine
engine = create_engine(
    DATABASE_URL,
    echo=True,
)

# Database Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base Class
Base = declarative_base()


def get_db():
    """
    Database Dependency
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@asynccontextmanager
async def get_db_session():
    """
    Async Database Session Dependency
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """
    Create all database tables.
    """

    Base.metadata.create_all(bind=engine)