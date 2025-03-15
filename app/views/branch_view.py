# app/views/branch_view.py s
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.branch_controller import (
    create_branch_controller, get_branch_controller,
    get_branches_by_company_controller)
from app.controllers.company_controller import create_company_controller
from app.database.db import get_db
from app.schemas.branch_schema import BranchCreate, BranchResponse

router = APIRouter()

@router.get("/companies/{company_id}/branches", response_model=List[BranchResponse])
async def read_branches(company_id: int, db: Session = Depends(get_db)):
    branches = get_branches_by_company_controller(db, company_id)
    return branches

@router.get("/branches/{branch_id}", response_model=BranchResponse)
async def read_branch(branch_id: int, db: Session = Depends(get_db)):
    branch = get_branch_controller(db, branch_id)
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch

@router.post("/branches/", response_model=BranchResponse)
async def create_branch_view(branch: BranchCreate, company_id: int, db: Session = Depends(get_db)):
    return create_branch_controller(db, branch, company_id)

@router.delete("/branches/{branch_id}", response_model=dict)
async def delete_branch(branch_id: int, db: Session = Depends(get_db)):
    branch = get_branch_controller(db, branch_id)
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    db.delete(branch)
    db.commit()
    return {"message": "Branch deleted successfully"}

@router.put("/branches/{branch_id}", response_model=BranchResponse)
async def update_branch(branch_id: int, branch_update: BranchCreate, db: Session = Depends(get_db)):
    branch = get_branch_controller(db, branch_id)
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    branch.name = branch_update.name
    branch.address = branch_update.address
    db.commit()
    db.refresh(branch)

    return branch
