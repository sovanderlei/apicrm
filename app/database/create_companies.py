from db import SessionLocal

from app.models.company import Company


def create_companies():
    db = SessionLocal()
    try:
        company1 = Company(name="Company 1", description="A primeira empresa")
        company2 = Company(name="Company 2", description="A segunda empresa")
        
        db.add(company1)
        db.add(company2)
        db.commit()
        db.refresh(company1)
        db.refresh(company2)

        print(f"Company 1: {company1.id}, Company 2: {company2.id}")
    except Exception as e:
        print(f"Erro ao criar empresas: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_companies()
