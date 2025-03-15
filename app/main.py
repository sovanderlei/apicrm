# main.py
from fastapi import FastAPI

from app.views.branch_view import router as branch_router
from app.views.company_view import router as company_router
from app.views.db_view import router as db_router
from app.views.general_view import router as general_router
from app.views.item_view import router as item_router

app = FastAPI()

app.include_router(item_router)
app.include_router(db_router) 
app.include_router(company_router)
app.include_router(branch_router)
app.include_router(general_router)
# app.include_router(general_router, prefix="/general")

@app.get("/")
def home():
    return {"message": "API está rodando!"}

