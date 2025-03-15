import os

from fastapi import APIRouter
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import OperationalError

from app.database.db import Base, engine
from app.models.branch import Branch
from app.models.company import Company
from app.models.item import Item

router = APIRouter()

MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DB", "crm_db")

# DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/"
DATABASE_URL = "mysql+pymysql://root:password@mysql/crm_db"


DROP_DATABASE_IF_EXISTS = os.getenv("DROP_DATABASE", "false").lower() == "true"

def create_database():
    """Cria o banco de dados se ele não existir."""
    engine_tmp = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT")
    with engine_tmp.connect() as conn:
        if DROP_DATABASE_IF_EXISTS:
            conn.execute(text(f"DROP DATABASE IF EXISTS {MYSQL_DB};"))
            print(f"Banco de dados {MYSQL_DB} excluído!")

        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"))
        print(f"Banco de dados {MYSQL_DB} criado!")

def create_tables():
    """Cria as tabelas apenas se elas ainda não existirem."""
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    tables_to_create = [table.__tablename__ for table in Base.__subclasses__() if table.__tablename__ not in existing_tables]

    if tables_to_create:
        Base.metadata.create_all(bind=engine)
        print(f"Tables created successfully: {tables_to_create}")
        return {"message": f"Tables created successfully: {tables_to_create}"}
    else:
        print("All tables already exist. No tables were recreated.")
        return {"message": "All tables already exist. No tables were recreated."}

@router.get("/createtablesforce")
def create_tables_endpoint():
    """Endpoint to create database and tables via API."""
    try:
        create_database()
        return create_tables()
    except OperationalError as e:
        return {"error": f"Error connecting to MySQL: {str(e)}"}
