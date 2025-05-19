from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.schemas.userLogin import userLoginSchema
from app.models.userModel import User
from app.middleware import auth 

router = APIRouter()

@router.post("/login")
def login(user_data: userLoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=user_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not auth.verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    token = auth.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
