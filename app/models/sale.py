# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from app.db.base_class import Base


class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    total_price = Column(Float)
    date_time = Column(DateTime, default=datetime.utcnow)

    product = relationship('Product', back_populates='sales')
