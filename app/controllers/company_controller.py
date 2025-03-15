# app/controllers/company_controller.py
from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company_schema import CompanyCreate
from app.services.company_service import (create_company, get_all_companies,
                                          get_company_by_id)


def create_company_controller(db: Session, company: CompanyCreate):
    return create_company(db, company)

def get_company_controller(db: Session, company_id: int): 
    return db.query(Company).options(joinedload(Company.branches)).filter(Company.id == company_id).first() # type: ignore

def get_all_companies_controller(db: Session):
    return get_all_companies(db)

