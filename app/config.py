import os

class Config:
    # Use DATABASE_URL if provided; otherwise, default to a local SQLite database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///budget.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
