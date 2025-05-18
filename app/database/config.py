from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def test_connection():
    try:
        with engine.connect() as connection:
            print("✅ Database connection successful!")
    except SQLAlchemyError as e:
        print("❌ Database connection failed:")
        print(e)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from app.models.userModel import Base  
from app.database.config import engine  

Base.metadata.create_all(bind=engine)
