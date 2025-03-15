from sqlalchemy import Column, Float, Integer, String

from app.database.db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True) 
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=True)

    def __repr__(self):
        return f"<Item(name={self.name}, price={self.price}, tax={self.tax})>"
