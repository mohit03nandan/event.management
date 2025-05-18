from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def test_connection():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            print("✅ Database connection successful!")
    except SQLAlchemyError as e:
        print("❌ Database connection failed:")
        print(e)
