# app/schemas/branch_schema.py
from typing import Optional

from pydantic import BaseModel


class BranchBase(BaseModel):
    name: str
    address: str

class BranchCreate(BranchBase):
    pass

class BranchResponse(BaseModel):
    id: Optional[int]
    company_id: Optional[int]
    name: str
    address: str

    class Config:
        orm_mode = True

