# app/controllers/item_controller.py
from sqlalchemy.orm import Session

from app.schemas.item_schema import ItemCreate
from app.services.item_service import (create_item, delete_item,
                                       get_item_by_id, update_item)


def create_item_controller(db: Session, item: ItemCreate):
    return create_item(db, item)

def get_item_controller(db: Session, item_id: int):
    return get_item_by_id(db, item_id)

def update_item_controller(db: Session, item_id: int, item: ItemCreate):
    return update_item(db, item_id, item)

def delete_item_controller(db: Session, item_id: int):
    return delete_item(db, item_id)
