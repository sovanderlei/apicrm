from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.user_schema import UserCreate
from app.services.user_service import create_user, get_user_by_email


def create_user_controller(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)
