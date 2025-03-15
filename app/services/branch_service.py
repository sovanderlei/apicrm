# app/services/branch_service.py
from sqlalchemy.orm import Session

from app.models.branch import Branch
from app.schemas.branch_schema import BranchCreate


def create_branch(db: Session, branch: BranchCreate, company_id: int):
    db_branch = Branch(name=branch.name, address=branch.address, company_id=company_id)
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch

def get_branches_by_company_id(db: Session, company_id: int):
    return db.query(Branch).filter(Branch.company_id == company_id).all()

def get_branch_by_id(db: Session, branch_id: int):
    return db.query(Branch).filter(Branch.id == branch_id).first()
