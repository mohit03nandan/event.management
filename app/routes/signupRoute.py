from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.schemas.userSignup import UserSignupSchema
from app.models.userModel import User
from app.middleware import auth

router = APIRouter()

@router.post("/signup")
def signup(user_data: UserSignupSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter_by(username=user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400 , detail="username already registered")
    
    hashed_password = auth.hash_password(user_data.password)
    new_user = User(username=user_data.username,hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "user created successfully"}