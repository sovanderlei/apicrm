# app/views/company_view.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.controllers.branch_controller import create_branch_controller
from app.controllers.company_controller import (create_company_controller,
                                                get_all_companies_controller,
                                                get_company_controller)
from app.database import db
from app.database.db import get_db
from app.models.company import Company
from app.schemas.branch_schema import BranchCreate, BranchResponse
from app.schemas.company_schema import CompanyCreate, CompanyResponse
from app.views.auth_view import get_current_user

router = APIRouter()

@router.get("/companies")
#  @router.get("/companies", dependencies=[Depends(get_current_user)]) # authenticated
async def get_companies_with_branches(db: Session = Depends(get_db)):
    companies = db.query(Company).all()

    result = []
    for company in companies:
        branches = [
            BranchResponse(
                id=branch.id,
                company_id=branch.company_id,
                name=branch.name,
                address=branch.address
            )
            for branch in company.branches
        ]

        result.append({
            "company_name": company.name,
            "description": company.description,
            "branches": branches
        })

    return result

@router.get("/companies/{company_id}", response_model=CompanyResponse)
async def read_company(company_id: int, db: Session = Depends(get_db)):
    company = get_company_controller(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.post("/companies/", response_model=CompanyResponse)
async def create_company_view(company: CompanyCreate, db: Session = Depends(get_db)): 
    existing_company = db.query(Company).filter(Company.name == company.name).first()
    if existing_company:
        raise HTTPException(status_code=400, detail="Company already exists")
 
    new_company = create_company_controller(db, company)
    return new_company

@router.delete("/companies/{company_id}", response_model=dict)
async def delete_company(company_id: int, db: Session = Depends(get_db)):
    company = get_company_controller(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    db.delete(company)
    db.commit()
    return {"message": "Company deleted successfully"}

@router.put("/companies/{company_id}", response_model=CompanyResponse)
async def update_company(company_id: int, company_update: CompanyCreate, db: Session = Depends(get_db)):
    company = get_company_controller(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    company.name = company_update.name
    company.description = company_update.description
    db.commit()
    db.refresh(company)

    return company

@router.get("/companiescadtest")
async def companies_cad_test(db: Session = Depends(get_db)):   
    companies_data = [
        {"name": "Company 1", "description": "A primeira empresa"},
        {"name": "Company 2", "description": "A segunda empresa"}
    ]

    created_companies = [] 

    for company_data in companies_data:
        company_create = CompanyCreate(**company_data)
        company = create_company_controller(db, company_create)
        created_companies.append(company)

        branches_data = [
            {"name": f"{company.name} - Filial 1", "address": "Endereço 1"},
            {"name": f"{company.name} - Filial 2", "address": "Endereço 2"}
        ]

        for branch_data in branches_data:
            branch_create = BranchCreate(**branch_data)
            create_branch_controller(db, branch_create, company.id)

    return {"message": "Successfully created companies and branches!"}
