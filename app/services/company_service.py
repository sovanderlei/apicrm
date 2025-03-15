# app/services/company_service.py  
from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company_schema import CompanyCreate


def create_company(db: Session, company: CompanyCreate):
    db_company = Company(name=company.name, description=company.description)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()

def get_all_companies(db: Session):
    return db.query(Company).all()
