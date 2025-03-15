# app/schemas/company_schema.py 
from typing import List, Optional

from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str
    description: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: int
    branches: List[str] = []  

    class Config:
        orm_mode = True
