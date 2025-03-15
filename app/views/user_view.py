from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.user_controller import create_user_controller
from app.database.db import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_controller(user, db)

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
