# app/views/item_view.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.item_controller import (create_item_controller,
                                             delete_item_controller,
                                             get_item_controller,
                                             update_item_controller)
from app.database.db import get_db
from app.schemas.item_schema import ItemCreate, ItemResponse

router = APIRouter()

@router.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item_controller(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.post("/items/", response_model=ItemResponse)
async def create_item_view(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item_controller(db, item)

@router.put("/items/{item_id}", response_model=ItemResponse)
async def update_item_view(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    updated_item = update_item_controller(db, item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return updated_item

@router.delete("/items/{item_id}", response_model=ItemResponse)
async def delete_item_view(item_id: int, db: Session = Depends(get_db)):
    deleted_item = delete_item_controller(db, item_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return deleted_item
