# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.db.base_class import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    price = Column(Float)

    category = relationship('Category', back_populates='products')
    inventory = relationship("Inventory", back_populates="product")
    sales = relationship("Sale", back_populates="product")
