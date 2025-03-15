# app/controllers/branch_controller.py
from sqlalchemy.orm import Session

from app.schemas.branch_schema import BranchCreate
from app.services.branch_service import (create_branch, get_branch_by_id,
                                         get_branches_by_company_id)


def create_branch_controller(db: Session, branch: BranchCreate, company_id: int):
    return create_branch(db, branch, company_id)

def get_branches_by_company_controller(db: Session, company_id: int):
    return get_branches_by_company_id(db, company_id)

def get_branch_controller(db: Session, branch_id: int):
    return get_branch_by_id(db, branch_id)
